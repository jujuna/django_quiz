# Generated by Django 3.1.4 on 2021-01-09 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_question_answer_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=models.CharField(default=None, max_length=100),
        ),
    ]