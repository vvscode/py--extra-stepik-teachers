# Поиск учителей+

[Начало здесь](https://github.com/vvscode/py--stepik-teachers)

[Diff здесь](https://github.com/vvscode/py--extra-stepik-teachers/pull/1)

## Глава 4 – проектное задание

Никаких макетов в этот раз. Внешний вид проекта останется без изменений.

Но легко не будет. Впереди переход от файлов к БД и от стандартный форм к WTF Forms

### 1. Создайте модель Преподаватель

- Установите и подключите SQLAlchemy
- Опишите модель для преподавателя
- Проверьте, что первичный ключ, типы и констрейнты в порядке
  – upd: сохраните расписание в виде простой json-строки, при выводе превращайте строку в словарь

Обратите внимание: подход с JSON-строкой хорош, если по данным не нужно будет искать. Если данные нужно будет редактировать или фильтровать, предпочтительнее хранить каждое время как запись в отдельной таблице.

### 2. Создайте модель Бронирование

- Опишите модель Бронирование
  – Свяжите модель отношениями с Преподавателем (one to many)
- Проверьте, что первичный ключ, типы и констрейнты в порядке

### 3. Создайте модель Заявка на подбор

- Опишите модель
- Проверьте, что первичный ключ, типы и констрейнты в порядке

### 4. Импортируйте данные

- Напишите скрипт, который запишет мок-данные из JSON в базу
- Запишите данные
- Проверьте, что все заимпортировалось
- Выкиньте файл, он вам больше не понадобится

### 5. Доработайте роут преподавателя

- Замените получение данных из файла на выполнение запроса в БД
  – Когда преподавателя не существует, выбросьте 404

### 6. Доработайте роут цели, например, "для переезда"

– получите преподавателей с помощью запроса с фильтром и сортировкой

### 7. Доработайте роут главной

- Замените получение данных из файла на выполнение запроса в БД

### 8. Доработайте роут и страницу бронирования с обратной связью

– Перепишите форму с помощью WFT Forms
– Валидируйте форму: все поля должны быть заполнены
– Замените запись в файла на запись в базу

### 9. Доработайте роут и страницу заявки на подбор

– Перепишите форму с помощью WFT Forms
– Валидируйте форму: все поля должны быть заполнены
– Замените запись в файла на запись в базу
