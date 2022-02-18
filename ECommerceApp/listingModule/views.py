from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Users, UserOrders, Products, ProductCategories, UserWishList
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser, JSONParser
from .serializers import (RegisterSerializer, LoginSerializer,
                         OrderSerializer, UserSerializer, WishListSerializer,
                         ProductSerializer, CategorySerializer, UserFavouritesSerializer)

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
        type(request)
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

    parser_classes = [JSONParser, MultiPartParser, FormParser, FileUploadParser]

    def get(self, request, pk=None):
        queryset = Users.objects.get(pk=pk)
        serializer = UserSerializer(queryset)
        return Response(serializer.data)

class UserPartialUpdateView(generics.GenericAPIView):

    parser_classes = [JSONParser, MultiPartParser, FormParser, JSONParser]

    def get_queryset(request, pk=None):
        queryset = Users.objects.get(pk=pk)
        return queryset

    def put(self, request, pk=None):
        queryset = Users.objects.get(pk=pk)
        serializer = UserSerializer(instance=queryset, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = serializer.data
        return Response({"data":data, "success":True, "message":"user updated successfully"}, status=status.HTTP_200_OK)

class WishListAdd(generics.GenericAPIView):
    
    def post(self, request):
        serialized = WishListSerializer(data = request.data)
        print(serialized)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

class WishListShow(generics.GenericAPIView):

    def get_queryset(self, request):
        queryset = UserWishList.objects.all()
        return queryset
    
    def get(self, request):
        queryset = self.get_queryset(queryset)
        serializer = WishListSerializer(queryset, many=True)
        return Response(serializer.data)

class FavouritesAPI(generics.GenericAPIView):
    
    parser_classes = [JSONParser, MultiPartParser, FormParser, FileUploadParser]

    def get(self, request, pk=None):
        queryset = Users.objects.get(pk=pk)
        serialized = UserFavouritesSerializer(queryset)
        serialized_fav = serialized.data['favourites']
        new_list = []
        for id in serialized_fav:
            queryset1 = Products.objects.get(pk = id)
            serialized1 = ProductSerializer(queryset1)
            new_list.append(serialized1.data)
        return Response({'User':serialized.data['name'], 'favourites':new_list}, status=status.HTTP_200_OK)

class OrdersAPI(generics.GenericAPIView):
    
    def post(self, request):
        serialized = OrderSerializer(data = request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

class OrdersCheckout(generics.GenericAPIView):
    
    def get(selfrequest, pk=None):
        order = UserOrders.objects.get(pk = pk)
        serialized = OrderSerializer(order)
        data = serialized.data
        return Response({"data":data, "success":True, "message":"data found"}, status=status.HTTP_200_OK)
