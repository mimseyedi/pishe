from django.contrib import admin
from django.urls import path, include
import account.views as views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('signup', views.signup_view, name="signup"),
    path('reset_password', views.reset_password_view, name="reset_password"),
    path('password_sent', views.password_sent_view, name="password_sent"),
    path('info', views.account_info_view, name="account_info"),
    path('dashboard', views.dashboard_view, name="dashboard"),
    path('setting', views.account_setting_view, name="account_sett"),
    path('favorite', views.account_favorite_view, name="account_fav"),
    path('orders', views.account_orders_view, name="account_ord"),
    path('password_changed', views.pass_changed_view, name="pass_changed"),
    path('account_deleted', views.account_deleted_view, name="account_del"),
]