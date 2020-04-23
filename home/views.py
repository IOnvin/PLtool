from django.shortcuts import render
from .forms import QuoteForm
from .models import AddQuote
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views import View
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)


def index(request):
    form = AddQuote.objects.all()[:10]

    context = {
        'form': form
    }
    return render(request, 'index.html', context)


def base(request):
    return render(request, 'base.html')


def errorpage(request):
    return render(request, '404.html')


def add_quote(request):
    form = QuoteForm(request.POST)
    if form.is_valid():
        # now the data is good
        form.save()
        form = QuoteForm()

    context = {
        'form': form
    }
    return render(request, 'add_quote.html', context)


class AddQuoteListView(View):
    template_name = 'quote_list.html'
    queryset = AddQuote.objects.all()

    '''def get_queryset(self):
        return self.queryset'''

    def get(self, request, *args, **kwargs):
        context = {'object_list': self.queryset}
        return render(request, self.template_name, context)


class AddQuoteDetailView(DetailView):
    template_name = 'quote_detail.html'
    queryset = AddQuote.objects.all()
