import os
import logging
from git import Repo, GitCommandError
from ai_module2 import askai

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)

def get_repo_structure(repo: Repo, branch_name: str) -> str:
    return repo.git.ls_tree('-r', '--name-only', branch_name)

def process_repositories(root_path: str):
    if not os.path.exists(root_path):
        raise ValueError(f"Путь {root_path} не существует!")

    subdirs = [os.path.join(root_path, d) for d in os.listdir(root_path)
               if os.path.isdir(os.path.join(root_path, d))]

    for repo_path in subdirs:
        if not os.path.exists(os.path.join(repo_path, '.git')):
            continue

        repo_name = os.path.basename(repo_path)
        logging.info(f"--- Репозиторий: {repo_name} ---")
        repo = Repo(repo_path)

        if not repo.heads:
            logging.warning(f"  [!] {repo_name} пуст. Пропуск.")
            continue

        # 1. Пытаемся запомнить текущую ветку
        try:
            original_branch = repo.active_branch.name
        except (TypeError, ValueError):
            original_branch = repo.head.commit.hexsha

        try:
            # 2. Собираем ВСЕ ветки (локальные + удаленные)
            # remote_branches вернет имена вроде 'origin/main', чистим их
            all_refs = [ref.name.split('/')[-1] for ref in repo.references]
            branches = list(set(all_refs))
            # Оставляем только осмысленные ветки (убираем HEAD, теги и т.д.)
            branches = [b for b in branches if b not in ['HEAD', 'origin']]

            for branch_name in branches:
                try:
                    logging.info(f"  Ветка: {branch_name}")
                    repo.git.checkout(branch_name)
                except GitCommandError:
                    logging.warning(f"    [!] Не удалось чекаутнуть {branch_name}. Пропуск.")
                    continue

                aiignore_path = os.path.join(repo_path, '.aiignore')

                if os.path.exists(aiignore_path):
                    logging.info(f"    [~] .aiignore уже на месте.")
                    continue

                structure = get_repo_structure(repo, branch_name)
                if not structure: continue

                logging.info(f"    Запрос AI для {branch_name}...")
                aiignore_content = askai(
                    prompt=f"Structure:\n{structure}\nGenerate .aiignore",
                    system_message="Output ONLY raw content.",
                    temperature=0.0
                )

                if not aiignore_content:
                    raise RuntimeError(f"AI Service отказал в ответе для {repo_name}!")

                with open(aiignore_path, 'w', encoding='utf-8') as f:
                    f.write(aiignore_content.strip())

                # Прямой коммит
                repo.git.add('.aiignore')
                repo.git.commit('-m', 'chore: add .aiignore for AI context')
                logging.info(f"    [+] .aiignore закоммичен!")

        except Exception as e:
            logging.error(f"!!! КРИТИЧЕСКИЙ СБОЙ в {repo_name}: {e}")
            raise

        finally:
            # 3. АВТОВОЗВРАТ НА ЖИВУЮ ВЕТКУ
            # Приоритет: 1. main, 2. master, 3. то что было в начале
            available = [b.name for b in repo.branches]
            target = None

            if "main" in available: target = "main"
            elif "master" in available: target = "master"
            elif original_branch in available: target = original_branch

            if target:
                logging.info(f"  [=>] Финальный переход на ветку: {target}")
                repo.git.checkout(target)
            else:
                # Если всё совсем плохо, просто остаемся где были
                logging.warning(f"  [!] Не удалось найти стабильную ветку для возврата.")

if __name__ == "__main__":
    path_to_repos = input("Введите путь к папке с репозиториями: ").strip()
    process_repositories(path_to_repos)
    logging.info("ГОТОВО. Все файлы на своих местах.")




