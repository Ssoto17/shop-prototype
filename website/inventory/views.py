from django.forms import BaseModelForm
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View, CreateView, DeleteView, UpdateView
from .forms import UserRegisterForm, InventoryItemForm
#from django.contrib.auth.models import UserRegisterForm
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .models import InventoryItem, Location 
from django.urls import reverse_lazy


class Index (TemplateView):
    template_name = 'inventory/index.html'

class InventoryList(View):
    def get(self,request):
        items = InventoryItem.objects.all()

        return render(request, 'inventory/inventorylist.html', {'items': items})
    
class SignUpView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'inventory/signup.html', {'form': form})
    def post(self, request):
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'],
                password = form.cleaned_data['password1'])
            login(request, user)
            return redirect('Index')
        return render(request, 'inventory/signup.html', {'form': form})
    
class AddItem(CreateView):
    model = InventoryItem
    form_class = InventoryItemForm
    template_name = 'inventory/add_item.html'
    success_url = reverse_lazy('InventoryList')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['locations'] = Location.objects.all()
        return context
    
class EditItem(UpdateView):
    model = InventoryItem
    form_class = InventoryItemForm
    template_name = 'inventory/add_item.html'
    success_url = reverse_lazy('InventoryList')

class DeleteItem(DeleteView):
    model= InventoryItem
    template_name = 'inventory/delete_item.html'
    success_url = reverse_lazy('InventoryList')
    context_object_name = 'item'


    