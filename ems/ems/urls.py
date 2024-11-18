from django.contrib import admin
from django.urls import path, include
from employees.views import (
    home_view,
    login_view,
    register_view,
    profile_view,
    employee_list_view,
    employee_detail_view
)
from rest_framework.routers import DefaultRouter
from employees.views import EmployeeViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required  # Import login_required

# DRF router setup for API endpoints
router = DefaultRouter()
router.register(r'employees', EmployeeViewSet, basename='employee')

urlpatterns = [
    path('', home_view, name='home'),  # Home page URL
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # API CRUD routes for employees
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT token obtain
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # JWT token refresh

    # Template-based views for frontend
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('profile/', profile_view, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout view

    # Password change views, require user to be logged in
    path('password_change/', login_required(auth_views.PasswordChangeView.as_view()), name='password_change'),
    path('password_change/done/', login_required(auth_views.PasswordChangeDoneView.as_view()), name='password_change_done'),

    path('employees/', employee_list_view, name='employee_list'),
    path('employees/<int:id>/', employee_detail_view, name='employee_detail'),
]
