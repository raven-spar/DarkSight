# Generated by Django 5.0.6 on 2024-05-18 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='leakeddb',
            fields=[
                ('email', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('pwd', models.CharField(max_length=200)),
            ],
        ),
    ]
