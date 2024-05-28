from lists import views
from django.urls import path, re_path

urlpatterns = [
    path('new', views.new_list, name='new_list'),
    re_path(r'^(\d+)/$',views.view_list, name='view_list'),
    re_path(r'^(\d+)/add_item$', views.add_item, name='add_item'),
]


# from lists import views as list_views
# from lists import urls as list_urls
# from django.urls import path, re_path, include

# urlpatterns = [
#     path('', list_views.home_page, name='home'),
#     path('lists/', include(list_urls)),
# ]
