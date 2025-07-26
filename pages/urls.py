from django.urls import path
from .views import PageDeleteView, delete_comment
from .views import toggle_like
from .views import PageListView, PageDetailView, PageCreateView, PageUpdateView, PageDeleteView

urlpatterns = [
    path('', PageListView.as_view(), name='page_list'),
    path('<int:pk>/', PageDetailView.as_view(), name='page_detail'),
    path('crear/', PageCreateView.as_view(), name='page_create'),
    path('<int:pk>/editar/', PageUpdateView.as_view(), name='page_update'),
    path('<int:pk>/eliminar/', PageDeleteView.as_view(), name='page_delete'),
    path('comentario/<int:pk>/eliminar/', delete_comment, name='delete_comment'),
    path('pages/<int:pk>/like/', toggle_like, name='toggle_like'),
]
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required   