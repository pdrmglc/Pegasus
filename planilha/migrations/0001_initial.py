# Generated by Django 4.2.1 on 2023-09-02 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planilha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arquivo', models.FileField(upload_to='planilhas/')),
                ('data_upload', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
