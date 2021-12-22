from django.db.models import query
from django.urls import reverse_lazy
from django.shortcuts  import redirect, render
from book.filters import BookFilter
from book.models import Book, Orders
from book import forms
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,DetailView,UpdateView,TemplateView
from django.utils.decorators import method_decorator
from book.decorators import signin_required


@method_decorator(signin_required,name="dispatch")
class BookCreateView(CreateView):
    model=Book
    form_class=forms.BookCreatForm
    template_name="addbook.html"
    success_url= reverse_lazy("listbook")

@method_decorator(signin_required,name="dispatch")
class BookDetails(DetailView):
    model=Book
    template_name="viewbook.html"
    context_object_name="book"
    pk_url_kwarg="id"

@method_decorator(signin_required,name="dispatch")
class BookList(ListView):
    model=Book
    template_name="listbook.html" 
    context_object_name="books"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["orders"]=Orders.objects.all()
        return context

@method_decorator(signin_required,name="dispatch")
class BookUpdate(UpdateView):
    model=Book
    form_class= forms.BookCreatForm
    template_name="editbook.html"
    pk_url_kwarg="id"
    success_url = reverse_lazy("listbook")

@method_decorator(signin_required,name="dispatch")
class BookRemove(DeleteView):
    model=Book
    template_name = "removebook.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("listbook")

@method_decorator(signin_required,name="dispatch")
class ViewCustomerOrders(ListView):
    model=Orders
    template_name="customer_order.html"
    context_object_name="orders"

    def get_context_data(self,*args,object_list=None,**kwargs):
        context=super().get_context_data(**kwargs)
        neworders=Orders.objects.filter(status="orderplaced")
        context["neworders"]=neworders
        delorders=Orders.objects.filter(status="delivered")
        context["delorders"]=delorders
        context["ordercount"]=neworders.count()
        return context

@method_decorator(signin_required,name="dispatch")
class ViewSingleCustomer(DetailView):
    model=Orders
    template_name="customer_order_detail.html"
    context_object_name="order"
    pk_url_kwarg = "id"


@method_decorator(signin_required,name="dispatch")
class ViewOrderUpdate(UpdateView):
    model=Orders
    template_name="orderupdate.html"
    pk_url_kwarg="id"
    form_class=forms.OrderUpdateForm
    success_url = reverse_lazy("cust_orders")

class BookSearchView(TemplateView):
    template_name="book.html"
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        f=BookFilter(self.request.GET,queryset=Book.objects.all())
        context["filter"]=f
        return context



