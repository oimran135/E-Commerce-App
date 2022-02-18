from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view()), #checked
    path('login/', views.LoginView.as_view()), #checked
    path('hot-products/', views.HotProductsView.as_view()), #checked #checked
    path('new-arrivals/', views.LatestProductsView.as_view()), #checked #checked
    path('categories/', views.CategoriesView.as_view()), #checked
    path('all-products/', views.AllProducts.as_view()), #checked
    path('promotions/', views.PromotionsView.as_view()), #checked
    path('order/place/', views.OrdersAPI.as_view()), #checked
    path('user/<int:pk>/order/checkout/', views.OrdersCheckout.as_view()), #checked
    path('wish-list/', views.WishListShow.as_view()), #checked
    path('wish-list/add-New/', views.WishListAdd.as_view()), #checked
    path('user/<int:pk>', views.UserProfileView.as_view()), #checked
    path('user/<int:pk>/update/', views.UserPartialUpdateView.as_view()), #checked
    path('user/<int:pk>/favourites/', views.FavouritesAPI.as_view()), #checked
]