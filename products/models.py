from django.db import models


class Product(models.Model):
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    title = models.TextField(verbose_name='Заголовок', max_length=100)
    description = models.TextField(verbose_name='Описание')
    images = models.ForeignKey('Image', verbose_name='Изображения', on_delete=models.CASCADE)
    category = models.ManyToManyField('Category', verbose_name='Категория')
    cost = models.FloatField(verbose_name='Стоимость')
    count = models.PositiveIntegerField(verbose_name='Количество')
    comments = models.ForeignKey('Comment', verbose_name='Комментарии', on_delete=models.CASCADE)


class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    title = models.TextField(verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')


class Image(models.Model):
    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    title = models.TextField(verbose_name='Заголовок', max_length=100)
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Изображение', upload_to='products/')
    number = models.PositiveSmallIntegerField(verbose_name='Порядок отображения')


class Comment(models.Model):
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    title = models.TextField(verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    #user = models.OneToOneField('User', verbose_name='Пользователь', null=True, on_delete=models.SET_NULL)
    approved = models.BooleanField(verbose_name='Одобрен', default=False, blank=False)
    #approved_by = models.OneToOneField('User', verbose_name='Кем одобрено', null=True, on_delete=models.SET_NULL)
    time_approved = models.DateTimeField(verbose_name='Когда одобрено', null=True)
