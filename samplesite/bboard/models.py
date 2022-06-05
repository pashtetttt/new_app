from django.db import models


# Create your models here.

class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Товар')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')

    # Связь один-ко-многим, бб - вторичное поле
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT,
                               verbose_name='Рубрика')

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published'] # Можно поставить несколько параметров в списке,
        # минус означает, что порядок сортировки будет обратным
        unique_together = ('title', 'published')

    # class Kinds(models.TextChoices):
    #     BUY = 'b', 'Куплю'
    #     SELL = 's', 'Продам'
    #     EXCHANGE = 'c', 'Обменяю'
    #     RENT = 'r'
    #     __empty__ = 'Выберите тип публикуемого объявления'
    #
    # kind = models.CharField(max_length=1, choices=Kinds.choices,default=Kinds.SELL)
    #


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True,
                            verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']
