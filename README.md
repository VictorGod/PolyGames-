# README: PolyGames

## Описание проекта

PolyGames — это система для хранения, отображения и управления играми, разработанными студентами Московского Политехнического университета. Проект построен по микросервисной архитектуре, что обеспечивает гибкость в развертывании и масштабируемость. Основные компоненты системы включают интерфейс для взаимодействия с пользователем, сервисы для аутентификации и авторизации, обработки данных, а также сервис для кэширования.

## Архитектура системы

### Компоненты
Система включает следующие микросервисы:

1. **Frontend** — взаимодействует с пользователями, отправляет запросы для регистрации, авторизации и получения данных.
2. **Auth Service** — выполняет регистрацию, авторизацию пользователей и генерацию JWT-токенов.
3. **Backend Service** — отвечает за бизнес-логику и взаимодействует с кэшем и Data Service.
4. **Data Service** — управляет данными, обрабатывает CRUD операции в базе данных.
5. **Redis Service** — хранит часто запрашиваемые данные для ускорения доступа.

### Архитектура базы данных
Используется PostgreSQL с реляционной моделью, включающей следующие основные сущности:

- **Users** — хранит данные о пользователях, включая роли и профили.
- **Games** — информация об играх, таких как жанры и платформы.
- **Profiles** — профили пользователей, включающие достижения и участие в играх.
- **Reviews** — отзывы и оценки пользователей об играх.
### Описание базы данных PolyGames

1. **`users`** — хранит данные пользователей.
   - Поля: `id`, `username`, `email`, `hashed_password`, `role`, `created_at`.
   - Связи: один пользователь имеет один профиль (`profiles`), может создавать игры (`games`) и оставлять отзывы (`reviews`).

2. **`profiles`** — данные профилей пользователей.
   - Поля: `id`, `user_id`, `games_participated`, `achievements`, `bio`.
   - Связи: каждый профиль принадлежит одному пользователю.

3. **`games`** — информация об играх, созданных пользователями.
   - Поля: `id`, `title`, `description`, `genre`, `platform`, `download_link`, `jam_participant`, `jam_winner`, `creator_id`, `created_at`.
   - Связи: каждая игра создается одним пользователем и может иметь несколько отзывов.

4. **`reviews`** — отзывы пользователей об играх.
   - Поля: `id`, `user_id`, `game_id`, `rating`, `review_text`, `created_at`.
   - Связи: каждый отзыв связан с одним пользователем и одной игрой.

### Краткие связи между таблицами:
- **`users - profiles`**: один к одному.
- **`users - games`**: один ко многим.
- **`users - reviews`**: один ко многим.
- **`games - reviews`**: один ко многим. 


### Основные сценарии
1. **Регистрация**: Frontend отправляет запрос на Auth Service, который сохраняет данные пользователя.
2. **Авторизация**: Frontend отправляет запрос на авторизацию, Auth Service генерирует JWT-токен и возвращает его.
3. **Получение данных**: Frontend отправляет запрос на Backend Service с токеном. Backend проверяет кэш и, если данных нет, обращается к Data Service.

## Запуск проекта

Для запуска проекта доступны два подхода: через виртуальное окружение Python и с использованием Docker.

### Запуск через виртуальное окружение (venv)

1. Склонируйте проект:
    ```bash
    git clone [<URL_проекта>](https://github.com/VictorGod/PolyGames-.git)
    cd <папка_проекта>
    ```

2. Создайте виртуальное окружение и активируйте его:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # для Linux/Mac
    .\venv\Scripts\activate   # для Windows
    ```

3. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

4. Запустите сервер:
    ```bash
    python main.py
    ```

### Запуск через Docker

1. Склонируйте проект:
    ```bash
    git clone [<URL_проекта>](https://github.com/VictorGod/PolyGames-.git)
    cd <папка_проекта>
    ```

2. Соберите и запустите контейнеры:
    ```bash
    docker-compose up --build
    ```

3. Для остановки контейнеров:
    ```bash
    docker-compose down
    ```

## Работа с Git

### Основные команды для работы с Git

1. **Склонировать проект**:
    ```bash
    git clone [<URL_проекта>](https://github.com/VictorGod/PolyGames-.git)
    ```

2. **Создать новую ветку для разработки**:
    ```bash
    git checkout -b имя_ветки
    ```

3. **Добавить изменения**:
    ```bash
    git add .
    ```

4. **Закоммитить изменения**:
    ```bash
    git commit -m "Описание изменений"
    ```

5. **Отправить изменения в удалённый репозиторий**:
    ```bash
    git push origin имя_ветки
    ```

6. **Переключиться на другую ветку**:
    ```bash
    git checkout имя_ветки
    ```

7. **Слить изменения из другой ветки в текущую**:
    ```bash
    git merge имя_ветки
    ```

