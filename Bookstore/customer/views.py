from django.db.models.query import QuerySet
from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from customer import forms
from book.models import Book,Cart,Orders,WhishList
from django.views.generic import  TemplateView,ListView
from django.contrib import messages
from django.db.models import Sum

class CustomerView(ListView):
    model=Book
    template_name="userhome.html"
    context_object_name="books"

    def get_context_data(self,*args,object_list=None,**kwargs):
        context=super().get_context_data(**kwargs)
        context["lbooks"]=Book.objects.order_by('-id')[:6]
        return context


class SignUpView(TemplateView):
    def get(self, request, *args, **kwargs):
        form=forms.UserRegistrationForm() 
        context={}
        context["form"]=form
        print(form)
        return render(request,"signup.html",context)

    def post(self,request):
        context={}
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print("user created")
            return redirect("signin")
        else:
            context["form"]=form
            return render(request,"signup.html",context)

class SignInView(TemplateView):
    def get(self,request,*args,**kwargs):
        form=forms.LoginForm()
        return render(request,"signin.html",{"form":form})

    def post(self,request, *args, **kwargs):
        form=forms.LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            user=authenticate(request,username=username,password=password)
            print(form)
            if user:
                login(request,user)
                return redirect("customerhome")
            
            else:
                return render(request,"signin.html",{"form":form})
        else:
            print("hello")
            context={"form":form}
            return render(request,"signin.html",context)

def sign_out(request):
    logout(request)
    return redirect("signin")


class AddToCart(TemplateView):
    model=Cart
    def get(self,request, *args, **kwargs):
        id=kwargs["id"]
        book=Book.objects.get(id=id)
        cart=Cart.objects.create(item=book,user=request.user)
        cart.save()
        print("book added to cart")
        messages.success(request,"item adedd to your cart")
        return redirect("customerhome")

class ViewMyCart(TemplateView):
    model=Cart
    template_name="mycart.html"
    context={}
    def get(self,request, *args, **kwargs):
        mycart=self.model.objects.filter(user=request.user,status="incart")
        self.context["items"]=mycart
        total=Cart.objects.filter(user=request.user,status="incart").aggregate(Sum("item__price"))
        self.context["total"]=total["item__price__sum"]
        return render(request,self.template_name,self.context)

class RemoveItemFromCart(TemplateView):
    model=Cart

    def get(self,request, *args, **kwargs):
        id=kwargs["id"]
        cart=Cart.objects.get(id=id)
        cart.status="cancelled"
        cart.save()
        messages.error(request,"item removed from your cart")
        return redirect("customerhome")
 
class OrderCreate(TemplateView):
    model=Orders
    form_class=forms.OrderForm
    template_name="order_create.html"
    context={}
    def get(self,request,*args,**kwargs):
        form=self.form_class()
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    
    def post(self,request,*args,**kwargs):
        cart_id=kwargs["id"]
        cart_item=Cart.objects.get(id=cart_id)
        form=self.form_class(request.POST)
        if form.is_valid():
            address=form.cleaned_data["address"]
            user=request.user.username
            item=cart_item.item
            order=self.model.objects.create(
                item=item,
                user=user,
                address=address,
            )
            order.save()
            cart_item.status="orderplaced"
            cart_item.save()
            messages.success(request,"order placed")
            return redirect("customerhome")

class ViewMyOrder(ListView):
    model=Orders
    template_name="myorders.html" 
    context_object_name="myorders"
    def get_queryset(self):
        queryset=super().get_queryset()
        queryset=self.model.objects.filter(user=self.request.user)
        return queryset

class AddToWhisList(TemplateView):
    model=WhishList
    template_name="whishlist.html"
    def get(self,request,*args,**kwargs):
        id=kwargs["id"]
        book=Book.objects.get(id=id)
        whish=WhishList.objects.create(wishitem=book,user=request.user)
        whish.save()
        print("added to whislist")
        messages.success(request,"added to whishlist")
        return redirect("customerhome")














# class OrdersView(TemplateView):
#     model=Orders
#     template_name="myorders.html"
#     context={}
#     def get(self,request,*args,**kwargs):
#         mycart=self.model.objects.filter(user=request.user,status="orderplaced")
#         self.context["items"]=mycart
#         return render(request,self.template_name,self.context)



# def sign_up(request):
#     form=forms.UserRegistrationForm()
#     context={}
#     context["form"]=form
#     if request.method=="POST":
#         form=forms.UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             print("user created")
#             return redirect("signin")
#         else:
#             return render(request,"signup.html",context)
#     return render(request,"signup.html",context)

# def sign_in(request):
#     form=forms.LoginForm()
#     context={"form":form}
#     if request.method=="POST":
#         form=forms.LoginForm(request.POST)
#         if form.is_valid():
#             username=form.cleaned_data["username"]
#             password=form.cleaned_data["password"]
#             user=authenticate(request,username=username,password=password)
#             if user:
#                 login(request,user)
#                 return redirect("customerhome")
#     return render(request,"signin.html",context)

