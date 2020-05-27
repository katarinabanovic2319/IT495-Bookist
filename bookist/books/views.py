from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.http import HttpResponseNotFound, HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic import CreateView, DetailView, UpdateView, TemplateView

from .models import Book, BookAuthor, BookComment, BookList, BookReview, Friend
from .forms import BookForm, BookAuthorForm, ListForm
from django.db.models import Q, Avg

def index(request):
    num_books = Book.objects.all().count()
    num_authors = BookAuthor.objects.all().count()
    avg_score = BookReview.objects.all().aggregate(Avg('review_score'))
    all_users = get_user_model().objects.all()

    context = {
        'num_books': num_books,
        'num_authors': num_authors,
        'avg_score': avg_score,
        'all_users': all_users,
    }

    # Render html template index.html with data in the context variable
    return render(request, 'index.html', context=context)

@login_required(login_url='login')
def all_friends(request):
    all_users = get_user_model().objects.exclude(id=request.user.id).exclude(id=1)
    friend = Friend.objects.get(current_user=request.user)
    friends = friend.users.all()

    context = {
        'all_users': all_users,
        'friends': friends,
    }

    # Render html template index.html with data in the context variable
    return render(request, 'books/people.html', context=context)

def books_in_list(request):
    all_books = BookList.objects.all().count()

    context = {
        'all_books': all_books
    }

    return render(request, 'books/list_detail.html', context=context)

@login_required(login_url='login')
def all_lists(request):
    all_lists = BookList.objects.all()

    context = {
        'all_lists': all_lists
    }

    return render(request, 'books/all_lists.html', context=context)

class BookListView(generic.ListView):
    model = Book
    template_name = 'books/book_list.html'
    paginate_by = 10


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'books/book_detail.html'

    def review_num(request):
        q = BookReview.objects.all()

        context = {
            'q': q,
        }

        return render(request, 'book_detail.html', context=context)


class AuthorListView(generic.ListView):
    model = BookAuthor
    template_name = 'books/author_list.html'
    paginate_by = 10


class AuthorDetailView(generic.DetailView):
    model = BookAuthor
    template_name = 'books/author_detail.html'

    def get_context_data(self, **kwargs):
        context = super(AuthorDetailView, self).get_context_data(**kwargs)
        context['book'] = get_object_or_404(Book, pk=self.kwargs['pk'])
        return context


@login_required(login_url='login')
def book_new(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            form.save_m2m()
            return redirect('book-detail', pk=book.pk)
    else:
        form = BookForm()
    return render(request, 'books/book_edit.html', {'form': form})


@login_required(login_url='login')
def book_edit(request, pk):
    post = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=post)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            form.save_m2m()
            return redirect('book-detail', pk=book.pk)
    else:
        form = BookForm(instance=post)
    return render(request, 'books/book_edit.html', {'form': form})


@login_required(login_url='login')
def author_new(request):
    if request.method == "POST":
        form = BookAuthorForm(request.POST)
        if form.is_valid():
            bookauthor = form.save(commit=False)
            bookauthor.save()
            return redirect('author-detail', pk=bookauthor.pk)
    else:
        form = BookAuthorForm()
    return render(request, 'books/author_edit.html', {'form': form})


@login_required(login_url='login')
def author_edit(request, pk):
    post = get_object_or_404(BookAuthor, pk=pk)
    if request.method == "POST":
        form = BookAuthorForm(request.POST, instance=post)
        if form.is_valid():
            bookauthor = form.save(commit=False)
            bookauthor.save()
            return redirect('author-detail', pk=bookauthor.pk)
    else:
        form = BookAuthorForm(instance=post)
    return render(request, 'books/author_edit.html', {'form': form})


class BookCommentCreate(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = BookComment
    fields = ['comment_text']

    def get_context_data(self, **kwargs):
        context = super(BookCommentCreate, self).get_context_data(**kwargs)
        context['book'] = get_object_or_404(Book, pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.instance.comment_author = self.request.user
        form.instance.comment_book = get_object_or_404(Book, pk=self.kwargs['pk'])
        return super(BookCommentCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('book-detail', kwargs={'pk': self.kwargs['pk'], })


class ListListView(LoginRequiredMixin, generic.ListView):
    login_url = 'login'
    model = BookList
    template_name = 'books/list_list.html'
    paginate_by = 10


class ListDetailView(LoginRequiredMixin, generic.DetailView):
    login_url = 'login'
    model = BookList
    template_name = 'books/list_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ListDetailView, self).get_context_data(**kwargs)
        context['book'] = get_object_or_404(Book, pk=self.kwargs['pk'])
        return context

@login_required(login_url='login')
def list_new(request):
    if request.method == "POST":
        form = ListForm(request.POST)
        if form.is_valid():
            booklist = form.save(commit=False)
            booklist.list_author = request.user
            booklist.save()
            form.save_m2m()
            return redirect('list-detail', pk=booklist.pk)
    else:
        form = ListForm()
    return render(request, 'books/list_edit.html', {'form': form})



class SearchResultsView(generic.ListView):
    model = Book
    template_name = 'books/search_results.html'

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        object_list = Book.objects.filter(Q(book_title__icontains=query))
        return object_list



class BookReviewCreate(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = BookReview
    fields = ['review_score']

    def get_context_data(self, **kwargs):
        context = super(BookReviewCreate, self).get_context_data(**kwargs)
        context['book'] = get_object_or_404(Book, pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        try:
            form.instance.review_user = self.request.user
            form.instance.review_book = get_object_or_404(Book, pk=self.kwargs['pk'])
            return super(BookReviewCreate, self).form_valid(form)
        except IntegrityError:
            return HttpResponse("You can not enter more than one review.")

    def get_success_url(self):
        return reverse('book-detail', kwargs={'pk': self.kwargs['pk'], })


class BookReviewUpdate(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = BookReview
    fields = ['review_score']


class UserProfileDetail(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'books/user_profile.html'


@login_required(login_url='login')
def change_friends(request, operation, pk):
    friend = get_user_model().objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, friend)
    elif operation == 'remove':
        Friend.lose_friend(request.user, friend)
    return redirect('people')