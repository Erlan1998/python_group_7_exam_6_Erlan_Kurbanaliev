# Generated by Django 3.1.7 on 2021-03-06 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0012_auto_20210306_0726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='date_creat',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
