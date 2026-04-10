import os
import json
import requests
import time
from dotenv import load_dotenv
from tqdm import tqdm

load_dotenv()
EMBED_URL = os.getenv("EMBED_SERIVCE_URL")
INPUT_DIR = "summaries"
OUTPUT_FILE = "vector_store.json"

def get_embedding(text, title=""):
    """
    Отправляет текст в твой сервис эмбеддингов.
    Использует структуру: {"text": "...", "task_type": "RETRIEVAL_QUERY", "title": "..."}
    """
    payload = {
        "text": text,
        "task_type": "RETRIEVAL_DOCUMENT", # Для документов лучше использовать DOCUMENT
        "title": title
    }
    
    try:
        response = requests.post(EMBED_URL, json=payload, timeout=30)
        response.raise_for_status()
        data = response.json()
        return data.get("embedding")
    except Exception as e:
        print(f"Ошибка при получении эмбеддинга для {title}: {e}")
        return None

def main():
    if not os.path.exists(INPUT_DIR):
        print(f"❌ Папка {INPUT_DIR} не найдена!")
        return

    vector_store = []
    files = [f for f in os.listdir(INPUT_DIR) if f.endswith(".txt")]
    
    print(f"🧬 Начинаем векторизацию {len(files)} файлов...")

    for filename in tqdm(files, desc="Embedding"):
        file_path = os.path.join(INPUT_DIR, filename)
        project_name = filename.replace(".txt", "")
        
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Получаем вектор
        vector = get_embedding(content, title=project_name)
        
        if vector:
            vector_store.append({
                "project_name": project_name,
                "content": content,
                "embedding": vector
            })
            
        # Небольшая пауза для стабильности API
        time.sleep(0.2)

    # Сохраняем всё в один JSON
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(vector_store, f, ensure_ascii=False, indent=4)

    print(f"\n✨ Готово! Векторная база сохранена в '{OUTPUT_FILE}'")

if __name__ == "__main__":
    main()