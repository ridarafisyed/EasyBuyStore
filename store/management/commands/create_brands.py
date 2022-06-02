
from django.core.management import BaseCommand
from django.template.defaultfilters import slugify
from store.models import Brand, Category, SubCategory

CATEGORIES =  [
        {
            "title": "ac",
            "image": "ac.jpg"
        },
        {
            "title": "cooler",
            "image": "cooler.jpg"
        },
        {
            "title": "desktop",
            "image": "desktop.jpeg"
        },
        {
            "title": "freezer",
            "image": "freezer.jpg"
        },
        {
            "title": "fridge",
            "image": "fridge.jpg"
        },
        {
            "title": "laptop",
            "image": "laptop.png"
        },
        {
            "title": "mobile",
            "image": "mobile.png"
        },
        {
            "title": "tablet",
            "image": "tablet.jpg"
        },
        {
            "title": "tv",
            "image": "tv.jpg"
        },
        {
            "title": "washing machine",
            "image": "washing.jpg"
        },
        {
            "title": "bike",
            "image": "bike.jpg"
        },
        {
            "title": "car",
            "image": "car.jpg"
        }
    ]

SUBCATEGORIES = [
        {
            "category": "laptop",
            "title": "gaming laptops"
        },
        {
            "category": "laptop",
            "title": "convertible"
        },
        {
            "category": "laptop",
            "title": "notebook"
        },
        {
            "category": "laptop",
            "title": "probook"
        },
        {
            "category": "tablet",
            "title": "android "
        },
        {
            "category": "tablet",
            "title": "ios"
        },
        {
            "category": "tablet",
            "title": "windows"
        },
        {
            "category": "mobile",
            "title": "android "
        },
        {
            "category": "mobile",
            "title": "ios"
        },
        {
            "category": "mobile",
            "title": "windows"
        },
        {
            "category": "tv",
            "title": "smart tv"
        },
        {
            "category": "tv",
            "title": "led tv"
        },
        {
            "category": "tv",
            "title": "4k tv"
        },
        {
            "category": "tv",
            "title": "qled tv"
        },
        {
            "category": "tv",
            "title": "lcd tv"
        },
        {
            "category": "tv",
            "title": "oled tv"
        },
        {
            "category": "desktop",
            "title": "gaming desktop"
        },
        {
            "category": "desktop",
            "title": "all in one"
        },
        {
            "category": "ac",
            "title": "centeral"
        },
        {
            "category": "ac",
            "title": "spilt"
        },
        {
            "category": "ac",
            "title": "window"
        },
        {
            "category": "ac",
            "title": "portable"
        },
        {
            "category": "ac",
            "title": "smart"
        },
        {
            "category": "ac",
            "title": "invertor"
        },
        {
            "category": "cooler",
            "title": "desert "
        },
        {
            "category": "cooler",
            "title": "room "
        },
        {
            "category": "cooler",
            "title": "personal"
        },
        {
            "category": "cooler",
            "title": "invertor"
        },
        {
            "category": "washing machine",
            "title": "semi automatic "
        },
        {
            "category": "washing machine",
            "title": "fully automatic"
        },
        {
            "category": "fridge",
            "title": "double door"
        },
        {
            "category": "fridge",
            "title": "single door"
        },
        {
            "category": "fridge",
            "title": "mini refregerator"
        },
        {
            "category": "freezer",
            "title": "vertical"
        },
        {
            "category": "freezer",
            "title": "double door deep freezer"
        },
        {
            "category": "freezer",
            "title": "single door deep freezer"
        },
        {
            "category": "bike",
            "title": "electric"
        },
        {
            "category": "bike",
            "title": "general"
        },
        {
            "category": "bike",
            "title": "heavy"
        },
        {
            "category": "bike",
            "title": "sports"
        },
        {
            "category": "car",
            "title": "automatic"
        },
        {
            "category": "car",
            "title": "manual"
        },
        {
            "category": "car",
            "title": "suv"
        },
        {
            "category": "car",
            "title": "hybrid"
        }
    ]

BRANDS =[
        {
            "title": "acer",
            "image": "acer.png"
        },
        {
            "title": "apple",
            "image": "apple.png"
        },
        {
            "title": "boss",
            "image": "boss.png"
        },
        {
            "title": "changhong ruba",
            "image": "crube.jpg"
        },
        {
            "title": "dell",
            "image": "dell.png"
        },
        {
            "title": "eco star",
            "image": "ecostar.jpg"
        },
        {
            "title": "haire",
            "image": "haier.png"
        },
        {
            "title": "honda",
            "image": "honda.png"
        },
        {
            "title": "hp",
            "image": "hp.png"
        },
        {
            "title": "huawei",
            "image": "huawei.png"
        },
        {
            "title": "iphone",
            "image": "images.png"
        },
        {
            "title": "itel",
            "image": "itel.png"
        },
        {
            "title": "keeway",
            "image": "keeway.jpg"
        },
        {
            "title": "lenovo",
            "image": "lenovo.png"
        },
        {
            "title": "lg",
            "image": "lg.jpg"
        },
        {
            "title": "microsoft",
            "image": "microsoft.png"
        },
        {
            "title": "msi",
            "image": "msi.png"
        },
        {
            "title": "nokia",
            "image": "nokia.png"
        },
        {
            "title": "oppo",
            "image": "oppo.png"
        },
        {
            "title": "orient",
            "image": "orient.png"
        },
        {
            "title": "samsung",
            "image": "samsung.png"
        },
        {
            "title": "sony",
            "image": "sony.png"
        },
        {
            "title": "super asia",
            "image": "superasia.png"
        },
        {
            "title": "tcl",
            "image": "tcl.png"
        },
        {
            "title": "toyota",
            "image": "toyota.png"
        },
        {
            "title": "united",
            "image": "united.jpg"
        },
        {
            "title": "vivo",
            "image": "vivo.png"
        },
        {
            "title": "xiaomi",
            "image": "xiaomi.png"
        },
        {
            "title": "yamaha",
            "image": "yamaha.png"
        }
    ]
class Command(BaseCommand):
    # Show this when the user types help
    help = "Create Role and its permissions"

    # A command must define handle()
    

    def handle(self, *args, **options):
        for item in BRANDS:
            title = item.get('title')
            image= item.get('image')
            brand, create = Brand.objects.get_or_create(title=title, image= image)
            print("brand is created successfull! " + title)
            brand.save()

        for item in CATEGORIES:
            title = item.get('title')
            image= item.get('image')
            slug = slugify(title)
            obj, create = Category.objects.get_or_create(title=title, image=image)
            print("Category is created successfull! " + title)
            obj.save()
        
        for item in SUBCATEGORIES:
            title = item.get('category')
            category = Category.objects.get(title = title)
            title = item.get('title')
            subcat, create = SubCategory.objects.get_or_create(category=category, title= title)
            print("Sub-Category is created successfull! " +  title)
            subcat.save()