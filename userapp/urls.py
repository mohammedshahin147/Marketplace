from django.urls import path
from .import views

urlpatterns = [
    path('home',views.Home,name='Home') ,
    path('booking/<int:id>',views.BookingView,name='BookingView') ,
    path('bookings',views.BookingView,name='BookingViews') ,
    path('searchitems',views.SearchView,name='SearchView'),
]

