from django.urls import path

from . import views

app_name = 'roadmap'
urlpatterns = [
    path('', views.road_map, name='road_map'),
]