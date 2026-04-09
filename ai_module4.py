import os
import requests
import logging
import openai
from typing import Optional, Any, Dict, List

# Настройка логирования
logger = logging.getLogger(__name__)

# Твой список приоритетных бесплатных моделей
BASE_MODELS = [
    "qwen/qwen3.6-plus:free",
    "z-ai/glm-4.5-air:free",
    "minimax/minimax-m2.5:free",
    "stepfun/step-3.5-flash:free",
    "nvidia/nemotron-3-super-120b-a12b:free",
    "arcee-ai/trinity-large-preview:free",
    "nvidia/nemotron-3-nano-30b-a3b:free",
    "arcee-ai/trinity-mini:free",
    "nvidia/nemotron-nano-12b-v2-vl:free",
    "minimax/minimax-m2.5:free",
    "nvidia/nemotron-nano-9b-v2:free",
    "nvidia/llama-nemotron-embed-vl-1b-v2:free",
    "openai/gpt-oss-120b:free"
]

def get_optimized_models() -> List[str]:
    """Проверяет доступность моделей через API OpenRouter и возвращает топ-3."""
    try:
        response = requests.get("https://openrouter.ai/api/v1/models", timeout=10)
        if response.status_code == 200:
            data = response.json().get('data', [])
            online_ids = {m['id'] for m in data}
            available_models = [m for m in BASE_MODELS if m in online_ids]
            if available_models:
                return available_models[:3]
        return BASE_MODELS[:3]
    except Exception as e:
        logger.warning(f"Не удалось обновить список моделей: {e}. Используем базовый список.")
        return BASE_MODELS[:3]

def askai(
    prompt: str,
    system_message: str = "You are a professional IT assistant.",
    temperature: float = 0.1,
    tools: Optional[List[Dict[str, Any]]] = None,
    max_tokens: int = 4096
) -> str:
    """
    Отправляет запрос к OpenRouter.
    Принцип: 'Падаем, не терпим' — если что-то идет не так, кидаем исключение.
    """
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise EnvironmentError("OPENROUTER_API_KEY не найден в переменных окружения!")

    # Инициализация клиента OpenAI (совместим с OpenRouter)
    client = openai.OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    models = get_optimized_models()
    model_string = ",".join(models)

    logger.info(f"Запрос к OpenRouter (модели: {model_string})...")

    try:
        response = client.chat.completions.create(
            model=model_string,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
            max_tokens=max_tokens,
            extra_headers={
                "HTTP-Referer": "https://github.com/your-repo", # Обязательно для OpenRouter
                "X-Title": "Github Formatter Project",
            },
            timeout=120
        )

        result = response.choices[0].message.content

        if not result or not result.strip():
            raise ValueError("AI вернул пустой ответ!")

        logger.info(f"Успех! Использована модель: {response.model}")
        return result.strip()

    except Exception as e:
        logger.error(f"Критическая ошибка OpenRouter: {e}")
        # Принцип 'Падаем': пробрасываем ошибку выше, чтобы readme_gen.py остановился
        raise RuntimeError(f"Сбой генерации через OpenRouter: {e}") from e

if __name__ == "__main__":
    # Быстрый тест
    # os.environ["OPENROUTER_API_KEY"] = "твой_ключ"
    try:
        print(askai("Привет! Напиши кратко: 'Тест пройден'"))
    except Exception as e:
        print(f"Тест провален: {e}")