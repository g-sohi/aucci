"""AUCCI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webapp.urls')),
    path('listing/<str:name>/', views.listing, name='listing'),
    path('listing/', views.listing, name='listing'),
    path('listing_by_user/<str:username>/', views.listing_by_user, name='listing_by_user'),
    path('listing_by_category/<str:category>/', views.listing_by_category, name='listing_by_category'),
    path('listing_by_params/<str:gender>/<str:brand>/<str:category>/<str:size>/<str:pcolor>/', views.listing_by_params, name='listing_by_params'),
    path('listing_by_id/<str:oid>/', views.listing_by_id, name='listing_by_id'),
    path('delete_listing/<str:oid>/', views.delete_listing, name='delete_listing'),
    path('create_listing/', views.create_listing, name='create_listing'),
    path('categories/', views.categories, name='categories'),
    path('update_listing/<str:oid>/', views.update_listing, name='update_listing'),
    path('update_listing_price/<str:oid>/', views.update_listing_price, name="update_listing_price"),
    path('up/', views.up, name='up'),
    path('create_bid_item/<str:listingid>/', views.create_bid_item, name='create_bid_item'),
    path('update_bid_item/<str:bidid>/', views.update_bid_item, name='update_bid_item'),
    path('delete_bidder/', views.delete_bidder, name='delete_bidder'),
    path('mybids/<str:bidid>/', views.mybids, name='mybids'),    
    path('get_highest_bidder/<str:bidid>/', views.get_highest_bidder, name='get_highest_bidder'),    
    path('delete_bidder/<str:bidid>/', views.delete_bidder, name='delete_bidder'),    
    path('get_my_bids/<str:username>/', views.get_my_bids, name='get_my_bids'),
    path('get_listing_by_bid_id/<str:bidid>/',views.get_listing_by_bid_id, name='get_listing_by_id'),
    path('get_bid_id_by_listing_id/<str:oid>/', views.get_bid_id_by_listing_id, name='get_bid_id_by_listing_id'),
]
