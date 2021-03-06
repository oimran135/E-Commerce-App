# Generated by Django 4.0.2 on 2022-02-10 16:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import listingModule.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True)),
                ('contactNo', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to=listingModule.models.UserImages)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductCategories',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to=listingModule.models.CategoryImages)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=100)),
                ('price', models.FloatField(blank=True, null=True)),
                ('discount', models.FloatField(blank=True, null=True)),
                ('quantity', models.IntegerField(default=0)),
                ('sold_qt', models.IntegerField(default=0)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to=listingModule.models.ProductImages)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='listingModule.productcategories')),
            ],
        ),
        migrations.CreateModel(
            name='UserWishList',
            fields=[
                ('wishID', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('brand_name', models.CharField(blank=True, max_length=100, null=True)),
                ('productURL', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserOrders',
            fields=[
                ('orderID', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('paymentMethod', models.CharField(choices=[('Cash on Delivery', 'Cash on Delivery'), ('Credit/Debit Card', 'Credit/Debit Card')], max_length=100)),
                ('products', models.ManyToManyField(to='listingModule.Products')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserLogs',
            fields=[
                ('logID', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('LoginDateTime', models.DateTimeField(auto_now_add=True)),
                ('logoutDateTime', models.DateTimeField(auto_now=True, null=True)),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('houseID', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('address', models.TextField()),
                ('houseDescription', models.TextField(blank=True, null=True)),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='users',
            name='favourites',
            field=models.ManyToManyField(to='listingModule.Products'),
        ),
        migrations.AddField(
            model_name='users',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='users',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
