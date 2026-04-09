import os
import logging
import json
from typing import Optional, List, Dict, Any
from ai_module5 import askai

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Описание схемы данных
RESUME_EXTRACTOR_TOOL = [
    {
        "type": "function",
        "function": {
            "name": "save_project_info",
            "description": "Сохраняет структурированную информацию о проекте из README",
            "parameters": {
                "type": "object",
                "properties": {
                    "project_name": {"type": "string", "description": "Название репозитория"},
                    "summary": {"type": "string", "description": "Краткое описание сути (1-2 предложения)"},
                    "technologies": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Список использованных технологий"
                    },
                    "key_features": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Список ключевых особенностей"
                    },
                    "achievements": {"type": "string", "description": "Технические вызовы и решенные задачи"}
                },
                "required": ["project_name", "summary", "technologies", "key_features", "achievements"]
            }
        }
    }
]

def read_readme(repo_path: str) -> str:
    """Ищет и читает файл README."""
    for filename in ['README.md', 'readme.md', 'README.txt', 'ReadMe.md']:
        p = os.path.join(repo_path, filename)
        if os.path.exists(p):
            try:
                with open(p, 'r', encoding='utf-8') as f:
                    return f.read()
            except Exception as e:
                logging.error(f"Ошибка при чтении {p}: {e}")
    return ""

def final_merge(cache_dir: str, output_file: str):
    """Собирает все промежуточные JSON файлы в один итоговый массив."""
    logging.info("=== Сборка финального файла из кеша ===")
    all_projects = []

    if not os.path.exists(cache_dir):
        logging.warning("Кеш пуст, нечего объединять.")
        return

    for filename in os.listdir(cache_dir):
        if filename.endswith(".json"):
            file_path = os.path.join(cache_dir, filename)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    all_projects.append(json.load(f))
            except Exception as e:
                logging.error(f"Ошибка чтения файла кеша {filename}: {e}")

    try:
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(all_projects, f, ensure_ascii=False, indent=4)
        logging.info(f"=== ГОТОВО! Все данные ({len(all_projects)} шт.) сохранены в {output_file} ===")
    except Exception as e:
        logging.error(f"Критическая ошибка сохранения: {e}")

def collect_json_data(root_path: str, cache_dir: str = "process_cache"):
    """Основной процесс сканирования и обращения к AI."""
    if not os.path.exists(root_path):
        raise ValueError(f"Путь {root_path} не существует!")

    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)

    subdirs = [os.path.join(root_path, d) for d in os.listdir(root_path)
               if os.path.isdir(os.path.join(root_path, d))]

    github_username = "PavelT2000"

    for repo_path in subdirs:
        # Проверяем, что это папка с кодом (наличие .git)
        if not os.path.exists(os.path.join(repo_path, '.git')):
            continue

        repo_name = os.path.basename(repo_path)
        cache_file = os.path.join(cache_dir, f"{repo_name}.json")

        # Если уже обрабатывали этот репо — пропускаем
        if os.path.exists(cache_file):
            logging.info(f"--- {repo_name} загружен из кеша ---")
            continue

        readme_content = read_readme(repo_path)
        if not readme_content or len(readme_content.strip()) < 50:
            logging.warning(f"Пропуск {repo_name}: README пуст или слишком мал.")
            continue

        logging.info(f"--- AI анализ проекта: {repo_name} ---")

        prompt = (
            f"Analyze the following README from the project '{repo_name}' and extract technical data. "
            f"Focus on personal contribution, stack, and complex tasks solved.\n\n"
            f"README CONTENT:\n{readme_content[:5000]}"
        )

        try:
            response_str = askai(
                prompt=prompt,
                system_message="You are a professional IT-recruiter. Use the tool to output clean JSON.",
                temperature=0,
                tools=RESUME_EXTRACTOR_TOOL
            )

            # Чистим Markdown, если AI его добавил
            clean_json = response_str.strip()
            if "```" in clean_json:
                clean_json = clean_json.split("```")[1]
                if clean_json.startswith("json"):
                    clean_json = clean_json[4:]

            project_data = json.loads(clean_json.strip())

            # Указываем твой GitHub ник в URL
            project_data["repo_url"] = f"https://github.com/{github_username}/{repo_name}"

            # Пишем временный файл
            with open(cache_file, "w", encoding="utf-8") as f:
                json.dump(project_data, f, ensure_ascii=False, indent=4)

        except Exception as e:
            logging.error(f"Сбой на репозитории {repo_name}: {e}")

    # После завершения цикла собираем все "кусочки" в один файл
    final_merge(cache_dir, "extracted_resume_data.json")

if __name__ == "__main__":
    target = input("Укажите путь к папке с репозиториями: ").strip() or "."
    collect_json_data(target)