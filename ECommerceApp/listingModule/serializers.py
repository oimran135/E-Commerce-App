from rest_framework import serializers
from django.contrib import auth
from .models import ProductCategories, UserOrders, Users, Products, UserWishList
from rest_framework.exceptions import AuthenticationFailed

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length = 68, min_length= 6, write_only = True)

    class Meta:
        model = Users
        fields = ['email', 'username', 'password',]

    # def validate(self, attrs):
    #     email = attrs.get('email', '')
    #     username = attrs.get('username', '')

    def create(self, validated_data):
         return Users.objects.create_user(**validated_data)

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)
    username = serializers.CharField(
        max_length=255, min_length=3, read_only=True)

    class Meta:
        model = Users
        fields = ['email', 'password', 'username']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        user = auth.authenticate(email=email, password=password)

        if not user:
            raise AuthenticationFailed('The email or password is incorrect')

        return{
            'email':user.email,
            'username':user.username
        }

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Users
        fields = ['id', 'name', 'username', 'email', 'contactNo', 'image', 'gender']

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategories
        fields = ['title', 'image']

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Products
        fields = ['id', 'title', 'image', 'price', 'category', 'quantity', 
        'sold_qt', 'description', 'added_at', 'discount']

class WishListSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserWishList
        fields = ['user', 'title', 'brand_name', 'productURL']

    # def create(self, validated_data):
    #      return Use.objects.create(**validated_data)

class OrderSerializer(serializers.ModelSerializer):
    #products_data = ProductSerializer(write_only=True, many=True)

    class Meta:
        model = UserOrders
        fields = '__all__'

    # def create(self, validated_data):
    #     products_data = validated_data.pop('products', None)
    #     item = UserOrders.objects.create(**validated_data)
    #     products = []
    #     if products_data is not None:
    #         for product in products_data:
    #             product_id = product.pop('id', None)
    #             product_data, _ = Products.objects.get_or_create(id=product_id, defaults=product)
    #             products.append(product_data)
    #             item.products.add(*products)
    #     item.save()
    #     return item

class UserFavouritesSerializer(serializers.ModelSerializer):
    #products_data = ProductSerializer(write_only=True, many=True)
    class Meta:
        model = Users
        fields = ['name', 'favourites']

    # def create(self, validated_data):
    #     products_data = validated_data.pop('favourites', None)
    #     item = Users.objects.create(**validated_data)
    #     products = []
    #     if products_data is not None:
    #         for product in products_data:
    #             product_id = product.pop('id', None)
    #             product_data, _ = Products.objects.get_or_create(id=product_id, defaults=product)
    #             products.append(product_data)
    #             item.products.add(*products)
    #     item.save()
    #     return item
    