from django.urls import path
from todo import views

urlpatterns = [
    path('', views.home),
    path('delete/<str:pk>', views.del_item),
    path('edit/<str:pk>', views.edit_item)
]
