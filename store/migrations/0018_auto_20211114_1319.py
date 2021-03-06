# Generated by Django 3.2.8 on 2021-11-14 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_auto_20211113_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book', to='store.book'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='cart_session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to='store.cart'),
        ),
    ]
