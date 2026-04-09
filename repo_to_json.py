import os
import json
from typing import Dict, List
from ai_module2 import askai

# Конфигурация
CACHE_DIR = "tech_mapping_cache"
OUTPUT_FILE = "technology_matrix.json"
GITHUB_USER = "PavelT2000"

def read_readme(repo_path: str) -> str:
    """Читает README, ограничиваясь 5000 символами для экономии контекста AI."""
    for filename in ['README.md', 'readme.md', 'README.txt', 'ReadMe.md']:
        p = os.path.join(repo_path, filename)
        if os.path.exists(p):
            try:
                with open(p, 'r', encoding='utf-8') as f:
                    return f.read(5000)
            except Exception as e:
                print(f"Ошибка чтения {p}: {e}")
    return ""

def get_normalized_techs(repo_name: str, readme: str) -> List[str]:
    """AI-экстрактор технологий с нормализацией."""
    prompt = (
        f"Analyze project '{repo_name}'. Extract technologies, frameworks, and databases. "
        f"Normalize: use '.NET 8', 'React', 'PostgreSQL', 'Docker'. "
        f"Return ONLY a JSON array of strings."
        f"\n\nREADME CONTENT:\n{readme}"
    )

    try:
        response = askai(prompt, system_message="Return clean JSON array only.", temperature=0)
        clean = response.strip().replace("```json", "").replace("```", "").strip()
        return json.loads(clean)
    except Exception as e:
        print(f"AI Error for {repo_name}: {e}")
        return []

def build_tech_matrix(root_path: str):
    # 1. Подготовка папок и загрузка старой матрицы (если есть)
    if not os.path.exists(CACHE_DIR):
        os.makedirs(CACHE_DIR)

    tech_matrix: Dict[str, List[str]] = {}

    # Пытаемся загрузить уже готовую матрицу, чтобы дополнить её, а не перезаписать
    if os.path.exists(OUTPUT_FILE):
        with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
            tech_matrix = json.load(f)
        print(f"Загружена существующая матрица: {len(tech_matrix)} технологий.")

    # 2. Сканирование директорий
    subdirs = [d for d in os.listdir(root_path) if os.path.isdir(os.path.join(root_path, d))]
    print(f"Найдено репозиториев для проверки: {len(subdirs)}")

    for repo_name in subdirs:
        repo_path = os.path.join(root_path, repo_name)

        # Пропускаем, если это не git-репозиторий
        if not os.path.exists(os.path.join(repo_path, '.git')):
            continue

        cache_path = os.path.join(CACHE_DIR, f"{repo_name}.json")
        repo_url = f"https://github.com/{GITHUB_USER}/{repo_name}"

        current_techs = []

        # --- КЕШИРОВАНИЕ ---
        if os.path.exists(cache_path):
            # Если файл в кеше есть — просто читаем список технологий
            try:
                with open(cache_path, "r", encoding="utf-8") as f:
                    current_techs = json.load(f)
                print(f"[-] {repo_name} взят из кеша.")
            except:
                current_techs = []

        if not current_techs:
            # Если в кеше нет — идем к AI
            readme = read_readme(repo_path)
            if not readme:
                print(f"[!] {repo_name} пропущен (нет README).")
                continue

            print(f"[+] AI Анализ: {repo_name}...")
            current_techs = get_normalized_techs(repo_name, readme)

            # Сохраняем результат в кеш немедленно
            with open(cache_path, "w", encoding="utf-8") as f:
                json.dump(current_techs, f, ensure_ascii=False, indent=2)

        # 3. Обновление итоговой матрицы
        for tech in current_techs:
            if tech not in tech_matrix:
                tech_matrix[tech] = []
            if repo_url not in tech_matrix[tech]:
                tech_matrix[tech].append(repo_url)

    # 4. Финальное сохранение
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(tech_matrix, f, ensure_ascii=False, indent=4)

    print(f"\n=== ГОТОВО ===")
    print(f"Уникальных технологий: {len(tech_matrix)}")
    print(f"Результат в: {OUTPUT_FILE}")

if __name__ == "__main__":
    target_path = input("Укажите путь к папке с репозиториями (Enter для текущей): ").strip() or "."
    build_tech_matrix(target_path)