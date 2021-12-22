from django.urls import path
from book import  views

urlpatterns = [
     path('add',views.BookCreateView.as_view(),name="bookadd"),
     path('list',views.BookList.as_view(),name="listbook"),
     path('remove/<int:id>',views.BookRemove.as_view(),name="deletebook"),
     path('update/<int:id>',views.BookUpdate.as_view(),name="updatebook"),
     path('view/<int:id>',views.BookDetails.as_view(),name="viewbook"),
     path("orders/list",views.ViewCustomerOrders.as_view(),name="cust_orders"),
     path("customer/orders/<int:id>",views.ViewSingleCustomer.as_view(),name="cust_single_order"),
     path("customer/orderupdate/<int:id>",views.ViewOrderUpdate.as_view(),name="orderupdate"),
     path("find",views.BookSearchView.as_view(),name="filterbook"),
]