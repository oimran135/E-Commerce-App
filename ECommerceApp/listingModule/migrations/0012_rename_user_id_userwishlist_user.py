# Generated by Django 4.0.2 on 2022-02-24 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listingModule', '0011_rename_userid_userwishlist_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userwishlist',
            old_name='user_id',
            new_name='user',
        ),
    ]
