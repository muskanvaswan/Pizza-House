# Generated by Django 2.1.5 on 2020-06-07 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20200607_1913'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='status',
        ),
    ]