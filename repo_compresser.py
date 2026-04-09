import os
import json
import tiktoken
from ai_module5 import askai
# Импортируем вашу функцию askai из вашего модуля
# from your_module import askai

# Папки для работы
CACHE_DIR = "compression_cache"
INPUT_FILE = "extracted_resume_data.json"
FINAL_OUTPUT = "compressed_resume.json"

def count_tokens(text: str, model: str = "gpt-4") -> int:
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        encoding = tiktoken.get_encoding("cl100k_base")
    return len(encoding.encode(text))

def ai_compress_project(project: dict) -> dict:
    """Просит ИИ переписать данные проекта максимально сжато."""
    prompt = (
        f"Rewrite this project data to be as concise as possible for a CV. "
        f"Keep technical keywords, but shorten sentences. "
        f"Output MUST be a valid JSON with the same keys.\n\n"
        f"DATA:\n{json.dumps(project, ensure_ascii=False)}"
    )

    system_msg = "You are a CV expert. Minimize text while keeping 100% of technical value. Return only JSON."

    try:
        response = askai(prompt, system_message=system_msg, temperature=0)
        # Очистка от markdown если есть
        clean_json = response.strip().replace("```json", "").replace("```", "").strip()
        return json.loads(clean_json)
    except Exception as e:
        print(f"Ошибка сжатия {project.get('project_name')}: {e}")
        return project # Возвращаем оригинал при сбое

def process_smart_compression():
    if not os.path.exists(CACHE_DIR):
        os.makedirs(CACHE_DIR)

    # 1. Загрузка исходных данных
    if not os.path.exists(INPUT_FILE):
        print(f"Файл {INPUT_FILE} не найден!")
        return

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        projects = json.load(f)

    limit = int(input("Введите целевой лимит токенов для всего набора: ") or "2000")

    compressed_list = []

    # 2. Обработка каждого проекта с сохранением прогресса
    print("=== Начало интеллектуального сжатия ===")
    for i, p in enumerate(projects):
        p_name = p.get('project_name', f'project_{i}')
        cache_path = os.path.join(CACHE_DIR, f"{p_name}.json")

        if os.path.exists(cache_path):
            with open(cache_path, "r", encoding="utf-8") as f:
                compressed_p = json.load(f)
            print(f"[{i+1}/{len(projects)}] {p_name} загружен из кеша")
        else:
            print(f"[{i+1}/{len(projects)}] Сжимаем {p_name} через ИИ...")
            compressed_p = ai_compress_project(p)
            with open(cache_path, "w", encoding="utf-8") as f:
                json.dump(compressed_p, f, ensure_ascii=False, indent=2)

        compressed_list.append(compressed_p)

    # 3. Финальная проверка лимита
    current_json = json.dumps(compressed_list, ensure_ascii=False)
    current_tokens = count_tokens(current_json)
    print(f"--- Текущий размер: {current_tokens} токенов ---")

    # Если всё еще не влезает, применяем жесткое отсечение (по количеству)
    if current_tokens > limit:
        print("Лимит превышен. Удаляем наименее объемные/важные проекты...")
        while current_tokens > limit and compressed_list:
            compressed_list.pop()
            current_json = json.dumps(compressed_list, ensure_ascii=False)
            current_tokens = count_tokens(current_json)

    # 4. Сохранение результата
    with open(FINAL_OUTPUT, "w", encoding="utf-8") as f:
        json.dump(compressed_list, f, ensure_ascii=False, indent=2)

    print(f"=== ГОТОВО! Итоговый размер: {current_tokens} токенов. Файл: {FINAL_OUTPUT} ===")

if __name__ == "__main__":
    process_smart_compression()