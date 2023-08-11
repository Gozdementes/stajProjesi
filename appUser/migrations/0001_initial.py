# Generated by Django 4.2.2 on 2023-08-10 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=150, verbose_name='İsim Soyisim')),
                ('text', models.TextField(verbose_name='Yorum')),
                ('date_now', models.DateTimeField(auto_now_add=True, verbose_name='Tarih - Saat')),
            ],
        ),
    ]
