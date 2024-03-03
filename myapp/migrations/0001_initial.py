# Generated by Django 5.0.2 on 2024-02-27 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('side', models.CharField(choices=[('o', 'o'), ('r', 'r')], max_length=5)),
                ('game_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
