# Generated by Django 5.1.3 on 2024-11-28 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_education'),
    ]

    operations = [
        migrations.CreateModel(
            name='my_skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('html', models.FileField(upload_to='static/')),
                ('css', models.FileField(upload_to='static/')),
                ('js', models.FileField(upload_to='static/')),
                ('bootstrap', models.FileField(upload_to='static/')),
                ('python', models.FileField(upload_to='static/')),
                ('django', models.FileField(upload_to='static/')),
            ],
        ),
    ]
