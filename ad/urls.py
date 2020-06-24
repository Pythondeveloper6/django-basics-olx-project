from django. urls import  path
from . import views


app_name='ad'

urlpatterns = [
    path('',views.all_ads ,name='all_ads'),
    path('<int:id>',views.single_ad ,name='single_ad'),
    path('add',views.add_ad ,name='add_add'),
    path('categories',views.all_categories ,name='all_ads'),
    path('categories/<int:id>',views.category_ads ,name='category_ads'),
]
