"""
URL configuration for RattmWeb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
----------------------------------------------------------------------------
-> Urls Config allows Django to determine which view should handle a given 
URL request.
----------------------------------------------------------------------------
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('transaction/', include('transaction.urls')),
    path('esg/', include('esg.urls')),
    path('env_impact_history/', include('env_impact_history.urls'))
]