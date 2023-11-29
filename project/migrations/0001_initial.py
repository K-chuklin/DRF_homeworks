# Generated by Django 4.2.7 on 2023-11-29 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='название')),
                ('preview', models.ImageField(upload_to='project/', verbose_name='превью')),
                ('description', models.TextField(max_length='150', verbose_name='описание')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='название')),
                ('preview', models.ImageField(upload_to='project/', verbose_name='превью')),
                ('description', models.TextField(max_length='150', verbose_name='описание')),
                ('video', models.TextField(max_length=2048, verbose_name='')),
            ],
        ),
    ]
