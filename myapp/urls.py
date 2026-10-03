from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('about', views.about, name='about-page'),
    path('contact', views.contact, name='cont-page'),
    path('viewcont', views.viewContact, name='cont-view-page'),
    path('delcont/<int:id>', views.delContact, name='cont-del-page'),
    path('updcont/<int:id>', views.updateContact, name='cont-upd-page'),
    path('register', views.register, name='reg-page'),
    path('login', views.userLogin, name='login-page'),
    path('logout', views.userLogout, name='logout-page'),
]
