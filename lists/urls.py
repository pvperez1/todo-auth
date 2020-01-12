from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:item_id>/', views.delete, name='delete'),
    path('cross_off/<int:item_id>/', views.cross_off, name='cross_off'),
    path('uncross/<int:item_id>/', views.uncross, name='uncross'),
    path('edit/<int:item_id>/', views.edit, name="edit")
]
