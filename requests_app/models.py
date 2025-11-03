from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class TransportRequest(models.Model):
    """A transport request submitted by an employee."""
    name_of_employee = models.CharField(max_length=255)
    employee_code = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=20)

    VEHICLE_CHOICES = [
        ("Car", "Car"),
        ("Train", "Train"),
        ("Flight", "Flight"),
        ("Bus", "Bus"),
    ]
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_CHOICES, default="Car")

    date_required = models.DateField(verbose_name="Date of Vehicle Required")
    time_required = models.TimeField(verbose_name="Time Required", null=True, blank=True)
    purpose = models.TextField(blank=True, null=True)
    pickup_location = models.CharField(max_length=255)
    drop_location = models.CharField(max_length=255)

    submitted_at = models.DateTimeField(auto_now_add=True)

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Scheduled", "Scheduled"),
        ("Completed", "Completed"),
        ("Cancelled", "Cancelled"),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")
    
    # Link to assigned transport company
    assigned_transport = models.ForeignKey(
        'TransportCompany', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='assigned_requests',
        verbose_name="Assigned Transport Company"
    )

    def __str__(self):
        return f"TransportRequest({self.name_of_employee}, {self.employee_code}, {self.date_required})"


class TransportCompany(models.Model):
    """Represents a transport company / driver details for admin."""
    company_name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    contact_number = models.CharField(max_length=20, blank=True, null=True)

    driver_name = models.CharField(max_length=255)
    driver_contact_number = models.CharField(max_length=20)
    vehicle_number = models.CharField(max_length=50)
    pickup_location = models.CharField(max_length=255, blank=True, null=True)
    unique_id = models.CharField(max_length=100, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.company_name} - {self.vehicle_number} ({self.unique_id})"
