# Generated by Django 4.2.6 on 2023-10-20 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectbox_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='boxproject',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
