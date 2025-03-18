from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', views.welcome, name='welcome'),
    path('register/', views.user_register, name='user_register'),
    path('create/', views.create_user, name='create_user'),
    path('list/', views.list_users, name='list_users'),
    path('get/<int:user_id>/', views.get_user, name='get_user'),
    path('update/<int:user_id>/', views.update_user, name='update_user'),
    path('delete/<int:user_id>/', views.delete_user, name='delete_user'),
]


