from django.forms import ModelForm,fields, widgets
from book.models import Book,Orders
from django import  forms

# class BookCreatForm(forms.Form):
#     book_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     author=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     price=forms.CharField(widget=forms.NumberInput(attrs={"class":"form-control"}))
#     copies=forms.CharField(widget=forms.NumberInput(attrs={"class":"form-control"}))
class BookCreatForm(ModelForm):
    class Meta:
        model=Book
        fields=["book_name","author","price","copies","image"]
        widgets={
            'book_name':forms.TextInput(attrs={"class":"form-control"}),
            'author':forms.TextInput(attrs={"class":"form-control"}),
            'price':forms.NumberInput(attrs={"class":"form-control"}),
            'copies':forms.NumberInput(attrs={"class":"form-control"})
        }
        labels={
            'book_name':'Book Name',
            'author':'Author',
            'price':'Price',
            'copies':'Copies'
        }

class OrderUpdateForm(ModelForm): 
    class Meta:
        model=Orders
        fields=["status","expected_delivery_date"]
        widgets={
            "status":forms.Select(attrs={"class":"form-select"}),
            "expected_delivery_date":forms.DateInput(attrs={"type":"date"}),
        }