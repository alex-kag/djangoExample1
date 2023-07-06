from django.urls import path
from . import views

urlpatterns = [
    path('hello_world/', views.hello, name='hello1'),
    path('', views.root, name='hello1'),
    path('about/', views.about, name='hello1'),
    path('items/', views.items, name = 'hello1'),
    path('item/<int:number>/', views.item, name = 'hello1'),
]
