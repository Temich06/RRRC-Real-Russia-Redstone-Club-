from django.urls import path
from article import views

urlpatterns = [
    path('items/', views.ItemList.as_view()),
    path('item/<int:pk>/', views.ItemDetail.as_view()),
]
