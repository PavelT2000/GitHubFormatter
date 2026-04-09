import os
import logging
from typing import Optional, Any, Dict, List, cast
from huggingface_hub import InferenceClient

# Импортируем типы для Pylance
from huggingface_hub.inference._generated.types.chat_completion import (
    ChatCompletionOutput,
    ChatCompletionInputTool
)

logger = logging.getLogger(__name__)

BASE_MODELS = [
    "Qwen/Qwen2.5-72B-Instruct",
    "meta-llama/Llama-3.1-8B-Instruct"
]

def askai(
    prompt: str,
    system_message: str = "You are a professional IT assistant.",
    temperature: float = 0.1,
    tools: Optional[List[Dict[str, Any]]] = None,
    max_tokens: int = 4096
) -> str:
    api_key = os.getenv("HF_TOKEN")
    if not api_key:
        raise EnvironmentError("HF_TOKEN не найден!")

    client = InferenceClient(token=api_key)

    for model_id in BASE_MODELS:
        try:
            messages = [
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt}
            ]

            # 1. Приводим tools к типу, который ожидает библиотека
            # 2. Используем cast, чтобы Pylance видел в response ChatCompletionOutput, а не Union
            response = cast(
                ChatCompletionOutput,
                client.chat_completion(
                    model=model_id,
                    messages=messages,
                    max_tokens=max_tokens,
                    temperature=temperature,
                    tools=cast(Optional[List[ChatCompletionInputTool]], tools),
                    tool_choice="auto" if tools else None,
                    stream=False # Явно указываем False, чтобы сработала нужная перегрузка
                )
            )

            message = response.choices[0].message

            if message.tool_calls:
                return str(message.tool_calls[0].function.arguments)

            result = message.content
            if result and isinstance(result, str):
                return result.strip()

            continue

        except Exception as e:
            logger.warning(f"Модель {model_id} ошибка: {e}")
            continue

    raise RuntimeError("Все модели не смогли обработать запрос.")