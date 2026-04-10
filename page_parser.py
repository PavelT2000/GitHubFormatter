import requests
from bs4 import BeautifulSoup

def get_vacancy_text(url):
    # Заголовки, чтобы сайт не принял нас за простого бота
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        # Загружаем страницу
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Проверка на ошибки (404, 500 и т.д.)
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Поиск блока по классам
        # Используем селектор, который ищет элемент с обоими классами
        target_classes = ["hht-vacancydescription", "hht-vacancydescription_adaptive"]
        description_div = soup.find("div", class_=lambda x: x and all(cls in x.split() for cls in target_classes))

        if description_div:
            # Извлекаем текст рекурсивно с разделением строк
            return description_div.get_text(separator='\n', strip=True)
        else:
            return "Блок с описанием не найден. Проверьте актуальность классов в HTML-коде."

    except requests.exceptions.RequestException as e:
        return f"Ошибка при загрузке страницы: {e}"

# Использование
