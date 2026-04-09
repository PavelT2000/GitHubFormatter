import os
import requests
import logging
from typing import Optional, Any, Dict, List

logger = logging.getLogger(__name__)

def askai(
    prompt: str,
    system_message: str = "You are a professional IT assistant.",
    temperature: float = 0.1,
    tools: Optional[List[Dict[str, Any]]] = None,
    max_tokens: int = 4096
) -> str: # Убрали Optional, теперь возвращаем только str или падаем
    url = os.getenv("AI_SERVICE_URL")
    if not url:
        raise EnvironmentError("AI_SERVICE_URL не задан в .env")

    payload = {
        "contents": [
            {
                "role": "user",
                "parts": [{"text": prompt}]
            }
        ],
        "system_instruction": system_message,
        "temperature": temperature,
        "max_output_tokens": max_tokens,
        "top_p": 0.95,
        "top_k": 40
    }

    if tools:
        payload["tools"] = tools

    logger.info(f"Запрос к AI (len: {len(prompt)})...")

    response = requests.post(url, json=payload, timeout=120)
    response.raise_for_status() # Падаем при 4xx/5xx

    data = response.json()

    # Извлекаем текст (поддержка разных форматов твоего прокси)
    try:
        if 'answer' in data:
            result = data['answer'].strip()
        else:
            result = data['candidates'][0]['content']['parts'][0]['text'].strip()

        if not result:
            raise ValueError("AI вернул пустой текст")
        return result

    except (KeyError, IndexError, TypeError) as e:
        logger.error(f"Ошибка парсинга. Ответ сервера: {data}")
        raise RuntimeError(f"Не удалось разобрать ответ AI: {e}")