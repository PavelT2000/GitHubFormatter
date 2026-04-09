import openai
import requests
import os
from typing import Optional, List

# Список ID моделей, которые нам интересны
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
    """Гарантированно возвращает не более 3 моделей."""
    try:
        response = requests.get("https://openrouter.ai/api/v1/models", timeout=5)
        if response.status_code == 200:
            data = response.json().get('data', [])
            online_ids = {m['id'] for m in data}
            available_models = [m for m in BASE_MODELS if m in online_ids]
            if available_models:
                return available_models[:3]
        return BASE_MODELS[:3]
    except Exception:
        return BASE_MODELS[:3]

def askai(
    prompt: str,
    system_message: str = "You are a professional IT assistant. Respond ONLY with the requested file content or code. No talk, no markdown blocks.",
    temperature: float = 0.1
) -> Optional[str]:
    """
    Отправляет запрос к ИИ с настраиваемыми параметрами.
    :param prompt: Основной текст запроса.
    :param system_message: Инструкция, определяющая роль и правила ответа.
    :param temperature: Степень креативности (0.0 - строго, 1.0 - хаос).
    """
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        print("Error: OPENROUTER_API_KEY is not set.")
        return None

    client = openai.OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    models = get_optimized_models()

    try:
        print(f"Sending request to models: {', '.join(models)}...")

        response = client.chat.completions.create(
            model=",".join(models),
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
            timeout=60
        )

        print(f"Success! Model used: {response.model}")
        return response.choices[0].message.content

    except Exception as e:
        print(f"Critical error: {e}")
        return None
