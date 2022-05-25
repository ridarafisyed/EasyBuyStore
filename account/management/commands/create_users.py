
from django.core.management import BaseCommand
from account.models import Store
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    # Show this when the user types help
    help = "Create Role and its permissions"

    # A command must define handle()
    def handle(self, *args, **options):
   
        obj1 = User.objects.create_client(username="storeowner1", first_name="Sherlock", last_name="Holmes", email="sherlock@storeowner1.com", password="store1234")
        obj1.save()
        store = Store.objects.create(owner= obj1, name="StoreOne")
        store.save()
        print("Creating {} user and his Store {}".format(obj1, store))


        obj1 = User.objects.create_client(username="storeowner2", first_name="Mycroft", last_name="Holmes", email="mycroft@storeowner2.com", password="store1234" )
        obj1.save()
        store = Store.objects.create(owner= obj1, name="StoreTwo")
        store.save()
        print("Creating {} user and his Store {}".format(obj1, store))
       
        obj1  = User.objects.create_client(username="storeowner3", first_name="John", last_name="Watson", email="john@storeowner2.com", password="store1234")
        obj1.save()
        store = Store.objects.create(owner= obj1, name="StoreThree")
        store.save()
        print("Creating {} user and his Store {}".format(obj1, store))

        obj1  = User.objects.create_user(username="customer1", first_name="Greg", last_name="Lestrade", email="greg@gmail.com", password="customer1234")
        obj1.save()
        print("Creating {} user".format(obj1))
       

        obj1  = User.objects.create_user(username="customer2", first_name="James", last_name="Moriarty", email="james@gmail.com", password="customer1234")
        obj1.save()
        print("Creating {} user".format(obj1))
        
        obj1  = User.objects.create_user(username="customer3", first_name="Molly", last_name="Hooper", email="molly@gmail.com", password="customer1234")
        obj1.save()
        print("Creating {} user ".format(obj1))