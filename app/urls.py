from django.urls import path
from .views import *

urlpatterns = [
    
    path('snippets/', SnippetListCreateAPIView.as_view(), name='snippet-list'),
    path('snippets/<int:pk>/', SnippetRetrieveUpdateDestroyAPIView.as_view(), name='snippet-detail'),
    path('tags/',TagListAPIView.as_view(), name='tag-list'),
    path('tags/<int:pk>/',TagRetrieveAPIView.as_view(), name='tag-detail'),
]