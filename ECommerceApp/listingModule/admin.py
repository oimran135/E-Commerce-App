from django.contrib import admin
from .models import (ProductCategories, Products,
                    Users, UserWishList, UserOrders,
                    UserLogs, UserAddress)

admin.site.register(ProductCategories)
admin.site.register(Products)
admin.site.register(Users)
admin.site.register(UserWishList)
admin.site.register(UserOrders)
admin.site.register(UserLogs)
admin.site.register(UserAddress)
