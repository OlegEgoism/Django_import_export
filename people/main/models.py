from django.db import models


class People(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=20, unique=True)
    age = models.IntegerField(verbose_name='Возраст')
    email = models.EmailField(verbose_name='Электронная почта', blank=True, null=True)
    city = models.ForeignKey('City', verbose_name='Город', related_name='peoples', on_delete=models.CASCADE, blank=True,
                             null=True)
    job = models.ForeignKey('Job', verbose_name='Работа', related_name='peoples', on_delete=models.CASCADE, blank=True,
                            null=True)

    class Meta:
        verbose_name = 'Информация о человеке'
        verbose_name_plural = 'ИНФОРМАЦИЯ О ЧЕЛОВЕКЕ'

    def __str__(self):
        return f'{self.name} - {self.age} года'


class City(models.Model):
    name = models.CharField(verbose_name='Название города', max_length=40, unique=True)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'ГОРОДА'

    def __str__(self):
        return self.name

    def count_people(self):
        return self.peoples.count()

    count_people.short_description = 'Количество людей'


class Job(models.Model):
    name = models.CharField(verbose_name='Название работы', max_length=100, unique=True)

    class Meta:
        verbose_name = 'Место работы'
        verbose_name_plural = 'МЕСТО РАБОТЫ'

    def __str__(self):
        return self.name

    def count_people(self):
        return self.peoples.count()

    count_people.short_description = 'Количество людей'
