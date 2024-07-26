from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin, name='admin'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('reservarCita/', reservarCita, name='reservarCita'),
    path('reserva_del/<str:pk>', reserva_del, name='reserva_del'),
    path('reserva_edit/<str:pk>/', editar_reserva, name='reserva_edit'),
    path('reservaRealizada/', reservaRealizada, name='reservaRealizada'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]