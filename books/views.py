from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Book
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.db.models import Q


class BookListView(LoginRequiredMixin, ListView):

    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'
    login_url = 'account_login'


class BookDetailView(LoginRequiredMixin, DetailView):

    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
    login_url = 'account_login'
    #permission_required = 'books.special_status'


class BookCreateView(LoginRequiredMixin, CreateView):

    model = Book
    context_object_name = 'book'
    template_name = 'books/book_new.html'
    login_url = 'account_login'
    fields = ('title','author','price','cover',)


class BookUpdateView(LoginRequiredMixin, UpdateView):

    model = Book
    context_object_name = 'book'
    template_name = 'books/book_update.html'
    login_url = 'account_login'
    fields = ('title','author','price','cover',)


class BookDeleteView(LoginRequiredMixin, DeleteView):

    model = Book
    template_name = 'books/book_delete.html'
    login_url = 'account_login'
    success_url = reverse_lazy('home')



class SearchResultsView(ListView):

    model = Book
    context_object_name = 'book_list'
    template_name = 'books/search_results.html'

    def get_queryset(self):

        query = self.request.GET.get("q")

        return Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))


