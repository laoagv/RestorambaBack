# Generated by Django 4.1.1 on 2024-05-30 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('randfoof', '0003_restaurent_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurent',
            name='picture',
            field=models.ImageField(default='None', max_length=500, upload_to=''),
        ),
    ]