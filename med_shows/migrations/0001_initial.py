# Generated by Django 4.1.1 on 2022-10-03 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalShows',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('img', models.ImageField(upload_to='C:\\Users\\Kalyibek\\PycharmProjects\\INAI\\atabek\\media')),
                ('img_type', models.CharField(choices=[('HEART', 'HEART'), ('KIDNEYS', 'KIDNEYS'), ('LIVER', 'LIVER'), ('EYES', 'EYES')], max_length=100)),
                ('add_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]