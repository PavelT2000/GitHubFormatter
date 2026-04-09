import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import List
from table import Technology
# Импортируй свои модели из предыдущего шага
# from database_setup import Technology, Repository

def get_all_tech_names(db_path: str) -> List[str]:
    """Извлекает список всех уникальных технологий из БД."""
    engine = create_engine(f"sqlite:///{db_path}")
    Session = sessionmaker(bind=engine)
    session = Session()

    # Получаем плоский список названий
    techs = session.query(Technology.tech_name).all()
    session.close()

    return [t[0] for t in techs]

def match_techs_to_job(job_description: str, db_path: str = "resume_data.db") -> List[str]:
    """Сравнивает стек из БД с описанием вакансии через AI."""

    # 1. Получаем наш доступный стек
    available_techs = get_all_tech_names(db_path)

    if not available_techs:
        print("База технологий пуста.")
        return []

    # 2. Формируем промпт
    # Мы просим вернуть валидный JSON массив, чтобы было легко распарсить
    prompt = (
        f"JOB DESCRIPTION:\n{job_description}\n\n"
        f"AVAILABLE TECHNOLOGIES LIST:\n{', '.join(available_techs)}\n\n"
        "Task: Identify which technologies from the 'AVAILABLE TECHNOLOGIES LIST' are required or highly relevant "
        "to the 'JOB DESCRIPTION'. Include direct matches and obvious synonyms. "
        "Return ONLY a JSON array of strings. No explanations."
    )

    # 3. Запрос к AI
    # Используем твою функцию askai
    from ai_module2 import askai

    response = askai(
        prompt=prompt,
        system_message="You are a technical recruiter. Return ONLY a valid JSON list of strings.",
        temperature=0 # Минимум фантазии, максимум точности
    )

    if not response:
        return []

    try:
        # Чистим ответ от возможных артефактов (на случай если AI добавил ```json)
        clean_json = response.strip().replace("```json", "").replace("```", "").strip()
        matched_techs = json.loads(clean_json)
        return matched_techs
    except Exception as e:
        print(f"Ошибка парсинга ответа AI: {e}")
        return []

if __name__ == "__main__":
    # Пример использования
    vacansy_text = """
    Мы ищем Backend разработчика на .NET 8.
    Опыт работы с PostgreSQL и Docker обязателен.
    Будет плюсом знание Redis и понимание микросервисной архитектуры.
    """

    print("--- Анализ вакансии и подбор технологий ---")
    relevant_stack = match_techs_to_job(vacansy_text)

    if relevant_stack:
        print(f"Найденные совпадения в вашем стеке: {', '.join(relevant_stack)}")
    else:
        print("Совпадений не найдено.")