# Generated by Django 3.2.8 on 2021-11-03 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_account_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='image',
            field=models.ImageField(blank=True, default='avatar-default.png', null=True, upload_to=''),
        ),
    ]
