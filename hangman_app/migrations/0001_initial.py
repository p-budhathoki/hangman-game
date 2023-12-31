# Generated by Django 4.1.11 on 2023-10-10 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HangmanGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=100)),
                ('guessed_letters', models.CharField(default='', max_length=100)),
                ('incorrect_guesses', models.IntegerField(default=0)),
                ('max_incorrect_guesses', models.IntegerField(default=0)),
                ('status', models.CharField(default='InProgress', max_length=20)),
            ],
        ),
    ]
