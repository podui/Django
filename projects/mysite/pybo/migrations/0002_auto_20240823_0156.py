# Generated by Django 3.1.3 on 2024-08-22 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='creat_date',
            new_name='create_date',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='creat_date',
            new_name='create_date',
        ),
    ]
