# Generated by Django 2.1.2 on 2019-03-11 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clipping', '0004_book_asin'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_clipping',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='是否删除'),
        ),
    ]
