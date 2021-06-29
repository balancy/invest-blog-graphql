from django.contrib.auth.models import User
from django.db import models
from tinymce.models import HTMLField



class Category(models.Model):
    title = models.CharField(
        max_length=150,
        default="",
        verbose_name="Название",
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f"{self.__class__.__name__} <{self.title}>"


class Mentor(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        verbose_name="Пользователь",
    )

    status = models.CharField(
        max_length=200,
        default="",
        blank=True,
        verbose_name="Статус",
    )

    bio = models.TextField(
        default="",
        blank=True,
        verbose_name="Биография",
    )

    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"

    def __str__(self):
        return f"{self.__class__.__name__} <{self.user}>"


class Course(models.Model):
    mentors = models.ManyToManyField(
        Mentor,
        blank=True,
        verbose_name="Преподаватели",
        related_name="courses",
    )
    
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Категория",
        related_name="courses",
    )

    title = models.CharField(
        max_length=150,
        default="",
        verbose_name="Название",
    )

    description = HTMLField(
        default="",
        blank=True,
        verbose_name="Описание курса",
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курс"

    def __str__(self):
        return f"{self.__class__.__name__} <{self.title}>"


class Student(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        verbose_name="Пользователь",
    )

    status = models.CharField(
        max_length=200,
        default="",
        blank=True,
        verbose_name="Статус",
    )

    bio = models.TextField(
        default="",
        blank=True,
        verbose_name="Биография",
    )

    courses = models.ManyToManyField(
        Course,
        blank=True,
        verbose_name="Курсы",
        related_name="students",
    )

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"

    def __str__(self):
        return f"{self.__class__.__name__} <{self.user}>"
