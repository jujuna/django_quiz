# Generated by Django 3.1.4 on 2021-01-09 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210109_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]