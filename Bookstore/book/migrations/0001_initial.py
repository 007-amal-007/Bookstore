# Generated by Django 3.2.7 on 2021-10-21 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=120, unique=True)),
                ('author', models.CharField(max_length=50)),
                ('price', models.PositiveIntegerField(default=20)),
                ('copies', models.PositiveIntegerField(default=1)),
                ('image', models.ImageField(null=True, upload_to='images')),
            ],
        ),
    ]
