# Generated by Django 3.0.5 on 2020-04-16 09:47

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('mydiary', '0002_comment'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='comment',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
