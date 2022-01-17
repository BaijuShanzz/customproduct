from django.urls import path

from django.contrib.auth import views as auth_views

from accounts import views
urlpatterns = [
    path('',views.home, name='home'),
    path('customer/<str:pk_test>/', views.customer, name='customer'),
    path('products/',views.products, name='products'),

    path('createorder/<str:pk>/', views.createorder, name='createorder'),
    path('updateorder/<str:pk>/', views.updateorder, name='updateorder'),
    path('deleteorder/<str:pk>/', views.deleteorder, name='deleteorder'),
    path('register',views.register, name='register'),
    path('login', views.loginuser, name='login'),
    path('logout', views.logoutuser, name='logout'),
    path('userpage',views.userpage, name='userpage'),
    path('account/', views.accountsettings, name="account"),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"), name="reset_password"),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), name="password_reset_done"),

    path('reset_password/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), name="password_reset_confirm"),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"), name="password_reset_complete"),

]