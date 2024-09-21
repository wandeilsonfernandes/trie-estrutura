# trieapp/urls.py

from django.urls import path
from .views import TrieView

urlpatterns = [
    path('trie/', TrieView.as_view(), name='trie'),
]
