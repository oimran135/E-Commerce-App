from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Users, UserOrders, Products, ProductCategories, UserWishList
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser, JSONParser
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import (ProfileViewSerializer, RegisterSerializer, LoginSerializer,
                         OrderSerializer, UserSerializer, WishListSerializer, OrderHistorySerializer,
                         ProductSerializer, CategorySerializer, UserFavouritesSerializer)
#from ECommerceApp.listingModule import serializers

class RegisterView(generics.GenericAPIView):
    
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(generics.GenericAPIView):
    
    def post(self, request):
        serialized = LoginSerializer(data = request.data)
        serialized.is_valid(raise_exception= True)
        return Response(serialized.data, status=status.HTTP_200_OK)

class AllProducts(generics.GenericAPIView):
        
    parser_classes = [JSONParser, MultiPartParser, FormParser, FileUploadParser]

    def get_queryset(self, request):
        queryset = Products.objects.all()
        return queryset

    def get(self, request):
        queryset = self.get_queryset(request)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

class Product(generics.GenericAPIView):

    def get(self, request, pk=None):
        queryset = Products.objects.get(pk=pk)
        serializer = ProductSerializer(queryset)
        return Response(serializer.data)


class CategoriesView(generics.GenericAPIView):
    
    parser_classes = [JSONParser, MultiPartParser, FormParser, FileUploadParser]

    def get_queryset(self, request):
        queryset = ProductCategories.objects.all()
        return queryset

    def get(self, request):
        queryset = self.get_queryset(request)
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

class PromotionsView(generics.GenericAPIView):
    
    parser_classes = [JSONParser, MultiPartParser, FormParser, FileUploadParser]

    def get_queryset(request):
        queryset = Products.objects.all().order_by('-discount')[:5]
        return queryset

    def get(self, request):
        queryset = PromotionsView.get_queryset(request)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

class HotProductsView(generics.GenericAPIView):
    
    parser_classes = [JSONParser, MultiPartParser, FormParser, FileUploadParser]

    def get_queryset(request):
        queryset = Products.objects.all().order_by('-sold_qt')[:10]
        return queryset

    def get(self, request):
        queryset = HotProductsView.get_queryset(request)
        serializer = ProductSerializer(queryset, many=True)
        data = serializer.data
        return Response(serializer.data, status=status.HTTP_200_OK)
       
class LatestProductsView(generics.GenericAPIView):
    
    parser_classes = [JSONParser, MultiPartParser, FormParser, FileUploadParser]

    def get_queryset(request):
        queryset = Products.objects.all().order_by('-added_at')[:10]
        return queryset

    def get(self, request):
        queryset = LatestProductsView.get_queryset(request)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

class UserProfileView(generics.GenericAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [JSONParser, MultiPartParser, FormParser, FileUploadParser]

    
    def get(self, request):
        user_id = request.user.id
        queryset = Users.objects.get(pk=user_id)
        serializer = ProfileViewSerializer(queryset)
        return Response(serializer.data)

# class NewPasswordView(generics.GenericAPIView):
        
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self, request):
#         queryset = self.request.id
#         return queryset

#     def put(self, request):
#         self.queryset = self.get_object()
#         serializer = self.get_serializer(data=request.data)
        
#         if serializer.is_valid():
#             if not self.object.check_password(serializer.data.get("old_password")):
#                 return Response({"current_password":"Your current password is wrong"}, status=status.HTTP_400_BAD_REQUEST)
#             self.object.set_password(serializer.data.get("new_password"))
#             self.object.save
#             return Response({"Password":"Password updated Successfully"}, status=status.HTTP_200_OK)


class UserPartialUpdateView(generics.GenericAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [JSONParser, MultiPartParser, FormParser, JSONParser]

    # def get_queryset(request, pk=None):
    #     queryset = Users.objects.get(pk=pk)
    #     return queryset

    def put(self, request):
        user_id = request.user.id
        queryset = Users.objects.get(pk=user_id)
        serializer = ProfileViewSerializer(instance=queryset, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = serializer.data
        return Response(serializer.data, status=status.HTTP_200_OK)

class WishListAdd(generics.GenericAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        request.data['user'] = request.user.id
        serialized = WishListSerializer(data = request.data)
        if serialized.is_valid():
            serialized.save()
            print(serialized.data)
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

class WishListShow(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [JSONParser, MultiPartParser, FormParser, JSONParser]
    
    def get(self, request):
        user_id = request.user.id
        queryset = UserWishList.objects.all().filter(user=user_id)
        serializer = WishListSerializer(queryset, many=True)
        return Response(serializer.data)

class FavouritesAPI(generics.GenericAPIView):
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [JSONParser, MultiPartParser, FormParser, FileUploadParser]

    def post(self, request, pk=None):
        user_id = request.user.id
        product = Products.objects.get(pk=pk)


    def get(self, request):
        user_id = request.user.id
        queryset = Users.objects.get(pk=user_id)
        print(queryset)
        serialized = UserFavouritesSerializer(queryset)
        return Response(serialized.data, status=status.HTTP_200_OK)

class OrdersAPI(generics.GenericAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.data['user'] = request.user.id
        serialized = OrderSerializer(data = request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

class OrdersView(generics.GenericAPIView):
    
    def get(self, request):
        user_id= request.user.id
        queryset = UserOrders.objects.all().filter(user = user_id)
        serializer = OrderHistorySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
