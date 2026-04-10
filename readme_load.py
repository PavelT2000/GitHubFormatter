from github import Github
import os


# Используй персональный токен доступа (PAT)
# Настройки -> Developer settings -> Personal access tokens
git_token = os.getenv("GITHUB_TOKEN")
g = Github(git_token)
user = g.get_user()

for repo in user.get_repos():
    try:
        # Пытаемся получить содержимое README
        readme = repo.get_readme()
        content = readme.decoded_content.decode('utf-8')
        
        # Сохраняем в файл или отправляем в обработку
        filename = f"readmes/{repo.name}_README.md"
        os.makedirs("readmes", exist_ok=True)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✅ Сохранен: {repo.name}")
        
    except Exception as e:
        print(f"❌ В {repo.name} нет README или произошла ошибка")