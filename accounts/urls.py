from django.urls import path
from . import views
from . import api

app_name = 'accounts'

urlpatterns = [
    path('signup',views.signup , name='signup'),
    path('profile',views.profile , name='profile'),
    path('profile/edit',views.profile_edit , name='profile_edit'),
    
    
    path('api/profile/<int:pk>',api.ProfileDetailView.as_view() , name='profile_api'),
    path('api/profile/<int:pk>/edit',api.ProfileEditView.as_view() , name='profile_edit_api'),
]
