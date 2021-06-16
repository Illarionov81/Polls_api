# Polls_api
### В проекте использованы:
    * Django-2.2.10 
    * DRF
    * Sqlite3
---------------------------------------------------------------
# Установка.
 1. Cклонировать проект с GitHub:
 2. * $ git clone git@github.com:Illarionov81/Polls_api.git
 3. Cоздайте виртуальное окружение:
   * ```$ cd Polls_api/```
   * ```Polls_api$ python3 -m venv venv```
 4. Активируйте его:
   * ```Polls_api$ . venv/bin/activate```
 5. Устанавите окружение:
   * ```(venv)Polls_api$ pip install -r requirements.txt```
 6. Проведите Мигрирацию БД:
   * ```Polls_api$ cd source/```
   * ```(venv)Polls_api/source$ python manage.py migrate```
 7. Запустить сервер:
   * ```./manage.py runserver```
 8. Загрузить дамп:  
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
