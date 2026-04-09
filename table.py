import json
import os
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

# Настройки
DB_NAME = "resume_data.db"
INPUT_FILE = "technology_matrix.json"

Base = declarative_base()

# Связующая таблица для Many-to-Many
repo_technology_association = Table(
    'repo_technologies',
    Base.metadata,
    Column('repo_id', Integer, ForeignKey('repositories.id'), primary_key=True),
    Column('tech_id', Integer, ForeignKey('technologies.id'), primary_key=True)
)

class Repository(Base):
    __tablename__ = 'repositories'

    id = Column(Integer, primary_key=True)
    repo_url = Column(String, unique=True, nullable=False)
    repo_name = Column(String)

    # Связь с технологиями
    technologies = relationship(
        "Technology",
        secondary=repo_technology_association,
        back_populates="repositories"
    )

class Technology(Base):
    __tablename__ = 'technologies'

    id = Column(Integer, primary_key=True)
    tech_name = Column(String, unique=True, nullable=False)

    # Обратная связь
    repositories = relationship(
        "Repository",
        secondary=repo_technology_association,
        back_populates="technologies"
    )

# --- Логика миграции ---

def migrate():
    if not os.path.exists(INPUT_FILE):
        print(f"Ошибка: Файл {INPUT_FILE} не найден.")
        return

    # Подключение
    engine = create_engine(f"sqlite:///{DB_NAME}")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    print("Начинаю импорт данных через SQLAlchemy...")

    # Словари для кеширования объектов в памяти (чтобы не делать лишних запросов SELECT)
    tech_cache = {}
    repo_cache = {}

    try:
        for tech_name, urls in data.items():
            # Получаем или создаем объект технологии
            if tech_name not in tech_cache:
                tech = session.query(Technology).filter_by(tech_name=tech_name).first()
                if not tech:
                    tech = Technology(tech_name=tech_name)
                    session.add(tech)
                tech_cache[tech_name] = tech

            current_tech = tech_cache[tech_name]

            for url in urls:
                # Получаем или создаем объект репозитория
                if url not in repo_cache:
                    repo = session.query(Repository).filter_by(repo_url=url).first()
                    if not repo:
                        repo_name = url.split('/')[-1]
                        repo = Repository(repo_url=url, repo_name=repo_name)
                        session.add(repo)
                    repo_cache[url] = repo

                current_repo = repo_cache[url]

                # Создаем связь, если её еще нет
                if current_tech not in current_repo.technologies:
                    current_repo.technologies.append(current_tech)

        session.commit()
        print(f"Успех! База {DB_NAME} обновлена.")

    except Exception as e:
        session.rollback()
        print(f"Критическая ошибка: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    migrate()