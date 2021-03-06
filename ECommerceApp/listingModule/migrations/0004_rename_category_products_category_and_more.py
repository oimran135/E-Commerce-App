# Generated by Django 4.0.2 on 2022-02-14 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listingModule', '0003_users_is_staff'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='category',
            new_name='Category',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='quantity',
            new_name='available_quantity',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='added_at',
            new_name='date_created',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='description',
            new_name='product_description',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='image',
            new_name='product_image',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='title',
            new_name='product_name',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='price',
            new_name='product_price',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='sold_qt',
            new_name='sold_quantity',
        ),
    ]
