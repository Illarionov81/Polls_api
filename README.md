# Polls_api
### В проекте использованы:
    * Django-2.2.10 
    * DRF
    * Sqlite3
---------------------------------------------------------------
# Установка.
 1. Cклонировать проект с GitHub:
   * $ git clone git@github.com:Illarionov81/Polls_api.git
 2. Cоздайте виртуальное окружение:
   * ```$ cd Polls_api/```
   * ```Polls_api$ python3 -m venv venv```
 3. Активируйте его:
   * ```Polls_api$ . venv/bin/activate```
 4. Устанавите окружение:
   * ```(venv)Polls_api$ pip install -r requirements.txt```
 5. Проведите Мигрирацию БД:
   * ```Polls_api$ cd source/```
   * ```(venv)Polls_api/source$ python manage.py migrate```
 6. Запустить сервер:
   * ```./manage.py runserver```
 7. Загрузить дамп:  
   * ```Polls_api/source$ ./manage.py loaddata ../fixtures/auth.json ```
   ----------------------------------------------

 ## Endpoints:
  - получение списка активных опросов:  
    * http://localhost:8000/api/polls/
  - post запрос на создание ответа на вопрос:  
    * http://localhost:8000/api/answers/ 
    * json exampl - {
        "question": 4,
        "answer": "text",
        "user_id": 5528
    }
   - получение пройденных пользователем опросов с детализацией по ответам:  
    * http://localhost:8000/api/polls/5528/user_answers/ 
    
## Для администратора системы (с ограниченными правами):  
    - авторизация в системе:  
    * http://localhost:8000/admin/
    * Username: administrator
    * Password: polls-123
    
## superuser:  
    * http://localhost:8000/admin/
    * Username: admin
    * Password: admin
