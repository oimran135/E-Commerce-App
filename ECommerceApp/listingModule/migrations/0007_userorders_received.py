# Generated by Django 4.0.2 on 2022-02-21 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listingModule', '0006_rename_houseid_useraddress_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userorders',
            name='received',
            field=models.BooleanField(default=False),
        ),
    ]
