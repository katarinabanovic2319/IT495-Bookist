from django.conf.urls import url
from django.urls import path, reverse

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('book/new/', views.book_new, name='book-new'),
    path('book/<int:pk>/edit/', views.book_edit, name='book-edit'),
    path('author/new/', views.author_new, name='author-new'),
    path('author/<int:pk>/edit/', views.author_edit, name='author-edit'),
    path('book/<int:pk>/comment/', views.BookCommentCreate.as_view(), name='book-comment'),
    path('lists/', views.ListListView.as_view(), name='lists'),
    path('list/<int:pk>', views.ListDetailView.as_view(), name='list-detail'),
    path('list/new/', views.list_new, name='list-new'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('book/<int:pk>/review/', views.BookReviewCreate.as_view(), name='book-review'),
    path('review/<int:pk>/update/', views.BookReviewUpdate.as_view(), name='review-update'),
    path('people/', views.all_friends, name='people'),
    url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', views.change_friends, name='change_friends'),
    path('alllists/', views.all_lists, name='all_lists')

]