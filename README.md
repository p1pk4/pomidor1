# pomidor1
https://www.youtube.com/watch?v=FHeAm-JAJ98&list=PLyaCd9XYVI9ACOnDvyto01CH6dx35PG-t

Настройка проекта.
  django-admin createproject project
  manage.py startapp ***
    settings.py: INSTALLED_APPS = [orders, products, accounts]
   urls.py: router
   
Создание моделей:
  models.py: Создание классов(моделей) с наследованием
  
View models:
  render and serializers
  
Urls:
  routers and path:
    Exm: path('', orders_page) - первая страница которая ссылается на view.py в котором функция def orders_page возвращает рендер файла index.html

SQLite.
  Паттерн Active Record:
    Модели как-будто оборачивают таблицы и поля предоставляя к ним достпус с помощью Python и Django
    
Миграции:
  manage.py makemigrations
  manage.py migrate
