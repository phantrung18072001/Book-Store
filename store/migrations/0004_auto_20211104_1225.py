# Generated by Django 3.2.8 on 2021-11-04 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_book_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('0', 'Triết học'), ('1', 'Tôn giáo'), ('2', 'Ngôn ngữ'), ('3', 'Khoa học xã hội'), ('4', 'Khoa học tự nhiên'), ('5', 'Kỹ thuật'), ('6', 'Nghệ thuật'), ('7', 'Văn học'), ('8', 'Địa lý - lịch sử')], max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='book_image',
            old_name='book_id',
            new_name='book',
        ),
        migrations.RenameField(
            model_name='book_inventory',
            old_name='book_id',
            new_name='book',
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.book_category'),
        ),
    ]