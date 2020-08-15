from django. urls import  path
from . import views
from . import api

app_name='ad'

urlpatterns = [
    path('',views.all_ads ,name='all_ads'),
    path('<int:id>',views.single_ad ,name='single_ad'),
    path('<int:id>/like',views.like_ad ,name='like_ad'),
    path('add',views.add_ad ,name='add_add'),
    path('categories',views.all_categories ,name='all_ads'),
    path('categories/<int:id>',views.category_ads ,name='category_ads'),


    path('api',api.api_ad_list ,name='api_ad_list'),
    path('api/<int:id>',api.api_ad_detail ,name='api_ad_list'),

    path('api/v2',api.AdListView.as_view() ,name='api_ad_list'),
    path('api/v2/<int:pk>',api.AdDetailView.as_view() ,name='api_ad_list'),
    path('api/v2/category',api.CategoryListView.as_view() ,name='api_category_list'),
    path('api/v2/category/<int:pk>/ads',api.CategoryAdsListView.as_view() ,name='api_category_ads_list'),
]
