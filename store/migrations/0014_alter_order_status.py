# Generated by Django 3.2.8 on 2021-11-10 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_auto_20211110_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Wait', 'Chờ xác nhận'), ('Sending', 'Đang vận chuyển'), ('Cancel', 'Đã hủy'), ('Completed', 'Hoàn thành')], default='Wait', max_length=100),
        ),
    ]
