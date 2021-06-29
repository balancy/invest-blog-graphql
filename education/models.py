from django.contrib.auth.models import User
from django.db import models
from tinymce.models import HTMLField


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

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"

    def __str__(self):
        return f"{self.__class__.__name__} <{self.user}>"


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


class Course(models.Model):
    responsible = models.ForeignKey(
        Mentor,
        on_delete=models.PROTECT,
        verbose_name="Отвественный",
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


class Lesson(models.Model):
    mentor = models.ForeignKey(
        Mentor,
        on_delete=models.PROTECT,
        verbose_name="Преподаватель",
        related_name="lessons",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Курс",
        related_name="lessons",
    )
    tags = models.ManyToManyField(
        "Tag",
        verbose_name="Тэг",
        related_name="lessons",
    )

    title = models.CharField(
        max_length=150,
        default="",
        verbose_name="Название",
    )
    description = HTMLField(
        default="",
        blank=True,
        verbose_name="Описание урока",
    )
    text = HTMLField(
        default="",
        blank=True,
        verbose_name="Текст занятия",
    )

    class Meta:
        verbose_name = "Занятие"
        verbose_name_plural = "Занятия"

    def __str__(self):
        return f"{self.__class__.__name__} <{self.title}>"


class TagQuerySet(models.QuerySet):
    def popular(self):
        return self.annotate(
            lessons_count=models.Count('lessons')
        ).order_by('-lessons_count')


class Tag(models.Model):
    title = models.CharField(
        max_length=150,
        default="",
        verbose_name="Название",
    )

    objects = TagQuerySet.as_manager()

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return f"{self.__class__.__name__} <{self.title}>"


class Schedule(models.Model):
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        verbose_name="Занятие",
        related_name="schedules",
    )

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        verbose_name="Студент",
        related_name="schedules",
    )

    lesson_time = models.DateTimeField(
        verbose_name="Дата занятия",
    )

    class Meta:
        verbose_name = "Расписание"
        verbose_name_plural = "Расписание"

    def __str__(self):
        return (f"{self.__class__.__name__} <{self.lesson}> <{self.student}> "
                f"at {self.lesson_time}")