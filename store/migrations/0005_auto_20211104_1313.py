# Generated by Django 3.2.8 on 2021-11-04 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20211104_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[('0', 'Triết học'), ('1', 'Tôn giáo'), ('2', 'Ngôn ngữ'), ('3', 'Khoa học xã hội'), ('4', 'Khoa học tự nhiên'), ('5', 'Kỹ thuật'), ('6', 'Nghệ thuật'), ('7', 'Văn học'), ('8', 'Địa lý - lịch sử')], max_length=100),
        ),
        migrations.DeleteModel(
            name='Book_Category',
        ),
    ]
