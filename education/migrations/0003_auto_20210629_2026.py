# Generated by Django 3.2.4 on 2021-06-29 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0002_auto_20210629_2019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='course',
        ),
        migrations.AddField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(blank=True, related_name='students', to='education.Course', verbose_name='Курсы'),
        ),
    ]
