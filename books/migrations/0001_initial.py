# Generated by Django 3.2.7 on 2021-09-09 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=1000)),
                ('read', models.BooleanField(default=False)),
            ],
        ),
    ]