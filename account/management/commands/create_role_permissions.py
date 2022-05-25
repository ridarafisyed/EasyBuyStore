
from django.core.management import BaseCommand
from accounts.models import Role, Permissions

ROLES =['Principal', 'Partner','Director','Accounting','Manager',
        'Sr. Atterney', 'Jr. Atterney', 'Paralegal', 'Assistant', 'Administrator', 'IT']


PERMISSIONS = ['Contact', 'Matter', 'Calender', 'Flat Fee', 'Expenses','Trust','Task(s)',
    'Invoice', 'Payments','Full DOB','Full SSN', 'Partial DOB', 'Partial SSN',
    'Roles', 'Reports', 'Discounts', 'Bank Acounts']



class Command(BaseCommand):
    # Show this when the user types help
    help = "Create Role and its permissions"

    # A command must define handle()
    def handle(self, *args, **options):
        for role_name in ROLES:

            new_role = Role.objects.create(name=role_name)
            
            for permission in PERMISSIONS:
                permission_obj = Permissions.objects.create(role = new_role, name = permission)
                name = "permission {} with role {}".format(permission, role_name)
                print("Creating {}".format(name))