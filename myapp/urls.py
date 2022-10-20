from django.urls import path
from . import views


urlpatterns = [
    path('home',views.home.as_view(),name="home"),
    path('list',views.list.as_view(),name="list"),
    path('delete/<int:eid>',views.delete.as_view(),name="delete"),
     path('admin',views.admin.as_view(),name="admin"),
    

]