# Generated by Django 4.1.5 on 2023-02-19 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_alter_news_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=300, null=True, verbose_name='Title'),
        ),
    ]
