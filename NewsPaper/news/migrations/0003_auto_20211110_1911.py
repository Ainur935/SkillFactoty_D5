# Generated by Django 3.2.9 on 2021-11-10 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_author_rating_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='one_to_one_relation',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='author',
            name='rating_user',
            field=models.IntegerField(default=0),
        ),
    ]
