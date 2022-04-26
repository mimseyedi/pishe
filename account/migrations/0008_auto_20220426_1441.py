# Generated by Django 3.2.4 on 2022-04-26 14:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookstore', '0003_cart_product'),
        ('account', '0007_productfavorite_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productfavorite',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookstore.book', verbose_name='شناسه کتاب'),
        ),
        migrations.AlterField(
            model_name='productfavorite',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='شناسه کاربر'),
        ),
    ]
