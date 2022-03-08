from django.urls import path
from .views import HomeView, StudentCreateView, StudentListView, StudentUpdateView, StudentDeleteView

urlpatterns =[
    path('home/', HomeView.as_view(), name="home"),
    path('create/', StudentCreateView.as_view(), name="stu_create"),
    path('list/', StudentListView.as_view(), name="stu_list"),
    path('update/<int:pk>/', StudentUpdateView.as_view(), name="stu_update"),
    path('delete/<int:pk>/', StudentDeleteView.as_view(), name="stu_delete"),
]