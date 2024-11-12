# Сферум бот

## Использование

##  Качаем код и заполянем нужные данные

```
git clone git@gitlab.com:zergvip/sferum_bot.git
cd sferum_bot
```

В Файле startup.py задать id чата сферум и хеш куки пользователя ВК от которого будет рассылка. Для поулчения куки:

[Sferum](https://web.vk.me/) >> <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>C</kbd> >> Application >> Storage >> Cookies >> ```https://web.vk.me```
After that you must see **table** with all cookies from this site!
in filter put ```remixdsid``` and copy data from **value** column.

id чата берем просто из адресной строки барзера зайдя в чат.

В файле main.py Ввести текст вместо "Тестовое сообщение из бота"

## Настраиваем окружение

```
python3 -m venv ./venv
source ./venv/bin/activate
pip install -r requirements.txt
```

## Запускаем

```
python3 startup.py
```

## Лицензия

Используйте на здоровье

## Спасибка

Бот сделан на основе исходных кодов проекта https://github.com/xKARASb/SferumBot?tab=readme-ov-file
Огромное спасибо автору @xKARASb

