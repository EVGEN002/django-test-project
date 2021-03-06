from django.shortcuts import render

# Create your views here.

from .models import Book, Author, BookInstance, Genre

def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact = 'a').count()
    num_authors = Author.objects.count()
    num_novel = Genre.objects.filter(name__icontains = 'Novel').count()
    num_sea = Book.objects.filter(title__icontains = "The Old Man and the Sea").count()

    return render(
        request,
        'index.html',
        context = {'num_books':num_books, 'num_instances':num_instances, 'num_instances_available':num_instances_available, 'num_authors':num_authors, 'novel': num_novel, 'num_sea': num_sea}
    )

from django.views import generic

class BookListView(generic.ListView):
    model = Book
    paginate_by = 10

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10

class AuthorDetailView(generic.DetailView):
    model = Author