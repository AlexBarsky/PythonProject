from django.contrib import admin
from .models import Organization, Status, Customer, Order, Employee, Service, Purchase

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'org_address_street', 'org_address_city', 'org_postcode', 'org_phone', 'employees_count')


class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'statuses_name')


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'personal_phone', 'visits', 'status_id')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_id', 'valuations', 'orders_cost', 'orders_date')


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'middle_name', 'last_name', 'age', 'personal_phone', 'employees_email',
                    'employees_experience', 'employees_salary', 'employees_rating', 'login')


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'services_name', 'services_price', 'employee_id')


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_id', 'service_id')


admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Purchase, PurchaseAdmin)
