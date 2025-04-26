"""
URL configuration for first_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.shortcuts import redirect


# normalerweise werden hier keine views eingerichtet
def redirect_to_tech_gadgets(request):
    return redirect('tech_gadgets/', permanent=True)    # verändert Statuscode von 302 zu 301


urlpatterns = [
    path('admin/', admin.site.urls),

    # bindet die urls der App tech_gadgets ein, Basis-URL ist tech_gadgets/, alles dahinter steht in den urls in der App tech_gadgets
    path('tech_gadgets/', include('tech_gadgets.urls')),

    # für die Homepage wird der view redirect_to_tech_gadgets aufgerufen, der leitet an tech_gadgets weiter
    # redirect hat Statuscode 302
    path('', redirect_to_tech_gadgets),


    # path('test/', start_page_view)
]
