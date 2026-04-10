import os
import requests
import time
from github import Github
from dotenv import load_dotenv
from tqdm import tqdm

load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
AI_URL = os.getenv("AI_SERVICE_URL")
OUTPUT_DIR = "summaries"

# Создаем папку, если её нет
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Промпт теперь просит краткий текст, а не JSON
SYSTEM_PROMPT = (
    "Ты — технический писатель. Твоя задача — максимально сжать README репозитория. "
    "Оставь только суть: стек технологий, основные фичи и архитектурные решения. "
    "Пиши сухо и плотно, без лишних вступлений. Максимум 2-3 абзаца."
)

def get_ai_summary(readme_text):
    payload = {
        "contents": [
            {
                "role": "user",
                "parts": [{"text": f"Сделай краткое описание этого проекта:\n\n{readme_text}"}]
            }
        ],
        "system_instruction": SYSTEM_PROMPT,
        "temperature": 0.3,
        "max_output_tokens": 800
    }
    
    try:
        response = requests.post(AI_URL, json=payload, timeout=60)
        response.raise_for_status()
        data = response.json()
        return data.get("answer", "").strip()
    except Exception as e:
        return None

def main():
    g = Github(GITHUB_TOKEN)
    user = g.get_user()
    
    repos = list(user.get_repos())
    print(f"🔍 Найдено репозиториев: {len(repos)}")

    for repo in tqdm(repos, desc="Сжатие README"):
        if repo.archived:
            continue
            
        # Формируем имя файла (заменяем спецсимволы, если они есть в названии репо)
        safe_name = repo.name.replace("/", "_")
        file_path = os.path.join(OUTPUT_DIR, f"{safe_name}.txt")
        
        # Прогресс: если файл уже есть, пропускаем
        if os.path.exists(file_path):
            continue

        try:
            readme_obj = repo.get_readme()
            readme_text = readme_obj.decoded_content.decode('utf-8')
            
            # Отправляем в ИИ
            summary = get_ai_summary(readme_text[:8000])
            
            if summary:
                # Добавляем в начало файла ссылку на репозиторий для удобства
                full_content = f"URL: {repo.html_url}\n\n{summary}"
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(full_content)
                
            time.sleep(0.3) # Маленькая пауза для стабильности
            
        except Exception:
            # Если README нет или ошибка доступа — просто идем к следующему
            continue

    print(f"\n✨ Готово! Все сжатые файлы лежат в папке '{OUTPUT_DIR}'")

if __name__ == "__main__":
    main()