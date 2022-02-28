from django.urls import path, include, re_path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('get-token/', TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify-token/', TokenVerifyView.as_view(),name='token_verify'),
    path('register/', views.RegisterView.as_view()), #checked #not registering to database from frontend
    path('login/', views.LoginView.as_view()), #checked
    path('hot-products/', views.HotProductsView.as_view()), #checked
    path('product/<int:pk>/', views.Product.as_view()),
    path('new-arrivals/', views.LatestProductsView.as_view()), #checked
    path('categories/', views.CategoriesView.as_view()), #checked
    path('all-products/', views.AllProducts.as_view()), #checked
    path('promotions/', views.PromotionsView.as_view()), #checked
    path('checkout/', views.OrdersAPI.as_view()),
    path('orders/', views.OrdersView.as_view()),
    #path('user/<int:pk>/order/checkout/', views.OrdersCheckout.as_view()), 
    path('wish-list/', views.WishListShow.as_view()), 
    path('make-request/', views.WishListAdd.as_view()), 
    path('user/', views.UserProfileView.as_view()), #checked
    path('user/update/', views.UserPartialUpdateView.as_view()), #checked
    path('favourites/', views.FavouritesAPI.as_view()), #checked
    #path('update/password/', views.NewPasswordView.as_view()),
    path('products', views.ProductQueryView.as_view()),
]