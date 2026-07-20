from django.contrib import admin
from django.urls import path
from restaurants.views import restaurant_list
from orders.views import order_list_create
from accounts_api.views import login_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/restaurants/', restaurant_list),
    path('api/orders/', order_list_create),
    path('api/login/', login_view),
    # JWT AUTH
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


