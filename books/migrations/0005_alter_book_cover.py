# Generated by Django 4.0.3 on 2022-04-28 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_book_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='covers/'),
        ),
    ]