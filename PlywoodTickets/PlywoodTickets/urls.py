"""
URL configuration for PlywoodTickets project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
]

# urlpatterns += [
#     path('login/', include('login.urls')),
# ]
# urlpatterns += [
#     path('', RedirectView.as_view(url='login/', permanent=True)),
# ]

# urlpatterns += [
#     path('registration/', include('registration.urls')),
# ]
# urlpatterns += [
#     path('', RedirectView.as_view(url='registration/', permanent=True)),
# ]

urlpatterns += [
    path('personalLocker/', include('personalLocker.urls')),
]
urlpatterns += [
    path('', RedirectView.as_view(url='personalLocker/', permanent=True)),
]

urlpatterns += [
    path('mainpage/', include('mainpage.urls')),
]
urlpatterns += [
    path('', RedirectView.as_view(url='mainpage/', permanent=True)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)