from django.urls import path

#from . import views
from .views import Index,SignUpView, InventoryList, AddItem, EditItem, DeleteItem
from django.contrib.auth import views as auth_views
urlpatterns = [ 
    path('', Index.as_view(), name='Index'),
    path('/inventorylist/', InventoryList.as_view(), name='InventoryList'), 
    path('/signup', SignUpView.as_view(), name = 'signup'),
    path('/login/', auth_views.LoginView.as_view(template_name='inventory/login.html'), name = 'login'),
    path('/logout/', auth_views.LogoutView.as_view(template_name= 'inventory/logout.html'), name = 'logout'),
    path('/add_item/', AddItem.as_view(template_name='inventory/add_item.html'), name = 'add_item'),   
    path('/edit_item/<int:pk>', EditItem.as_view(), name='edit_item'),#dynamic url to edit item based on id which is the primrary key
    path('/delete_item/<int:pk>', DeleteItem.as_view(), name= 'delete_item'),
]
