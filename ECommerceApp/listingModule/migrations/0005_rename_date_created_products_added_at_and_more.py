# Generated by Django 4.0.2 on 2022-02-14 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listingModule', '0004_rename_category_products_category_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='date_created',
            new_name='added_at',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='Category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='product_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='product_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='product_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='available_quantity',
            new_name='quantity',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='sold_quantity',
            new_name='sold_qt',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='product_name',
            new_name='title',
        ),
    ]
