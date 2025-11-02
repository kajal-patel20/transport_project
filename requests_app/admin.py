from django.contrib import admin
from .models import TransportCompany, TransportRequest


@admin.register(TransportCompany)
class TransportCompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'driver_name', 'driver_contact_number', 'vehicle_number', 'unique_id', 'pickup_location', 'created_at')
    search_fields = ('company_name', 'driver_name', 'vehicle_number', 'unique_id')


@admin.register(TransportRequest)
class TransportRequestAdmin(admin.ModelAdmin):
    list_display = ('name_of_employee', 'employee_code', 'mobile_number', 'vehicle_type', 'date_required', 'time_required', 'pickup_location', 'drop_location', 'status', 'assigned_transport', 'submitted_at')
    list_filter = ('vehicle_type', 'status', 'date_required', 'submitted_at')
    search_fields = ('name_of_employee', 'employee_code', 'mobile_number', 'pickup_location', 'drop_location', 'purpose')
    readonly_fields = ('submitted_at',)
    actions = ['mark_scheduled', 'mark_pending', 'mark_completed', 'mark_cancelled']
    
    fieldsets = (
        ('Employee Information', {
            'fields': ('name_of_employee', 'employee_code', 'mobile_number')
        }),
        ('Transport Details', {
            'fields': ('vehicle_type', 'date_required', 'time_required', 'purpose')
        }),
        ('Location Details', {
            'fields': ('pickup_location', 'drop_location')
        }),
        ('Assignment & Status', {
            'fields': ('assigned_transport', 'status', 'submitted_at')
        }),
    )
    
    def mark_scheduled(self, request, queryset):
        queryset.update(status='Scheduled')
    mark_scheduled.short_description = "Mark selected requests as Scheduled"

    def mark_pending(self, request, queryset):
        queryset.update(status='Pending')
    mark_pending.short_description = "Mark selected requests as Pending"

    def mark_completed(self, request, queryset):
        queryset.update(status='Completed')
    mark_completed.short_description = "Mark selected requests as Completed"
    
    def mark_cancelled(self, request, queryset):
        queryset.update(status='Cancelled')
    mark_cancelled.short_description = "Mark selected requests as Cancelled"
