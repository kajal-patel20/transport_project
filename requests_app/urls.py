from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'), 
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('transport/request/', views.transport_request_view, name='transport_request'),
    path('admin/transport-companies/', views.admin_transport_company_create, name='admin_transport_company_create'),
]
