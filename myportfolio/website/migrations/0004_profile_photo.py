# Generated by Django 5.1.3 on 2024-11-27 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_social_media'),
    ]

    operations = [
        migrations.CreateModel(
            name='profile_photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ImageField(upload_to='static/')),
            ],
        ),
    ]
