from django.urls import path
import polls.views as views

urlpatterns = [
    path('', views.index, name='index'),
]