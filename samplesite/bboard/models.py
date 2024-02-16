from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
# Выводит ошибку, когда она связана не с полем, а с целой моделью
from django.core.exceptions import NON_FIELD_ERRORS

# Модель объявлений
class Bb(models.Model):
    title = models.CharField(max_length = 50, verbose_name = "Товар")
    content = models.TextField(blank = True, null = True, verbose_name = "Описание")
    price = models.FloatField(null = True, blank = True, verbose_name = "Цена")
    published = models.DateTimeField(auto_now_add = True, db_index = True)

    rubric = models.ForeignKey('Rubric', null = True, on_delete = models.PROTECT, verbose_name = 'Рубрика')

# Описываю, как будет вести себя форма при ошибках ввода
    def clean(self):
        errors = {}
        
        if not self.content:
            errors['content'] = ValidationError('Укажите описание продаваемого товара')

        if self.price and self.price < 0:
            errors['price'] = ValidationError("Укажите неотрицательное значение цены")

        if errors:
            raise ValidationError(errors)
        
        errors[NON_FIELD_ERRORS] = ValidationError('Ошибка в модели!')
        
# Дополнительные параметры модели
    class Meta:
        verbose_name_plural = "Объявления"
        verbose_name = "Обьявление"
        ordering = ['-published']

    def clean(self):
        errors = {}
        if not self.content:
            errors['content'] = ValidationError("Укажите описание продаваемого товара")

class Rubric(models.Model):
    name = models.CharField(max_length = 20, db_index = True, verbose_name = 'Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Рубрики"
        verbose_name = "Рубрика"
        ordering = ['name']

class AdvUser(models.Model):
    is_activated = models.BooleanField(default = True)
    user = models.OneToOneField(User, on_delete = models.CASCADE, verbose_name = "Пользователи")

    class Meta:
        verbose_name_plural = "Пользователи"
        verbose_name = "Пользователь"

    def __str__(self):
        return str(self.user)
    
