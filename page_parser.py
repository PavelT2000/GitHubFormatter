import requests
from bs4 import BeautifulSoup

def get_vacancy_text(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        # 1. Используем CSS-селектор. Точки заменяют пробелы между классами.
        # Это найдет ВСЕ блоки, у которых есть полный набор этих классов.
        selector = ".bloko-column.bloko-column_xs-4.bloko-column_s-8.bloko-column_m-12.bloko-column_l-10"
        description_blocks = soup.select(selector)

        if description_blocks:
            # Собираем текст из всех найденных блоков в один список
            texts = [block.get_text(separator='\n', strip=True) for block in description_blocks]
            # Объединяем их двойным переносом строки для читаемости
            return "\n\n--- Следующий блок ---\n\n".join(texts)
        else:
            return "Блоки не найдены. Возможно, верстка изменилась или контент подгружается через JS."

    except requests.exceptions.RequestException as e:
        return f"Ошибка при загрузке страницы: {e}"

