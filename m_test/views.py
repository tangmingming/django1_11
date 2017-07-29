from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic import ListView, DetailView


from .models import Publisher, Author, Book


from .models import Book

# Create your views here.

class Index_3(TemplateView):
    template_name = "m_test/index_3.html"


class BookList(ListView):
    mode = Book

    def head(elf, *args, **kwargs):
        last_book = self.get_queryset().last("publication_date")
        response = HttpResponse('')
        response['Last-Modified'] = last_book.publication_date.strftime('%a, %d %b %Y %H:%M:%S GMT')

        return response

class Index_4(View):
    greeting = "Good Day"
    def get(self, request):
        return HttpResponse(self.greeting)

@method_decorator(login_required, name="dispatch")
class Index_5(Index_4):
    greeting = "Welcome"

    def dispatch(self, request, *args, **kwargs):
        return HttpResponse("Custom dispatch")


class PublisherList(ListView):
    model = Publisher
    context_object_name = "my_favorite_publishers"


class PublisherDetail(DetailView):
    model = Publisher

    def get_content_data(self, **kwargs):
        context = super(PublisherDetail, self).get_context_data(**kwargs)
        context["book_list"] = Book.objects.all()
        return context