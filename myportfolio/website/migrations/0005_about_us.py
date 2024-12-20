# Generated by Django 5.1.3 on 2024-11-27 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_profile_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='about_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_heading', models.CharField(max_length=100)),
                ('about_details', models.TextField()),
                ('my_resume', models.FileField(upload_to='static/')),
            ],
        ),
    ]
