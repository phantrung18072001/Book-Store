# Generated by Django 3.2.8 on 2021-11-16 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0020_auto_20211116_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Chờ xử lý', 'Chờ xử lý'), ('Đang vận chuyển', 'Đang vận chuyển'), ('Đã hủy', 'Đã hủy'), ('Hoàn thành', 'Hoàn thành')], default='Chờ xử lý', max_length=100),
        ),
        migrations.AddIndex(
            model_name='book',
            index=models.Index(fields=['category'], name='store_book_categor_9ae749_idx'),
        ),
    ]
