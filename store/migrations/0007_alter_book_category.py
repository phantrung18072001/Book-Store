# Generated by Django 3.2.8 on 2021-11-04 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20211104_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[('Triết Học', 'Triết Học'), ('Tôn Giáo', 'Tôn Giáo'), ('Ngôn Ngữ', 'Ngôn Ngữ'), ('Khoa Học Xã Hội', 'Khoa Học Xã Hội'), ('Khoa Học Tự Nhiên', 'Khoa Học Tự Nhiên'), ('Kỹ Thuật', 'Kỹ Thuật'), ('Nghệ Thuật', 'Nghệ Thuật'), ('Văn Học', 'Văn Học'), ('Địa Lý - Lịch Sử', 'Địa Lý - Lịch Sử')], max_length=100),
        ),
    ]
