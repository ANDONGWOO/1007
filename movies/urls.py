from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.main, name='main'),
    path('index/', views.index, name='index'),
    path('create/', views.create, name='create'),
    # path('<int:pk>/', views.cerate, name=''),
    # path('<int:pk>/update/ ', views.cerate, name='update'),
]