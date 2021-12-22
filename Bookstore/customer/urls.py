from django.urls import path
from customer import views
urlpatterns = [
    path("home",views.CustomerView.as_view(),name="customerhome"),
    path("accounts/users/signup",views.SignUpView.as_view(),name="signup"),
    path("accounts/users/signin",views.SignInView.as_view(),name="signin"),
    path("accounts/users/logout",views.sign_out,name="signout"),
    path("book/addtocart/<int:id>",views.AddToCart.as_view(),name="addtocart"),
    path("book/mycart",views.ViewMyCart.as_view(),name="viewcart"),
    path("book/mycart/remove/<int:id>",views.RemoveItemFromCart.as_view(),name="deleteitem"),
    path("book/buynow/<int:id>",views.OrderCreate.as_view(),name="ordercreate"),
    path("book/myorders",views.ViewMyOrder.as_view(),name="myorders"),
    path("book/whishlist/<int:id>",views.AddToWhisList.as_view(),name="adwhishlist"),
]