from django.db import models
from django.conf import settings

# Create your models here.


class CourseApply(models.Model):  # создаем отдельную таблицу
    name = models.CharField(max_length=50)
    email = models.EmailField(null=True)
    package = models.CharField(max_length=10, choices=(
        ('standart', 'Standart'), ('gold', 'Gold'), ('vip', 'Vip')),
        default='gold')
    news_subscribe = models.BooleanField()
    comment = models.TextField()
    is_active = models.BooleanField(default=True)
    date_apply = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Position(models.Model):  # создаем отдельную таблицу
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Coursename(models.Model):  # создаем отдельную таблицу
    name = models.CharField(verbose_name=u'Course', max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Course'


class Instructor(models.Model):  # имя таблицы
    name = models.CharField(verbose_name=u'Instructor name', max_length=255, help_text='This is name')  # поля таблицы (столбцы)
    surname = models.CharField(max_length=64)
    data_of_birth = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True, null=True)
    
    #course = models.CharField(max_length=255, null=True)
    #course = models.ForeignKey(Coursename)
    courses = models.ManyToManyField(Coursename)
    is_active = models.BooleanField(default=True)
    
    position = models.ForeignKey(Position)

    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True)

    # position = models.CharField(max_length=1, choices=(('i', 'Instructor'), ('a', 'Assistent')))

    def __str__(self):
        return (self.name + ' ' + self.surname)

    '''
    phone = models.CharField(max_length=15, null=True, blank=True)
    slug = models.SlugField(unique=True)
    gender = models.CharField(max_length=1, choices=(('m', 'Male'), ('f', 'Female')))
    '''

'''
CharField
EmailField
SlugField

DateField
DateTimeField
TimeField

BooleanField
IntegerField
DecimalField
FloatField

FileField
ImageField

TextField
'''
