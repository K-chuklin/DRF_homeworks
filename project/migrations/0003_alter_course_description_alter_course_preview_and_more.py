# Generated by Django 4.2.7 on 2023-11-29 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_alter_subject_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(blank=True, max_length='150', null=True, verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='course',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to='project/', verbose_name='превью'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='description',
            field=models.TextField(blank=True, max_length='150', null=True, verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to='project/', verbose_name='превью'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='video',
            field=models.TextField(blank=True, max_length=2048, null=True, verbose_name='ссылка_на_видео'),
        ),
    ]
