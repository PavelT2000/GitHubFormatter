import os
import requests
import logging
from typing import Optional

# Настройка локального логирования для модуля
logger = logging.getLogger(__name__)

def askai(
    prompt: str,
    system_message: str = "You are a professional IT assistant. Respond ONLY with the requested file content or code. No talk, no markdown blocks.",
    temperature: float = 0.1
) -> Optional[str]:
    """
    Отправляет запрос к собственному AI сервису.
    """
    url = os.getenv("AI_SERVICE_URL")
    if not url:
        logger.error("AI_SERVICE_URL не задан в переменных окружения (.env)")
        return None

    # Формируем тело запроса согласно твоей схеме
    payload = {
        "contents": [
            {
                "role": "user",
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ],
        "system_instruction": system_message,
        "temperature": temperature,
        "max_output_tokens": 2048,  # Увеличил лимит для длинных конфигов/кода
        "top_p": 0.95,
        "top_k": 40
    }

    try:
        logger.info(f"Отправка запроса на собственный сервис: {url}")

        response = requests.post(
            url,
            json=payload,
            timeout=90  # Даем запас времени для генерации больших структур
        )

        # Проверка на ошибки HTTP
        response.raise_for_status()

        data = response.json()

        try:
            # 1. Сначала проверяем твой формат (ключ 'answer')
            if 'answer' in data:
                return data['answer'].strip()

            # 2. Если нет 'answer', пробуем стандартный путь Gemini/Google
            ai_text = data['candidates'][0]['content']['parts'][0]['text']
            return ai_text.strip()

        except (KeyError, IndexError, TypeError) as parse_error:
            logger.error(f"Ошибка парсинга ответа: {parse_error}. Ответ: {data}")
            return None
    except requests.exceptions.RequestException as e:
        logger.error(f"Ошибка при обращении к AI сервису: {e}")
        return None
    except Exception as e:
        logger.error(f"Непредвиденная ошибка в модуле askai: {e}")
        return None

if __name__ == "__main__":
    # Быстрый тест модуля
    # os.environ["AI_SERVICE_URL"] = "твой_урл"
    res = askai("Напиши print hello на python")
    print(f"Результат теста: {res}")