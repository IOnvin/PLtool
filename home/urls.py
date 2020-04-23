from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('404/', views.errorpage, name='404'),
    path('base/', views.base, name='base'),
    path('add_quote/', views.add_quote, name='add_quote'),
    path('quote_list', views.AddQuoteListView.as_view(), name='quote_list'),
    path('<int:pk>/', views.AddQuoteDetailView.as_view(), name='quote_detail'),
]


