from django.conf.urls import url
from django.urls import path
from .views import SignUpView
from . import views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('user/<int:pk>', views.UserDetailView.as_view(), name='user-profile'),
    path('user/<int:pk>/update/', views.UserProfileUpdate.as_view(), name='profile-update'),
    path('profile/', views.profile, name='profile'),
    path('profile/<int:pk>/', views.profile, name='profile-withpk'),
]
