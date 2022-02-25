from rest_framework import serializers
from django.contrib import auth
from .models import ProductCategories, UserOrders, Users, Products, UserWishList
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

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

    tokens = serializers.SerializerMethodField()
    def get_tokens(self, obj):
        user = Users.objects.get(email=obj['email'])
        return user.tokens()['access']

    class Meta:
        model = Users
        fields = ['id', 'email', 'password', 'username', "tokens"]

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        user = auth.authenticate(email=email, password=password)

        if not user:
            raise AuthenticationFailed('The email or password is incorrect')

        return{
            'id':user.id,
            'email':user.email,
            'username':user.username,
            'tokens':user.tokens
        }

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Users
        fields = ['name', 'username', 'email', 'contactNo', 'image', 'gender', 'tokens']

class ProfileViewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Users
        fields = ['name', 'username', 'email', 'contactNo', 'image', 'gender']

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategories
        fields = ['title', 'image']

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Products
        fields = ['id', 'title', 'image', 'price', 'category', 'quantity', 
        'sold_qt', 'description', 'added_at', 'discount', 'img']

class WishListSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserWishList
        fields = ['user','title', 'brand_name', 'productURL']

class RequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserWishList,
        fields = ["user", "title", "brand_name", "productURL"]

    # def create(self, validated_data):
    #      return Use.objects.create(**validated_data)

class OrderSerializer(serializers.ModelSerializer):
    #products_data = ProductSerializer(write_only=True, many=True)

    class Meta:
        model = UserOrders
        fields = ['user', 'products', 'paymentMethod']


class UserFavouritesSerializer(serializers.ModelSerializer):
    #products_data = ProductSerializer(write_only=True, many=True)
    class Meta:
        model = Users
        fields = ['name', 'favourites']
        depth = 1