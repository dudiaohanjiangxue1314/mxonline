# Generated by Django 2.0.1 on 2018-08-02 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_course_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='tag',
            field=models.CharField(default='', max_length=15, verbose_name='课程标签'),
        ),
    ]
