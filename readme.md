# Загрузка изображений из космоса
## Описание
Проект создан для загрузки изображений из космоса ,запуска космических кораблей и планеты "Земля".
# Установка
Скачайте необходимые файлы, затем используйте `pip` ( или `pip3`, если есть конфликт с Python2 ) для установки зависимостей и установить зависимости. Установите зависимости командой:
```
pip install -r requirements.txt
```
# Пример запуска скрипта
Для запуска у вас должен установлен Python3.
Для получений изображений с Nasa Apod надо написать:
```
python apod.py
```
Для получений изображений с Nasa epic надо написать:
```
python epic.py
```
Для получений изображений с Space X надо написать:
```
python spacex.py
```
Для загрузки изображений в  telegram надо написать:
```
python upload_images.py
```
# Переменые окружения
 Часть настроек проекта берется из переменных окружения. Чтоб определить переменые окружения необходимо создать файл `.env` рядом с `main.py` и запишите данные туда в таком формате: переменная = значение.
 Пример содержания файла `.env`:
 ```
 NASA_API_KEY = "nasa_token"
 TG_TOKEN = "bot_Token"
 TG_CHAT_ID = "@название вашего телеграмм канала"
 ```
 Получить токен NASA_API_KEY можно на сайте [NASA](https://www.nasa.gov/). Получить [TG_TOKEN](https://t.me/BotFather) у `отца ботов`
 # Цель проекта
 Проект был написан в образовательных целях
