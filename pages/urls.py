from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pages/', views.post_list, name='post_list'),
    path('pages/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('pages/crear/', views.PostCreateView.as_view(), name='post_create'),
    path('pages/<int:pk>/editar/', views.post_edit, name='post_edit'),
    path('pages/<int:pk>/borrar/', views.post_delete, name='post_delete'),
]
