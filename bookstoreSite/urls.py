"""bookstoreSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from bookstore.views import product, product_details # not needed
from django.conf import settings
from django.conf.urls.static import static
from bookstore import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.product, name='index'),
    path('', views.product ),
    path('register/', views.register_request, name='register'),
    path('product/<int:id>', views.product_details, name='product_details'),
    path('shopping_cart/', views.shopping_cart, name='shopping_cart'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#if settings.DEBUG:
    #urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)