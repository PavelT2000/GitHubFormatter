import json
import os
import numpy as np
from page_parser import get_vacancy_text
import requests
from dotenv import load_dotenv

load_dotenv()

class ProjectMatcher:
    def __init__(self, vector_store_path="vector_store.json"):
        self.ai_url = str(os.getenv("AI_SERVICE_URL"))
        self.embed_url = str(os.getenv("EMBED_SERIVCE_URL"))
        self.vector_store_path = vector_store_path
        self.projects = self._load_store()

    def _load_store(self):
        if not os.path.exists(self.vector_store_path):
            raise FileNotFoundError(f"Сначала создай базу векторов: {self.vector_store_path}")
        with open(self.vector_store_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def _squeeze_job(self, raw_text):
        """Очищает текст вакансии от HR-шума через ИИ"""
        system_instruction = (
            "Ты — технический рекрутер. Извлеки из текста вакансии только: "
            "стек технологий, требования к архитектуре и ключевые задачи. "
            "Удали описание компании, бенефиты и софт-скиллы. Пиши кратко."
        )
        payload = {
            "contents": [{"role": "user", "parts": [{"text": raw_text}]}],
            "system_instruction": system_instruction,
            "temperature": 0.2
        }
        try:
            response = requests.post(self.ai_url, json=payload, timeout=30)
            return response.json().get("answer", raw_text)
        except:
            return raw_text # Если ИИ упал, используем сырой текст

    def _get_embedding(self, text):
        """Получает вектор для текста"""
        payload = {
            "text": text,
            "task_type": "RETRIEVAL_QUERY"
        }
        response = requests.post(self.embed_url, json=payload, timeout=30)
        return response.json().get("embedding")

    @staticmethod
    def _cosine_similarity(v1, v2):
        v1, v2 = np.array(v1), np.array(v2)
        return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

    def find_top_projects(self, job_description, top_k=3):
        """Основная функция: сжимает, векторизует и сравнивает"""
        print("🧹 Очистка вакансии...")
        clean_job = self._squeeze_job(job_description)

        print("🧬 Векторизация требований...")
        job_vector = self._get_embedding(clean_job)

        if not job_vector:
            return []

        print("📊 Расчет сходства...")
        results = []
        for project in self.projects:
            score = self._cosine_similarity(job_vector, project["embedding"])
            results.append({
                "name": project["project_name"],
                "score": score,
                "summary": project["content"]
            })

        # Сортировка по убыванию
        results.sort(key=lambda x: x["score"], reverse=True)
        return results[:top_k]

# Пример использования:
if __name__ == "__main__":
    matcher = ProjectMatcher()

    url="https://rabota.by/vacancy/131987206?query=C%2B%2B&hhtmFrom=vacancy_search_list"
    text=get_vacancy_text(url=url)
    top_projects = matcher.find_top_projects(text,5)

    for p in top_projects:
        print(f"\n[Score: {p['score']:.4f}] Проект: {p['name']}")
        print(f"Суть: {p['summary'][:150]}...")