# Generated by Django 3.1.7 on 2021-03-13 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Categoria', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='codigo',
        ),
        migrations.AlterField(
            model_name='categoria',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
