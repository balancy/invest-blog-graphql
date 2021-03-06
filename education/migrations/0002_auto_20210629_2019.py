# Generated by Django 3.2.4 on 2021-06-29 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='lesson',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='student',
        ),
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.ManyToManyField(to='education.Course'),
        ),
        migrations.DeleteModel(
            name='Lesson',
        ),
        migrations.DeleteModel(
            name='Schedule',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
