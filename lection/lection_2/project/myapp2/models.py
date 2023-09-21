from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return f'name: {self.name}, email: {self.email}, age: {self.age}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    # Внимание! Для использования в моделях Django поля ImageField необходимо
    # установить дополнительный модуль Pillow. Выполните команду внутри виртуального окружения проекта:
    # pip install Pillow


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f'Name: {self.name}, email: {self.email}'


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'Title is {self.title}'

    def get_summary(self):
        words = self.content.split()
        return f'{" ".join(words[:7])}...'

# Для создания миграций для моделей Django используется команда "makemigrations". Например, чтобы создать
# миграции для моделей приложения myapp2, мы должны выполнить следующую команду:
# > python manage.py makemigrations myapp2

# Важно! Перед запуском команды убедитесь, что ваше приложение добавлено
# в список INSTALLED_APPS файла settings.py вашего проекта

# Применение миграций: После создания миграционного файла мы должны применить его к базе
# данных с помощью команды "migrate":
# > python manage.py migrate

# База данных при этом наполнится таблицами, включая пользователя, которого
# мы создали ранее. А если вы оставили модели товары и заказы при создании
# миграций, эти таблицы также будут созданы в БД
