import os
import logging
import shutil  # Добавлено для перемещения файлов
from git import Repo
from ai_module4 import askai
import pathspec

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

CONTEXT_BUDGET = 15000

DEFAULT_IGNORE = [
    '**/bin/', '**/obj/', '**/Release/', '**/Debug/', '**/.vs/',
    '**/*.sln', '**/*.slnx', '**/*.suo', '**/*.user', '**/*.vsidx',
    '**/*.cache', '**/packages/', '**/*.bin', '**/*.exe', '**/*.dll',
    '**/*.pdb', '**/node_modules/', '**/.git/', 'compressedcontext.txt', 'oldreadme/'
]

# ... (функции get_ignored_spec, get_filtered_files, generate_tree_hierarchy без изменений) ...

def get_ignored_spec(repo_path: str) -> pathspec.PathSpec:
    patterns = DEFAULT_IGNORE.copy()
    ignore_file = os.path.join(repo_path, '.aiignore')
    if os.path.exists(ignore_file):
        with open(ignore_file, 'r', encoding='utf-8') as f:
            patterns.extend([line.strip() for line in f if line.strip() and not line.startswith('#')])
    return pathspec.PathSpec.from_lines('gitwildmatch', patterns)

def get_filtered_files(working_dir: str, spec: pathspec.PathSpec):
    valid_files = []
    for root_dir, dirs, files in os.walk(working_dir):
        dirs[:] = [d for d in dirs if not spec.match_file(os.path.relpath(os.path.join(root_dir, d), working_dir) + '/')]
        for f in files:
            rel_path = os.path.relpath(os.path.join(root_dir, f), working_dir)
            if not spec.match_file(rel_path):
                valid_files.append(rel_path)
    return sorted(valid_files)

def generate_tree_hierarchy(files_list: list) -> str:
    tree = {}
    for path in files_list:
        parts = path.split(os.sep)
        current = tree
        for part in parts:
            current = current.setdefault(part, {})
    lines = []
    def build(t, indent=""):
        keys = sorted(t.keys())
        for i, key in enumerate(keys):
            is_last = (i == len(keys) - 1)
            marker = "└── " if is_last else "├── "
            lines.append(f"{indent}{marker}{key}")
            extension = "    " if is_last else "│   "
            build(t[key], indent + extension)
    build(tree)
    return "\n".join(lines)

def create_compressed_context(repo_path: str, spec: pathspec.PathSpec, target_branch: str) -> str:
    repo = Repo(repo_path)
    repo.git.checkout(target_branch)
    working_dir = str(repo.working_tree_dir)
    all_files = get_filtered_files(working_dir, spec)
    project_hierarchy = generate_tree_hierarchy(all_files)
    files_summary = []
    for path in all_files:
        try:
            size = os.path.getsize(os.path.join(working_dir, path))
            files_summary.append(f"{path} [{size} bytes]")
        except: continue

    logging.info(f"[*] ИИ выбирает код (Бюджет: {CONTEXT_BUDGET} симв.)...")
    selection_prompt = (
        f"Project: {os.path.basename(repo_path)}\n"
        f"Full Hierarchy:\n{project_hierarchy[:3000]}\n\n"
        f"Available files for content extraction:\n{ ' | '.join(files_summary[:500]) }\n\n"
        f"TASK: Select key files for the README context. Total size < {CONTEXT_BUDGET} bytes.\n"
        f"Return ONLY comma-separated paths."
    )
    important_files_raw = askai(selection_prompt, system_message="Architect mode. Select essential files.")
    important_files = [f.strip().strip('"`\'') for f in important_files_raw.split(',')]
    final_content = ["=== PROJECT HIERARCHY ===", project_hierarchy, "\n=== SOURCE CODE ==="]
    current_size = len(project_hierarchy)
    for path in important_files:
        full_p = os.path.join(working_dir, path)
        if os.path.exists(full_p) and os.path.isfile(full_p):
            try:
                file_size = os.path.getsize(full_p)
                if current_size + file_size > CONTEXT_BUDGET * 1.3: break
                with open(full_p, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    if '\0' in content: continue
                    final_content.append(f"\n--- FILE: {path} ---\n{content}")
                    current_size += len(content)
            except: continue
    compressed_text = "\n".join(final_content)
    context_path = os.path.join(working_dir, 'compressedcontext.txt')
    with open(context_path, 'w', encoding='utf-8') as f:
        f.write(compressed_text)
    return compressed_text

def process_readme(repo_path: str):
    repo = Repo(repo_path)
    repo_name = os.path.basename(repo_path)
    compressed_file = os.path.join(repo_path, 'compressedcontext.txt')
    readme_file = os.path.join(repo_path, 'README.md')
    old_readme_dir = os.path.join(repo_path, 'oldreadme')

    # 0. СКИП: Если есть и контекст, и ридми
    if os.path.exists(compressed_file) and os.path.exists(readme_file):
        logging.info(f"[-] {repo_name} уже обработан (есть и контекст, и README). Пропуск.")
        return

    # 1. БЭКАП: Если есть только README, переносим его
    if os.path.exists(readme_file) and not os.path.exists(compressed_file):
        logging.info(f"[*] Найден старый README в {repo_name} без контекста. Переносим в oldreadme.")
        if not os.path.exists(old_readme_dir):
            os.makedirs(old_readme_dir)
        # Переименовываем с добавлением времени, чтобы не затереть другие бэкапы
        backup_path = os.path.join(old_readme_dir, 'README.md')
        shutil.move(readme_file, backup_path)

    # Определение веток
    raw_branches = [ref.name for ref in repo.references if 'HEAD' not in ref.name]
    if not raw_branches: return
    branch_map = {ref.split('/')[-1]: ref for ref in raw_branches}
    branches = list(branch_map.keys())
    target_branch = "main" if "main" in branches else ("master" if "master" in branches else branches[0])
    spec = get_ignored_spec(repo_path)

    # 2. ШАГ 1: Создание контекста
    if not os.path.exists(compressed_file):
        logging.info(f"=== [ПРОХОД 1] Сбор данных для {repo_name} ===")
        create_compressed_context(repo_path, spec, target_branch)
        logging.info(f"[!] Контекст готов для {repo_name}. Запустите снова для генерации.")
        return

    # 3. ШАГ 2: Генерация README
    logging.info(f"=== [ПРОХОД 2] Генерация README для {repo_name} ===")
    with open(compressed_file, 'r', encoding='utf-8') as f:
        project_context = f.read()

    readme_prompt = (
        f"Project Name: {repo_name}\n"
        f"Context:\n{project_context}\n\n"
        "Generate a professional README.md."
    )

    readme_content = askai(readme_prompt, system_message="Technical Writer mode.", temperature=0.3)

    repo.git.checkout(target_branch)
    with open(readme_file, 'w', encoding='utf-8') as f:
        f.write(readme_content)

    logging.info(f"[+] README.md успешно создан для {repo_name}!")

if __name__ == "__main__":
    root = input("Путь к репозиториям: ").strip()
    for d in os.listdir(root):
        full_d = os.path.join(root, d)
        if os.path.isdir(full_d) and os.path.exists(os.path.join(full_d, '.git')):
            try:
                process_readme(full_d)
            except Exception as e:
                logging.error(f"Ошибка в {d}: {e}")