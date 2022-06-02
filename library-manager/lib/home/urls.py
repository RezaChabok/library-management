from django.urls import path
from .views import home_View , login_user, log_out_user, book_view , search_View



app_name = 'home'

urlpatterns = [
    
]

urlpatterns = [
    path('', home_View, name='home'),
    path('login', login_user, name='login'),
    path('logout', log_out_user, name='logout'),
    path('book/<_isbn>/',book_view,name='book_info'),
    path('search/',search_View,name='search'),

]