from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import TransportRequestForm, TransportCompanyForm
from .models import TransportRequest, TransportCompany


def login_view(request):
    """Handles employee login."""
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == 'POST':
        auth_form = AuthenticationForm(request, data=request.POST)
        if auth_form.is_valid():
            username = auth_form.cleaned_data.get('username')
            password = auth_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome, {username}!")
                return redirect('dashboard')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        auth_form = AuthenticationForm()
    
    return render(request, 'requests_app/login.html', {
        'auth_form': auth_form,
        'title': 'Employee Login'
    })

@login_required
def logout_view(request):
    """Handles HOD logout."""
    logout(request)
    messages.info(request, "You have been logged out successfully.")
    return redirect('login')


@login_required
def dashboard_view(request):
    """Shows all transport requests submitted by employees."""
    # Show all transport requests if user is admin/staff, otherwise show all requests
    if request.user.is_staff or request.user.is_superuser:
        transport_requests = TransportRequest.objects.all().order_by('-submitted_at')
    else:
        transport_requests = TransportRequest.objects.all().order_by('-submitted_at')
    
    context = {
        'transport_requests': transport_requests,
        'title': f"{request.user.username}'s Dashboard"
    }
    return render(request, 'requests_app/dashboard.html', context)


@login_required
def transport_request_view(request):
    """Employee form where they can request a vehicle after login."""
    if request.method == 'POST':
        form = TransportRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Transport request submitted successfully. Status: Pending.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = TransportRequestForm()

    return render(request, 'requests_app/transport_request.html', {'form': form, 'title': 'Transport Request'})


@login_required
def admin_transport_company_create(request):
    """Admin portal to add or update transport company/driver details. Requires login."""
    # Optional: require staff users only
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('dashboard')

    if request.method == 'POST':
        form = TransportCompanyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Transport company saved successfully.')
            return redirect('admin_transport_company_create')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = TransportCompanyForm()

    companies = TransportCompany.objects.all().order_by('-created_at')
    return render(request, 'requests_app/admin_transport_company.html', {'form': form, 'companies': companies, 'title': 'Admin - Transport Companies'})
