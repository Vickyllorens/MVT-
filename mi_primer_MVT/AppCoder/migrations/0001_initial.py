# Generated by Django 4.1.1 on 2022-10-05 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familiares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('edad', models.IntegerField()),
                ('tipo', models.CharField(max_length=40)),
                ('profesion', models.CharField(max_length=40)),
            ],
        ),
    ]
