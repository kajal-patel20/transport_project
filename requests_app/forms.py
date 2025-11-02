from django import forms
from .models import TransportRequest, TransportCompany


class TransportRequestForm(forms.ModelForm):
    date_required = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-input'}),
        label="Date of Vehicle Required"
    )
    
    time_required = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time', 'class': 'form-input'}),
        label="Time Required",
        required=False
    )

    class Meta:
        model = TransportRequest
        fields = [
            'name_of_employee', 'employee_code', 'mobile_number', 'vehicle_type',
            'date_required', 'time_required', 'purpose', 'pickup_location', 'drop_location'
        ]
        widgets = {
            'name_of_employee': forms.TextInput(attrs={'class': 'form-input'}),
            'employee_code': forms.TextInput(attrs={'class': 'form-input'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-input'}),
            'vehicle_type': forms.Select(attrs={'class': 'form-select'}),
            'purpose': forms.Textarea(attrs={'class': 'form-input', 'rows': 3}),
            'pickup_location': forms.TextInput(attrs={'class': 'form-input'}),
            'drop_location': forms.TextInput(attrs={'class': 'form-input'}),
        }


class TransportCompanyForm(forms.ModelForm):
    class Meta:
        model = TransportCompany
        fields = [
            'company_name', 'email', 'contact_number', 'driver_name', 'driver_contact_number',
            'vehicle_number', 'pickup_location', 'unique_id'
        ]
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-input'}),
            'driver_name': forms.TextInput(attrs={'class': 'form-input'}),
            'driver_contact_number': forms.TextInput(attrs={'class': 'form-input'}),
            'vehicle_number': forms.TextInput(attrs={'class': 'form-input'}),
            'pickup_location': forms.TextInput(attrs={'class': 'form-input'}),
            'unique_id': forms.TextInput(attrs={'class': 'form-input'}),
        }
