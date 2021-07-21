from locallibrary.catalog.models import Author
from django.urls import path
from django.urls.conf import re_path
from . import views
from django.conf.urls import url

urlpatterns = [
    re_path(r'^$', views.index, name="index"),
    re_path(r'^books/$', views.BookListView.as_view(), name="books"),
    re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name="book-detail"),
    re_path(r'^authors/$', views.AuthorListView.as_view(), name="authors"),
    re_path(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name="author-detail"),
]