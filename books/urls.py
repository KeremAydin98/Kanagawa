from django.urls import path
from .views import BookListView, BookDetailView, SearchResultsView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('new/', BookCreateView.as_view(), name='book_new'),
    path('<uuid:pk>', BookDetailView.as_view(), name='book_detail'),
    path('<uuid:pk>/update/', BookUpdateView.as_view(), name='book_update'),
    path('<uuid:pk>/update/delete/', BookDeleteView.as_view(), name='book_delete'),
    path('search/',SearchResultsView.as_view(), name='search_results'),
]