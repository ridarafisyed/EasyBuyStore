import random
from django.core.management import BaseCommand
from account.models import Store, UserAccount 
from store.models import Product, Category
from decimal  import Decimal


CATEGORIES = [""]

PRODUCTS = [
        {
            "title": "Hp Notebook 14 - DQ0032DX",
            "description": "More Information&#10;Product Type        Laptop&#10;Availability         In Stock&#10;Series        HP. Notebook&#10;Model        dq0032dx&#10;OS Version        Windows 11 Home&#10;Processor        Intel Celeron&#10;    Generation        Dual Core&#10;    Speed        1.1 / 2.8 Ghz, N4020, 4MB Cache, 2 Core, 2 Thread&#10;Screen Size        14\"&#10;    Max Res        1366 x 768 :HD&#10;    Detail        micro-edge, BrightView, 220 nits, 45% NTSC&#10;RAM        4 GB&#10;Drive        64 GB&#10;    Type        eMMC&#10;Optical        No Optical Drive&#10;Graphics Card        Intel Integrated Graphics&#10;    Memory        System Shared&#10;Audio        Dual speakers&#10;Features        Wifi, WebCam, Bluetooth&#10;External Ports        USB 3.x, HDMI, Headphone/Mic combo, USB-C&#10;Dimensions        32.4 x 22.5 x 1.79 cm&#10;Weight        3.218 lbs&#10;Manufacturer image        Additional Information&#10;Warranty        International / Manufacturer&#10;Color        White",
            "category": "laptop",
            "sub_cat": "HP laptop",
            "price": "58500.00",
            "quantity": "70",
            "image": "https://myshop.pk/pub/media/catalog/product/cache/044822f421975447750ae9c7b18ed8ed/h/p/hp-14-dq0032dx-white-myshop-pk-1.jpg"
        },
        {
            "title": "Hp Notebook 14 - DQ0032DX UG",
            "description": "More Information&#10;Product Type        Laptop&#10;Availability         In Stock&#10;Series        HP. Notebook&#10;Model        dq0032dx&#10;OS Version        Windows 11 Home&#10;Processor        Intel Celeron&#10;    Generation        Dual Core&#10;    Speed        1.1 / 2.8 Ghz, N4020, 4MB Cache, 2 Core, 2 Thread&#10;Screen Size        14\"&#10;    Max Res        1366 x 768 :HD&#10;    Detail        micro-edge, BrightView, 220 nits, 45% NTSC&#10;RAM        4 GB&#10;Drive        64 GB&#10;    Type        eMMC&#10;    Additional        256GB SD Card&#10;    Detail        256GB MicroSD Card will be added in External Memory Card Slot&#10;Optical        No Optical Drive&#10;Graphics Card        Intel Integrated Graphics&#10;    Memory        System Shared&#10;Audio        Dual speakers&#10;Features        Wifi, WebCam, Bluetooth&#10;External Ports        USB 3.x, HDMI, Headphone/Mic combo, USB-C&#10;Dimensions        32.4 x 22.5 x 1.79 cm&#10;Weight        3.218 lbs&#10;Manufacturer image        Additional Information&#10;Warranty        International / Manufacturer&#10;Color        White",
            "category": "laptop",
            "sub_cat": "HP laptop",
            "price": "62900.00",
            "quantity": "22",
            "image": "https://myshop.pk/pub/media/catalog/product/cache/044822f421975447750ae9c7b18ed8ed/h/p/hp-14-dq0032dx-white-myshop-pk-1_1.jpg"
        },
        {
            "title": "Hp Notebook 15s - DU1520TU ",
            "description": "More Information&#10;Product Type        Laptop&#10;Availability         Same Day Delivery&#10;Series        HP. Notebook&#10;Model        DU1520TU (465S5PA)&#10;OS Version        Windows 10 Home&#10;Processor        Intel Celeron&#10;    Generation        1st Generation&#10;    Speed        1.1 / 2.8 Ghz, N4020, 4MB Cache, 2 Core, 2 Thread&#10;    Detail        Intel® Celeron® N4020 (1.1 GHz base frequency, up to 2.8 GHz burst frequency, 4 MB L2 cache, 2 cores)&#10;Screen Size        15.6\"&#10;    Max Res        1366 x 768 :HD&#10;    Detail        15.6\" diagonal, HD (1366 x 768), micro-edge, BrightView, 220 nits, 45% NTSC&#10;RAM        4 GB&#10;    Detail        4 GB DDR4-2400 MHz RAM (1 x 4 GB)&#10;Drive        1 TB&#10;    Type        HDD&#10;    Detail        1 TB 5400 rpm SATA HDD&#10;Optical        No Optical Drive&#10;Graphics Card        Intel Integrated Graphics&#10;    Memory        System Shared&#10;    Detail        Intel® UHD Graphics 600&#10;Features        Wifi, WebCam, Bluetooth&#10;External Ports        USB 3.x, HDMI, RJ45 (LAN), Headphone/Mic combo, USB-C&#10;    Total USB        2&#10;Dimensions        35.85 x 24.2 x 1.99 cm&#10;Weight        3.92 lbs&#10;Manufacturer image        Additional Information&#10;Warranty        1 Year Local&#10;Color        Silver",
            "category": "laptop",
            "sub_cat": "HP laptop",
            "price": "73500.00",
            "quantity": "25",
            "image": "https://myshop.pk/pub/media/catalog/product/cache/044822f421975447750ae9c7b18ed8ed/h/p/hp_notebook_15_-_dy2071wm_myshop-pk-1_1_1_1_12.jpg"
        },
        {
            "title": "Hp Notebook 14 - DQ2031tg",
            "description": "More Information&#10;Extra Value        with 4Core Processor, FullHD Screen & Fingerprint&#10;Product Type        Laptop&#10;Availability         Sold Out&#10;Series        HP. Notebook&#10;Model        DQ2031tg (333V2UA)&#10;OS Version        Windows 10 Home in S Mode&#10;Processor        Intel Core i3&#10;    Generation        11th Generation&#10;    Speed        2.0 / 3.7 Ghz, i3-1125G4, 8MB Cache, 4 Core, 8 Thread&#10;Screen Size        14\"&#10;    Max Res        1920 x 1080 :Full HD&#10;    Detail        35.6 cm (14\") diagonal, FHD (1920 x 1080), IPS, micro-edge, anti-glare, 250 nits, 45% NTSC&#10;RAM        4 GB&#10;    Detail        4 GB DDR4-2666 MHz RAM (1 x 4 GB)&#10;Drive        128 GB&#10;    Type        SSD&#10;    Detail        128 GB SATA 3 TLC M.2 SSD&#10;Optical        No Optical Drive&#10;Graphics Card        Intel Integrated Graphics&#10;    Memory        System Shared&#10;    Detail        Intel® UHD Graphics&#10;Audio        HD Audio with stereo speakers&#10;Features        Wifi, WebCam, Bluetooth, Fingerprint Reader&#10;External Ports        USB 3.0, HDMI, Headphone/Mic combo, USB-C&#10;    Total USB        2&#10;Dimensions        12.76 x 8.86 x 0.71 in&#10;Weight        3.24 lb&#10;Manufacturer image        Additional Information&#10;Warranty        International / Manufacturer&#10;Color        Silver",
            "category": "laptop",
            "sub_cat": "HP laptop",
            "price": "87500.00",
            "quantity": "51",
            "image": "https://myshop.pk/pub/media/catalog/product/cache/044822f421975447750ae9c7b18ed8ed/7/1/71tc1jqtois.-ac-sl1500--4012-720176-081221123603028-myshop-pk-1.jpg"
        },
        {
            "title": "Hp Notebook 15 - FQ2002NE",
            "description": "More Information&#10;Product Type        Laptop&#10;Availability         Coming Soon&#10;Series        HP. Notebook&#10;Model        fq2002ne&#10;OS Version        Windows 10 Home&#10;Processor        Intel Core i3&#10;    Generation        11th Generation&#10;    Speed        1.7 / 4.1 Ghz, i3-1115G4, 6MB Cache, 2 Core, 4 Thread&#10;Screen Size        15.6\"&#10;    Max Res        1366 x 768 :HD&#10;    Detail        39.6 cm (15.6\") diagonal, HD (1366 x 768), micro-edge, anti-glare, 250 nits, 45% NTSC&#10;RAM        4 GB&#10;Drive        128 GB&#10;    Type        SSD&#10;Optical        No Optical Drive&#10;Graphics Card        Intel Integrated Graphics&#10;    Memory        System Shared&#10;Features        Wifi, WebCam, Bluetooth&#10;External Ports        USB 3.x, HDMI, Headphone/Mic combo, USB-C, Card Slot&#10;Dimensions        35.85 x 24.2 x 1.79 cm&#10;Weight        3.858 lbs&#10;Manufacturer image        Additional Information&#10;Warranty        International / Manufacturer&#10;Color        Black",
            "category": "laptop",
            "sub_cat": "HP laptop",
            "price": "87500.00",
            "quantity": "32",
            "image": "https://myshop.pk/pub/media/catalog/product/cache/044822f421975447750ae9c7b18ed8ed/h/p/hp-notebook-15-dw3157nia-myshop-pk-1_1.jpg"
        },
        {
            "title": "Dell Inspiron 15 - 3511 i3 :1y",
            "description": "More Information&#10;Product Type        Laptop&#10;Availability         In Stock&#10;Series        Dell. Inspiron&#10;Model        3511 (3000)&#10;OS Version        DOS&#10;Processor        Intel Core i3&#10;    Generation        11th Generation&#10;    Speed        1.7 / 4.1 Ghz, i3-1115G4, 6MB Cache, 2 Core, 4 Thread&#10;Screen Size        15.6\"&#10;    Max Res        1920 x 1080 :Full HD&#10;    Detail        15.6-inch FHD (1920 x 1080) Anti-glare LED Backlight Non-Touch Narrow Border WVA Display&#10;RAM        4 GB&#10;Drive        1 TB&#10;    Type        HDD&#10;Optical        No Optical Drive&#10;Graphics Card        Intel Integrated Graphics&#10;    Memory        System Shared&#10;Features        Wifi, WebCam, Bluetooth&#10;External Ports        USB 2.0, USB 3.x, HDMI, Headphone/Mic combo, Card Slot&#10;Dimensions        Height (front): 17.50 mm (0.68\") x Height (rear): 18.99 mm (0.74\") x Width: 358.50 mm (14.11\") x Depth: 235.56 (9.27\")&#10;Weight        1.85 kg / 4.07 lb&#10;Manufacturer image        Additional Information&#10;Warranty        1 Year Local&#10;Color        Black&#10;Color Detail        Carbon Black",
            "category": "laptop",
            "sub_cat": "Dell laptop",
            "price": "88500.00",
            "quantity": "20",
            "image": "https://myshop.pk/pub/media/catalog/product/cache/26f8091d81cea4b38d820a1d1a4f62be/d/e/dell-inspiron-3511-black-1-myshop-pk-1_2_1.jpg"
        },
        {
            "title": "Dell Vostro 14 - 3400",
            "description": "More Information&#10;Product Type        Laptop&#10;Availability         In Stock&#10;Series        Dell. Vostro&#10;Model        3400&#10;OS Version        DOS&#10;Processor        Intel Core i5&#10;    Generation        11th Generation&#10;    Speed        2.4 / 4.2 Ghz, i5-1135G7, 8MB Cache, 4 Core, 8 Thread&#10;Screen Size        14\"&#10;    Max Res        1920 x 1080 :Full HD&#10;    Detail        14\", FHD 1920x1080, 60Hz, Non-Touch, AG, Wide Viewing Angle, LED-Backlit, Narrow Border&#10;RAM        8 GB&#10;Drive        1 TB&#10;    Type        HDD&#10;Optical        No Optical Drive&#10;Graphics Card        Intel Integrated Graphics&#10;    Memory        System Shared&#10;Features        Wifi, WebCam, Bluetooth&#10;External Ports        USB 2.0, USB 3.x, HDMI, RJ45 (LAN), Headphone/Mic combo, Card Slot&#10;Dimensions        328 x 239.5 x 18.1-19 mm&#10;Weight        3.51 lbs&#10;Manufacturer image        Additional Information&#10;Warranty        International / Manufacturer&#10;Color        Black&#10;Color Detail        Accent Black",
            "category": "laptop",
            "sub_cat": "Dell laptop",
            "price": "110500.00",
            "quantity": "70",
            "image": "https://myshop.pk/pub/media/catalog/product/cache/26f8091d81cea4b38d820a1d1a4f62be/d/e/dell-vostor-14-3400-myshop-pk-1.jpg"
        },
        {
            "title": "Dell Latitude - 3520 :1y",
            "description": "More Information&#10;Product Type        Laptop&#10;Availability         Same Day Delivery&#10;Series        Dell. Latitude&#10;Model        3520&#10;OS Version        DOS&#10;Processor        Intel Core i3&#10;    Generation        11th Generation&#10;    Speed        1.7 / 4.1 Ghz, i3-1115G4, 6MB Cache, 2 Core, 4 Thread&#10;Screen Size        15.6\"&#10;    Max Res        1920 x 1080 :Full HD&#10;    Detail        15.6\" FHD (1920 x 1080) AG Non-Touch, 250nits, Camera w/shutter & Microphone, WLAN Capable&#10;RAM        8 GB&#10;Drive        256 GB&#10;    Type        SSD&#10;Optical        No Optical Drive&#10;Graphics Card        Intel Integrated Graphics&#10;    Memory        System Shared&#10;Audio        Stereo speakers with Realtek Audio Controller, 2W x 2 = 4 W&#10;Features        Wifi, WebCam, Bluetooth, Fingerprint Reader, Backlit Keyboard&#10;External Ports        USB 3.x, HDMI, RJ45 (LAN), Headphone/Mic combo, USB-C, Card Slot&#10;Dimensions        Height: 18.06 mm (0.71\") x Width: 361 mm (14.2\") x Depth: 240.9 mm (9.5\")&#10;Weight        3.95 lbs&#10;Manufacturer image        Additional Information&#10;Warranty        International / Manufacturer&#10;Color        Black",
            "category": "laptop",
            "sub_cat": "Dell laptop",
            "price": "119500.00",
            "quantity": "4",
            "image": "https://myshop.pk/pub/media/catalog/product/cache/26f8091d81cea4b38d820a1d1a4f62be/d/e/dell-latitude-3520-myshop-2_2.jpg"
        },
        {
            "title": "Apple Macbook Air - 13\" 256GB",
            "description": "More Information&#10;Product Type        Laptop&#10;Availability         &#10;Series        Apple. Macbook Air (2020)&#10;Model        MGN63LL-MGND3LL-MGN93LL&#10;OS Version        macOS&#10;Processor        Apple&#10;    Generation        Latest&#10;    Speed        M1 chip, 8 Core CPU, 7 Core GPU&#10;    Detail        8-core CPU with 4 perform­ance cores and 4 efficiency cores&#10;7-core GPU&#10;16-core Neural Engine&#10;Screen Size        13.3\"&#10;    Max Res        2560 x 1600 :WQXGA&#10;    Detail        13.3-inch (diagonal) LED-backlit display with IPS technology; 2560-by-1600 native resolution at 227 pixels per inch with support for millions of colors&#10;RAM        8 GB&#10;Drive        256 GB&#10;    Type        SSD&#10;Optical        No Optical Drive&#10;Graphics Card        Apple M1 GPU Graphics&#10;    Memory        System Shared&#10;Features        Wifi, WebCam, Bluetooth, Backlit Keyboard&#10;External Ports        Headphone/Mic combo, USB-C",
            "category": "laptop",
            "sub_cat": "Apple",
            "price": "209900.00",
            "quantity": "54",
            "image": "https://myshop.pk/pub/media/catalog/product/cache/26f8091d81cea4b38d820a1d1a4f62be/a/p/apple-macbook-air-myshop.pk03_2_1_1.jpg"
        },
        {
            "title": "Apple Macbook Air - 13\" 512GB",
            "description": "More Information&#10;Product Type        Laptop&#10;Availability         &#10;Series        Apple. Macbook Air (2020)&#10;Model        MGN73LL-MGNE3LL-MGNA3LL&#10;OS Version        macOS&#10;Processor        Apple&#10;    Generation        Latest&#10;    Speed        M1 chip, 8 Core CPU, 8 Core GPU&#10;    Detail        8-core CPU with 4 perform­ance cores and 4 efficiency cores&#10;8-core GPU&#10;16-core Neural Engine&#10;Screen Size        13.3\"&#10;    Max Res        2560 x 1600 :WQXGA&#10;    Detail        13.3-inch (diagonal) LED-backlit display with IPS technology; 2560-by-1600 native resolution at 227 pixels per inch with support for millions of colors&#10;RAM        8 GB&#10;Drive        512 GB&#10;    Type        SSD&#10;Optical        No Optical Drive&#10;Graphics Card        Apple M1 GPU Graphics&#10;    Memory        System Shared&#10;Features        Wifi, WebCam, Bluetooth, Backlit Keyboard&#10;External Ports        Headphone/Mic combo, USB-C",
            "category": "laptop",
            "sub_cat": "Apple",
            "price": "254900.00",
            "quantity": "42",
            "image": "https://myshop.pk/pub/media/catalog/product/cache/26f8091d81cea4b38d820a1d1a4f62be/a/p/apple-macbook-air-myshop.pk03_2_1_2.jpg"
        },
        {
            "title": "Apple Macbook Air - 13\" 16GB 256GB",
            "description": "More Information&#10;Product Type        Laptop&#10;Availability         &#10;Series        Apple. Macbook Air (2020)&#10;OS Version        macOS&#10;Processor        Apple&#10;    Generation        Latest&#10;    Speed        M1 chip, 8 Core CPU, 7 Core GPU&#10;    Detail        8-core CPU with 4 perform­ance cores and 4 efficiency cores&#10;7-core GPU&#10;16-core Neural Engine&#10;Screen Size        13.3\"&#10;    Max Res        2560 x 1600 :WQXGA&#10;    Detail        13.3-inch (diagonal) LED-backlit display with IPS technology; 2560-by-1600 native resolution at 227 pixels per inch with support for millions of colors&#10;RAM        16 GB&#10;Drive        256 GB&#10;    Type        SSD&#10;Optical        No Optical Drive&#10;Graphics Card        Apple M1 GPU Graphics&#10;    Memory        System Shared&#10;Features        Wifi, WebCam, Bluetooth, Backlit Keyboard&#10;External Ports        Headphone/Mic combo, USB-C",
            "category": "laptop",
            "sub_cat": "Apple",
            "price": "267900.00",
            "quantity": "34",
            "image": "https://myshop.pk/pub/media/catalog/product/cache/26f8091d81cea4b38d820a1d1a4f62be/a/p/apple-macbook-air-myshop.pk04_6_1.jpg"
        },
        {
            "title": "Samsung 32 Inch 32N5000 LED TV Price",
            "description": "The Lowest price of Samsung 32 Inch 32N5000 LED TV in Pakistan is Rs. 35,489, and the estimated average price is Rs. 45,707.  32N5000 is one of the flat, non-smart LED TVs from Samsung having a screen size of 32 inches. It comes equipped with Full HD resolution, HDMI, and USB connectivity. Full HD resolution provides crisp and clear images Wide Color Enhancer improves the image quality and displays bright and rich colors with more detail. You can plug and play your favorite entertainment on this LED TV. Enjoy videos, music, and view photos through a USB connection. Moreover, Clean View in 32N5000 LED TV reduces noise and interference and lets you enjoy everything with refined quality.Previously the price was Rs. 33,749 in November, approximately a 4% increase. Latest May 2022 price from tracked on major eCommerce stores all across Pakistan.",
            "category": "TV",
            "sub_cat": "Samsung",
            "price": "35489.00",
            "quantity": "73",
            "image": "https://pakistanistores.com/public/data/images/6ef3f6f956ef81cdc9dc19ebc664f225.jpg"
        },
        {
            "title": "Sony 40 Inch 40W652D LED TV Price  ",
            "description": "Screen Size: 40-inch Resolution: 1920 x 1080 (FHD) Smart Features: No Hdmi: Yes&#10;The Sony 40W652D is a higher midrange LED TV that has advanced features such as X-Protection Pro, X-Reality Pro, and Live Color technology Even though it is not a smart TV, the excellent connectivity options that support USB, HDMI, and smartphone connectivity ensure that you can stream your favorite movies and TV shows on the LED TV. The Dolby Digital audio system ensures that you have a clear, natural audio playback when watching TV. The picture quality is superb and the Live Color technology ensures that the Sony 40W652D delivers vibrant colors and excellent contrast.",
            "category": "TV",
            "sub_cat": "Sony",
            "price": "65999.00",
            "quantity": "80",
            "image": "https://pakistanistores.com/public/data/images/15492040076ebde75379376f4f506069279981f224.jpg"
        },
        {
            "title": "Sony 43 Inch 43W660F LED TV Price  ",
            "description": "Screen Size: 43-inch Resolution: 1920 x 1080 (FHD) Smart Features: No Hdmi: Yes&#10;The Sony 43W660F is one of the newest models from the Sony Bravia series that provides a comfortable viewing experience with a durable design. This 43-inch flat FHD LED TV features the X-Reality Pro engine with Live Colour technology that ensures excellent color reproduction with great contrast and sharpness. Overall, the image quality is quite impressive, particularly if you are looking to watch 1080p TV shows and movies on your LED TV. The connectivity features cover all the basics including USB, HDMI, and smartphone connectivity. The HDR10 feature further adds to the overall quality of the picture enabling a superb viewing for users. Overall, if you are looking for an excellent non-smart FHD LED TV then the Sony 43W660F is a good choice to consider.",
            "category": "TV",
            "sub_cat": "Sony",
            "price": "74999.00",
            "quantity": "75",
            "image": "https://pakistanistores.com/public/data/images/15492040664ee8d767352857b2f694129f23065c24.jpg"
        },
        {
            "title": "TCL 32 Inch Led Tv D310 Price ",
            "description": "Screen Size: 32-inch Resolution: 1366 x 768 (HD) Smart Features: No Hdmi: Yes&#10;D310 is a basic, non-smart, entry-level LED TV from TCL which comes with features of HD resolution, 32 inches display, and USB & HDMI connections. Natural Light Engine in this LED TV provides the brightest and highest contrast level to ensure true color reproduction. Turbo Sound enhances your entertainment experience and the USB & HDMI connections allow you to share your favorite data from different technologies and systems and display on your TV. Although it is not a smart TV, it is a good choice for the people who are on a budget.",
            "category": "TV",
            "sub_cat": "TCL",
            "price": "27999.00",
            "quantity": "69",
            "image": "https://pakistanistores.com/public/data/images/4538c03ac4db9673b7c4b066dec4aa13.jpg"
        },
        {
            "title": "PEL 32\" Smart HD LED TV",
            "description": "Screen Size: 32-inch Resolution: 1366 x 768 (HD) Smart Features: Yes HDMI: Yes&#10;PEL ColorOn 32\" is a Smart LED TV with HD resolution. It is a budget and pretty basic LED but of good quality. It's smart features lets you watch YouTube and Netflix in HD quality and has the HDMI connectivity to connect your devices to play anything on a bigger display.",
            "category": "TV",
            "sub_cat": "PEL",
            "price": "35900.00",
            "quantity": "40",
            "image": "https://pakistanistores.com/public/data/images/355aa5dbbac28fda218a441c3105521d.jpg"
        },
        {
            "title": "Huawei Nova 9",
            "description": "Huawei Nova 9 price in Pakistan&#10;Huawei Nova 9 price in Pakistan is Rs. 107,999. Official dealers and warranty providers regulate the retail price of Huawei mobile products in official warranty.&#10;&#10;Price of Huawei Nova 9 in Pakistan is Rs. 107,999.&#10;Price of Huawei in USD is $537.&#10;Huawei Nova 9 - Flagship Smartphone With Kirin Chipset&#10;Huawei is unveiling its new Nova 9 to the market soon. Huawei is working on its new device of its Nova-series. The smartphone will be launch in August of October this year. The Chinese company is launching a flagship smartphone and it will be called Huawei Nova 9. The smartphone got a Chipset of Qualcomm SM7325 Snapdragon 778G 4G SoC which is the most powerful chipset in the market now a day's and to give more power to this Huawei's Nova 9 to have a 2.4 GHz Octa-Core processor inside the phone to make the device ultra fast. And also there is a GPU of Adreno 642L under the hood of this smartphone. The display screen size of the smartphone is 6.57 Inches and It will provide the user with full HD plus the resolution of 1080 x 2340 Pixels. The new Huawei Nova 9's having an OLED Capacitive Touchscreen display that is the latest one and well known for its outstanding results. The smartphone is using Corning Gorilla Glass for protection purposes. This handset Nova 9 by Huawei will be paired with a gigantic RAM capacity of 8 gigabytes. The chipset and the RAM capacity of the device show that it will enable the user to execute things with this smartphone within seconds. The internal storage capacity of the smartphone is 256 gigabytes that is enough to store a huge amount of data for future use. On the rear of the Huawei 9, there is a Quad Camera setup. The main sensor will be 50 megapixels, 8 megapixels ultra-wide, 2 megapixels depth, 2 megapixels macro sensors. The selfie shooter of the phone is 32 megapixels wide, to make taking selfies more easy and attractive. The Huawei Nova's 9 is having an under-display, optical fingerprint reader to secure the data on the smartphone and only allow the authorized person. The Huawei Nova 9 will be fueled with a Non-removable Li-Po 4500 mAh battery that will carry support for Fast charging. Samsung and other tech giants will face serious competition when the coming smartphone Nova 9's will release.",
            "category": "Mobile",
            "sub_cat": "Huawei",
            "price": "107999.00",
            "quantity": "47",
            "image": "hhttps://www.whatmobile.com.pk/admin/images/Huawei/HuaweiNova9-b.jpg"
        },
        {
            "title": "Infinix Zero 5G",
            "description": "Infinix Zero 5G price in Pakistan&#10;Infinix Zero 5G price in Pakistan is Rs. 49,999. Official dealers and warranty providers regulate the retail price of Infinix mobile products in official warranty.&#10;&#10;Price of Infinix Zero 5G in Pakistan is Rs. 49,999.&#10;Price of Infinix in USD is $248.&#10;Infinix Zero 5G - A Dimensity Smartphone&#10;Infinix is launching a new smartphone Zero 5G to the market soon. Infinix is working on a new device with 5G technology. The coming smartphone of the company was popped in the database of the Play Console. The smartphone will be a mid-ranger and will be named Infinix Zero 5G. The smartphone got a Chipset of Dimensity 900 which is the most powerful chipset in the market now a day's, and to give more power to this Infinix's Zero 5G to have an Octa-Core processor inside the phone to make the device ultra fast. And also there is a GPU of Mali G68 under the hood of this smartphone. The display screen size of the smartphone is 6.78 Inches and It will provide the user with full HD plus the resolution of 1080 x 2460 Pixels. The new Infinix Zero 5G's has a IS LCD Capacitive Touchscreen display that is the latest one and well known for its outstanding results. The smartphone is using Corning Gorilla Glass for protection purposes. The coming handset Zero 5G by Infinix will be paired with a gigantic RAM capacity of 8 gigabytes. The chipset and the RAM capacity of the device show that it will enable the user to execute things with this smartphone within seconds. The internal storage capacity of the smartphone is 128 gigabytes that is enough to store a huge amount of data for future use. On the rear of the Infinix 5G, there is a triple camera setup. The main sensor will be 48 megapixels, 13 megapixels, 2 megapixels. The selfie shooter of the phone is 16 megapixels wide, to make taking selfies more easy and attractive. The Infinix Zero's 5G is having a side-mounted fingerprint reader to secure the data on the smartphone and only allow the authorized person. The Infinix Zero 5G will be fueled with a Non-removable Li-Po 5000 mAh battery that will carry support for Fast charging of 33W. Infinix Zero 5G and other tech giants will face serious competition when the coming smartphone Zero 5G's will released.",
            "category": "Mobile",
            "sub_cat": "Infinix",
            "price": "49999.00",
            "quantity": "33",
            "image": "https://www.whatmobile.com.pk/admin/images/Infinix/InfinixZero5G-b.jpg"
        },
        {
            "title": "itel Vision 3",
            "description": "itel Vision 3 price in Pakistan&#10;itel Vision 3 price in Pakistan is Rs. 16,299. Official dealers and warranty providers regulate the retail price of itel mobile products in official warranty.&#10;&#10;Price of itel Vision 3 in Pakistan is Rs. 16,299.&#10;Price of itel in USD is $81.&#10;itel Vision 3 - Anther Budget-Friendly Smartphone&#10;itel is launching a new Vision 3 to the market. The Chinses company is unveiling a new smartphone of its Vision series. The coming smartphone will be a budget-friendly phone and will be named itel Vision 3. The smartphone got a Chipset of Unisoc SC9863A, which is the most powerful chipset, and to give more power to this handset has a 1.6 GHz Octa-Core processor inside the itel's Vision 3 to make the device ultra fast. And also there is a GPU of PowerVR GE8322 under the hood of this smartphone. The display screen size of the smartphone is 6.6 Inches and It will provide the user with full HD plus the resolution of 720 x 1600 Pixels. The new itel Vision 3's having an IPS LCD Capacitive Touchscreen display that is the latest one and well known for its outstanding results. The upcoming new handset of the Vision 3 by itel will be paired with a gigantic RAM capacity of 3 gigabytes. The chipset and the RAM capacity of the device show that it will enable the user to execute things with this smartphone within seconds. The internal storage capacity of the itel 2GB is 32 gigabytes which is enough to store a huge amount of data for future use. On the rear of the smartphone, there is a Dual Camera setup. The main sensor of the itel Vision's 3 will be 8 megapixels, AI Lens. The selfie shooter of the phone is 5 megapixels to make taking selfies more easy and more attractive. The itel Vision 3 is having a rear-mounted fingerprint reader to secure the data on the smartphone and only allows the authorized person. The device will be fueled with a Non-removable Li-Po 5,000 mAh battery that will carry support for Fast charging of 18W. Samsung and other tech giants will face serious competition when the coming Vision 3's will be released.",
            "category": "Mobile",
            "sub_cat": "itel vision",
            "price": "18499.00",
            "quantity": "45",
            "image": "https://www.whatmobile.com.pk/admin/images/itel/itelVision33GB-b.jpg"
        },
        {
            "title": "Oppo F21",
            "description": "Oppo F21 price in Pakistan&#10;Oppo F21 price in Pakistan is expected to be Rs. 48,999. Oppo F21 Expected to be launched on Apr 30, 2022. This is 6 GB RAM / 128 GB internal storage variant of Oppo which is available in Various colours.&#10;&#10;Expected Price of Oppo F21 in Pakistan is Rs. 48,999.&#10;Expected Price of Oppo in USD is $365.&#10;Oppo F21 - A Powerful Smartphone&#10;The Chinese Oppo is launching the F21 smartphone to the market. This company may be preparing to launch the F17 successor in India next month. While one group of tipsters believe the smartphone will be called F19, others are suggesting the company might end up calling it the Oppo F21. The smartphone will be powered by one of the latest chipsets available for smartphones in the market that is called Mediatek Helio. The new Oppo's F21 has got a 2.2 GHz Octa-Core processor under the hood of this handset. This new upcoming smartphone has a 6.5 Inches screen size which is a big-screen display, with a Super AMOLED Capacitive Touchscreen, and this device Oppo F21's going to have a full-HD display with a resolution of 1080 x 2400 Pixels. And talking about the Protection of this smartphone it has Corning Gorilla Glass 3+. The upcoming new Oppo sharp F21 is going to packing the upcoming smartphone with 6 gigabytes RAM, which is the highest point of RAM used in this smartphone so you can say that your phone is going to run at a super-fast speed because of its powerful RAM. Oppo has got 128 gigabytes of storage in F21 which means that the capacity of your data is unlimited. On the rear of the smartphone, there is a Quad Camera setup. The main sensor of the smartphone F21 will be 48 megapixels. 8 megapixels, 2 megapixels, 2 megapixels. The selfie shooter in this phone will be 16 megapixels to make taking selfies more easy and attractive with this new F21. The under-display, optical sensor will allow the F21 to protect its data by only allowing the authorized person. The F21 by Oppo will be fueled with a Non-removable Li-Po 4300 mAh battery that will carry support for Fast charging. Samsung and other tech giants will face serious competition when this Oppo F21 will release.",
            "category": "Mobile",
            "sub_cat": "oppo",
            "price": "52999.00",
            "quantity": "52",
            "image": "https://www.whatmobile.com.pk/admin/images/Oppo/OppoF20Pro-b.jpg"
        },
        {
            "title": "Realme 9 pro",
            "description": "Realme 9 pro price in Pakistan&#10;Realme 9 pro price in Pakistan is expected to be Rs. 49,999. Realme 9 pro Expected to be launched on Mar 15, 2022. This is 6 GB RAM / 128 GB internal storage variant of Realme which is available in Midnight Black, Aurora Green, Sunrise Blue colours.&#10;&#10;Expected Price of Realme 9 pro in Pakistan is Rs. 49,999.&#10;Expected Price of Realme in USD is $373.&#10;Realme 9 pro - A Pro Variant Of Realme&#10;Realme is unveiling its new 9 Pro to the market. The Realme is launching its new handsets of its 9-series of smartphones. This is one of them, the device is in a mid-range segment. The company is adding a new Pro variant and it will be called Realme 9 pro. The upcoming smartphone of the company has got a chipset of Qualcomm SM6375 Snapdragon 695, which is used in mid-range devices, to give more power to the handset there is a 2.2 Ghz Octa-Core processor under the hood of this Realme's 9 Pro. Also, there is a GPU of Adreno 619 in this smartphone. This new upcoming smartphone has a 6.6 Inches screen size which is a big-screen display. The new Realme 9 pro's going to have a IPS LCD Capacitive Touchscreen, and this device has got a full-HD display with a resolution of 1080 x 2400 Pixels. The upcoming new 9 pro by Realme has got 8 gigabytes of RAM, which is a powerful RAM used in this smartphone so you can say that your phone is going to run at a super-fast speed because of its powerful RAM. The built-in storage capacity of the Realme pro is 128 gigabytes which means that the capacity of your data is unlimited. On the rear of the smartphone, there is a Quad Camera setup. The main sensor of the phone will be 64 megapixels main sensor 8 megapixels' ultra-wide, and the 2 megapixels depth sensor. The selfie shooter in this Realme 9's pro will be a single camera which is, 16 megapixels to make taking selfies more easy and attractive. The device has got an under-display, the optical fingerprint reader is there to protect it from any unauthorized person. The battery of the Realme 9 Pro is also a massive one. The handset is fueled with (Li-Po Non-removable), 5,000 mAh battery to get enough backup time and the smartphone got a Fast charging. Now Samsung and other smartphone companies will have a competitor when the 9 pro's launched.",
            "category": "Mobile",
            "sub_cat": "Realme",
            "price": "69999.00",
            "quantity": "12",
            "image": "https://www.whatmobile.com.pk/admin/images/Realme/Realme9proPlus-b.jpg"
        },
        {
            "title": "Samsung Galaxy S22",
            "description": "Samsung Galaxy S22 price in Pakistan Samsung Galaxy S22 price in Pakistan is Rs. 179,999. Official dealers and warranty providers regulate the retail price of Samsung mobile products in official warranty. Price of Samsung Galaxy S22 in Pakistan is Rs. 179,999. Price of Samsung in USD is $894. Samsung Galaxy S22 - The Company's Beast Phone Samsung is working on a Galaxy S22 smartphone. This smartphone manufacturer company is working on a beast because it is more than a flagship device. The upcoming smartphone from Samsung will be a powerful handset of the year. The company will call it the Samsung Galaxy S22. The smartphone will be empowered by the Qualcomm SM8450 Snapdragon 8 Gen 1 (4 nm) chipset, this chipset is used in flagship phones. To give more power to this handset there is a 3.0 GHz Octa-Core inside this Samsung's Galaxy S22. There is also a GPU of Adreno 730 under the hood of this smartphone. The device has got a Dynamic AMOLED 2X Capacitive Touchscreen display with a screen size of 6.1 inches and has a full HD+ of resolution 1080 x 2400 Pixels. Samsung Galaxy S22's going to have a bigger screen size, the users of this device will be enjoying using it. They have a Dynamic AMOLED 2X Capacitive Touchscreen, with a full HD resolution of 1080 x 2400 Pixels under the hood of the Galaxy S22 by Samsung. The Protection of the screen this device has got Corning Gorilla Glass Victus. The RAM that is coupled with the SoC is 8 gigabytes. This is the high-end RAM capacity that is used in the Samsung S22. Both, the chipset and the RAM will enhance the processing speed of the handset a great deal. The internal storage is 256 gigabytes that is enough to store the data on the Samsung Galaxy's S22 for the rest of your life. There is a Triple Camera setup in the back of this handset, The main sensor will be 50 megapixels, and the others are yet to be confirmed. The selfie shooter of the Samsung Galaxy S22 is a single camera, which will change your lifestyle. The under-display, ultrasonic fingerprint reader of the handset is there to protect it from any unauthorized person. And the device is IP68 dust/water resistant (up to 1.5m for 30 mins). The battery of the new Galaxy S22's will be somewhere around 3700 mAh. This is enough power for this smartphone, and there is a Fast battery charging.",
            "category": "Mobile",
            "sub_cat": "Samsung",
            "price": "179999.00",
            "quantity": "22",
            "image": "https://www.whatmobile.com.pk/admin/images/Samsung/SamsungGalaxyS22-b.jpg"
        },
        {
            "title": "Tecno Spark 8C",
            "description": "Tecno Spark 8C price in Pakistan&#10;Tecno Spark 8C price in Pakistan is Rs. 17,999. Official dealers and warranty providers regulate the retail price of Tecno mobile products in official warranty.&#10;&#10;Price of Tecno Spark 8C in Pakistan is Rs. 17,999.&#10;Price of Tecno in USD is $89.&#10;Tecno Spark 8C - A Big Battery Phone&#10;Tecno is unveiling its all new Spark 8C to the market soon. The Chinese smartphone company Tecno has released a new handset in its Spark-series. The coming device of the company will be a budget-friendly phone. The newcomer will be called Tecno Spark 8C. The new smartphone will be empowered by the powerful chipset called Unisoc T606. This chipset is used in mid-range smartphones, and to give more power to this Tecno's Spark 8C it has a Quad-Core processor inside the handset. The device has got an IPS LCD Capacitive Touchscreen and also there is a GPU of ARM Mali-G57. The upcoming new Tecno Spark 8C's going to have a big screen size of 6.6 Inches, the users will enjoying using this screen size. This smartphone has a full HD plus resolution of 720 x 1612 Pixels. The Spark 8C by Tecno has 2 gigabytes of RAM that will assist the chipset to perform well and make the execution speed lightning fast. In this upcoming handset, there are 64 gigabytes of internal storage capacity in Tecno 8C. which is enough to store a huge amount of data for a long period of time that can be used in the future. But you can also increase the capacity of storage of the device as it carries support for the MicroSD card. The Tecno Spark's 8C will come equipped with a dual rear camera setup. The main sensor of the handset will be 13 megapixels and the secondary sensor will be an AI sensor. The selfie shooter of the phone will be 8 megapixels. The Tecno Spark 8C features a rear-mounted fingerprint reader plus Face Unlock, that will detect the unauthorized user and will stop him from getting into the phone and steal data. The handset is fueled with a gigantic battery that is going to be a Non-removable Li-Po 5,000 mAh battery Also there is a Battery charging of 10W. The coming Spark 8C's will be a good rival for the Samsung upcoming smartphones.",
            "category": "Mobile",
            "sub_cat": "Tecno spark",
            "price": "22999.00",
            "quantity": "44",
            "image": "https://www.whatmobile.com.pk/admin/images/Tecno/TecnoSpark8C4GB-b.jpg"
        },
        {
            "title": "Vivo X80",
            "description": "Vivo X80 price in Pakistan&#10;Vivo X80 price in Pakistan is Rs. 159,999. Official dealers and warranty providers regulate the retail price of Vivo mobile products in official warranty.&#10;&#10;Price of Vivo X80 in Pakistan is Rs. 159,999.&#10;Price of Vivo in USD is $795.&#10;Vivo X80 - A Powerful Mid-Ranger&#10;Smart tech Vivo is unveiling X80 to the market soon. The Chinese manufacturer is working on a successor of the Vivo X70 series, which was launched a few months ago. Now the company is launching a new series of phones and that will be called Vivo X80. The smartphone will be powered by one of the latest chipsets available for smartphones in the market that is called MediaTek Dimensity 9000. Also, there is a powerful GPU of ARM Mali-G710. The new Vivo's X80 has got an Octa-Core processor under the hood of this handset. This new upcoming smartphone has a 6.78 Inches screen size which is a big-screen display, with a Capacitive LTPO AMOLED Capacitive Touchscreen, and this device Vivo X80's going to have a full-HD display with a resolution of 1080 x 2400 Pixels. Also, there is the latest operating system called Android 12. The upcoming new Vivo sharp X80 is going to pack the upcoming smartphone with 12 gigabytes RAM, which is the highest point of RAM used in this smartphone so you can say that your phone is going to run at a super-fast speed because of its powerful RAM. Vivo has got 256 gigabytes of storage in X80 which means that the capacity of your data is unlimited. On the rear of the smartphone, there is a Triple Camera setup. The main sensor of the smartphone X80 will be 50 megapixels, 12 megapixels, 12 megapixels. The selfie shooter in this phone will be 32 megapixels to make taking selfies more easy and attractive with this new X80. The under-display, optical sensor will allow the X80 to protect its data by only allowing the authorized person. The X80 by Vivo will be fueled with a Non-removable Li-Po 4500 mAh battery that will carry support for Fast charging of 55W. Samsung and other tech giants will face serious competition when this Vivo X80 will release.",
            "category": "Mobile",
            "sub_cat": "Vivo",
            "price": "159999.00",
            "quantity": "20",
            "image": "https://www.whatmobile.com.pk/admin/images/Vivo/VivoX80-b.jpg"
        },
        {
            "title": "Xiaomi 12",
            "description": "Xiaomi 12 price in Pakistan Xiaomi 12 price in Pakistan is Rs. 179,999. Official dealers and warranty providers regulate the retail price of Xiaomi mobile products in official warranty. Price of Xiaomi 12 in Pakistan is Rs. 179,999. Price of Xiaomi in USD is $894. Xiaomi 12- A Most Powerful Machine In The Planet Smart tech Xiaomi will unveil 12 series of smartphones to the market soon this year. According to reports, the company is readying itself to produce its next-level flagship smartphone. Xiaomi will launch two variants in its new 12-series, the first one will be called Xiaomi 12. The smartphone will be powered by one of the latest chipsets in the market Qualcomm Snapdragon 8 Gen 1. The Chipset of the smartphone is also a flagship chipset that can all the high-end specs with accuracy and ease. The new Xiaomi's 12 has a 3.0 GHz Octa-Core processor to give more power to this chipset. The device has a 6.28 Inches massive screen size, the users of this device will be enjoying using it. The Xiaomi 12's going with an AMOLED Capacitive Touchscreen, with a full HD resolution of 1080 x 2340 Pixels under the hood of the handset. The Protection of the screen this device has got Corning Gorilla Glass Victus, also there is a powerful GPU of Adreno. The SoC of the Xiaomi sharp 12 is paired with 8 gigabytes of RAM. The chipset and the RAM of the device will make the processing speed of the phone lightning fast. The upcoming new Xiaomi has got 128 GB of internal storage in 12. This is enough storage capacity that will give you enough space to place a huge amount of data for future use. There is a Triple Camera setup in the back of this handset, The main sensor will be 50 megapixels, and the other will be confirmed yet. The 12 selfie shooter has a single selfie camera, and that is 32 megapixels which will change your lifestyle. The upcoming new 12 has got the latest operating system Android 12. There is an under-display, optical fingerprint reader that is there to protect it from any unauthorized person. The battery of the 12 is also a massive one. The handset is fueled with (Li-Po Non-removable), 4500 mAh battery to get enough backup time and the 12 by Xiaomi got a Fast charging of 67W, it can charge the device very quickly. Now Samsung and other smartphone companies will be looking to bring features like Xiaomi 12.",
            "category": "Mobile",
            "sub_cat": "Xiaomi",
            "price": "179999.00",
            "quantity": "30",
            "image": "https://www.whatmobile.com.pk/admin/images/Xiaomi/Xiaomi12-b.jpg"
        },
        {
            "title": "Keeway SUPERLIGHT 200 ",
            "description": "Factory customs are some of the most popular bikes on earth, and Keeway’s Superlight 200 fits the bill perfectly.                                               &#10;Category Naked Bike&#10;Displacement  200cc&#10;Engine Type  4-Stroke Single Cylinder Air Cooled&#10;Starter Electric&#10;Front Brakes Single Disc&#10;Rear Brakes Drum Brake&#10;Designed to evoke the look, sound and feel of classic customs, the Superlight 200 features the fat-fender, thick-tire, custom-painted and chrome-tinged look that style-conscious riders love.",
            "category": "Bike",
            "sub_cat": "Keeway",
            "price": "650000.00",
            "quantity": "59",
            "image": "https://motorcycleshop.pk/779-large_default/keeway-superlight-200-price-in-pakistan-rating-reviews-and-pictures.jpg"
        },
        {
            "title": "Keeway K-Light 202",
            "description": "Everything you need for a great ride, and nothing more. Handlebar. Mirrors. Speedo. Controls.Its Four-Stroke Single-Cylinder engine is Liquid-cooled for durability and offers a perfect blend of smooth power. There’s also electronic ignition and kick starting, both front and rear disc brakes, a unique exhaust, and a multi-mode Digital instrument, performance and affordability.&#10;Category  Naked Bike&#10;Displacement  200cc&#10;Engine Type  4-Stroke Single Cylinder Air Cooled&#10;Starter  Electric&#10;Front Brakes  Single Disc&#10;Rear Brakes  Drum Brake",
            "category": "Bike",
            "sub_cat": "Keeway",
            "price": "675000.00",
            "quantity": "86",
            "image": "https://motorcycleshop.pk/783-large_default/keeway-k-light-202-price-in-pakistan-rating-reviews-and-pictures.jpg"
        },
        {
            "title": "Yamaha YBR 125",
            "description": "The Yamaha YBR 125 is a light motorcycle made by Yamaha that succeeds it's previous model for this segment, the Yamaha SR125. Introduced in 2005, it comes in naked, faired and 'custom' variants. It has a single-cylinder, air-cooled, four-stroke engine, displacing 124 cc.  Key features of the motorcycle includes; Engine: OHC 125 CC&#10;Design: Sporty&#10;Transmission: 5 Speed&#10;Head Light: HS1 35W/35W",
            "category": "Bike",
            "sub_cat": "Yamaha",
            "price": "232000.00",
            "quantity": "60",
            "image": "https://motorcycleshop.pk/27-large_default/yamaha-ybr-125-price-in-pakistan-rating-reviews-and-pictures.jpg"
        },
        {
            "title": "Yamaha YBR 125G",
            "description": "The Yamaha YBR 125G 4-Stroke motorcycle designed specially for convenience and adventure with 5-speed transmission, engine guard, long front shock absorbed with stylish double front fender and many other appealing features. Colors:&#10;&#10;YBR 125G RED&#10;YBR 125G BLUE&#10;YBR 125G BLACK&#10;PERFORMANCE, DESIGN & COMFORT&#10;&#10;WITH ITS SPLENDID AND UNRUFFLED PERFORMANCE, DESIGN and COMFORT, YBR 125G WON'T LET YOU DOWN.&#10;&#10;",
            "category": "Bike",
            "sub_cat": "Yamaha",
            "price": "245000.00",
            "quantity": "23",
            "image": "https://motorcycleshop.pk/826-large_default/yamaha-ybr-125g-price-in-pakistan-rating-reviews-and-pictures.jpg"
        },
        {
            "title": "United US 100CC Scooty",
            "description": "Category&#10;Street Bike&#10;Displacement&#10;100 cc&#10;Engine Type&#10;4 stroke single cylinder&#10;Compression Ratio&#10;8.8:1&#10;Fuel Control&#10;Injuction&#10;Transmission&#10;Chain&#10;Starter&#10;Kick Start&#10;Front Tyre&#10;2.50 -18&#10;Rear Tyre&#10;2.50 -18&#10;Dry Weight&#10;90 kg&#10;Fuel Tank Capacity&#10;5.5 Liters",
            "category": "Bike",
            "sub_cat": "United Scooty",
            "price": "155000.00",
            "quantity": "0",
            "image": "https://motorcycleshop.pk/989-large_default/united-us-100cc-scooty.jpg"
        },
        {
            "title": "United US125 Euro II",
            "description": "United US 125 Euro II presents in that stage when there is a extraordinary demand for fuel well-organized bikes. The main objective to present the United US 125 is to object potential customers who have high desires for fuel efficient transportation. United US 125 incorporates a manifest Euro II technology completely engineered to succeed your range requirements. Not only this, a noticeably low price label of United US 125 Euro II provides a chance to the customers to consider this bike over other 125cc bikes in the market. United US 125 Euro II is a perfect mixture of engineered fuel competent technology and commanding 125cc engine.&#10;&#10;",
            "category": "Bike",
            "sub_cat": "United Bike",
            "price": "92000.00",
            "quantity": "69",
            "image": "https://motorcycleshop.pk/463-large_default/united-us125-euro-ii-price-in-pakistan-rating-reviews-and-pictures.jpg"
        },
        {
            "title": "Honda Civic RS",
            "description": "MILEAGE (KM/LITER)&#10;11 to 14&#10;Transmission&#10;Automatic (CVT)&#10;Fuel Type&#10;Petrol&#10;Engine&#10;1500 cc&#10;Honda Civic RS Price in Pakistan&#10;The price of Honda Civic RS in Pakistan is PKR 6,649,000. This price of Civic RS is ex-factory and does not include freight, taxes and other documentation charges.&#10;&#10;Variant        Ex-Factory Price        On Road Price&#10;Honda Civic RS&#10;PKR 6,649,000&#10;Get Civic RS On Road Price&#10;Honda Civic RS Colors&#10;Honda Civic RS is available in 7 different colours - Carnelian Red Pearl, Crystal Black Pearl, Lunar Silver Metallic, Meteoroid Gray Metalic, Morning Mist Blue Metallic, Taffeta White , and Urban Titanium Metallic&#10;&#10;Carnelian Red Pearl&#10;&#10;Crystal Black Pearl&#10;&#10;Lunar Silver Metallic&#10;&#10;Meteoroid Gray Metalic&#10;&#10;Morning Mist Blue Metallic&#10;&#10;Taffeta White&#10;&#10;Urban Titanium Metallic&#10;&#10;Honda Civic RS Specifications & Features&#10;Specifications&#10;Features&#10;Specifications&#10;Dimensions&#10;Overall Length 4687 mmKerb Weight 1396 KGOverall Width 1802 mmBoot Space 409 LOverall Height 1432 mmSeating Capacity 5 personsWheel Base 2735 mmNo. of Doors 4 doorsGround Clearance 154 mm&#10;Engine/ Motor&#10;Engine Type PetrolNo. of Cylinders 4Displacement 1500 ccCylinder Configuration In LineHorse Power 176 HP @ 6000 RPMCompression Ratio 10.3:1Torque 220 Nm @ 4500 RPMValves per Cylinder 4Fuel System PGM FIValve Mechanism DOHC DUAL VTC+EXH-VTECMax Speed 260 KM/H&#10;Transmission&#10;Transmission Type Automatic (CVT)Gearbox -CVT &#10;Steering&#10;Steering Type Rack and PinionMinimum Turning Radius 5.3mPower Assisted Electric Power Steering&#10;Suspension & Brakes&#10;Suspension Front: Macpherson with Stabilizer Rear: Multiimage with StabilizerBrakes Front: Disc Rear: Disc&#10;Wheels and Tyres&#10;Wheel Type Alloy WheelsTyre Size 215/50/R17Wheel Size 17 inSpare Tyre PCD -Spare Tyre Size 17 in&#10;Fuel Economy&#10;Mileage City 11 KM/LFuel Tank Capacity 47 LMileage Highway 14 KM/L&#10;Features&#10;Safety&#10;No. of Airbags 2Anti-Lock Braking System (ABS) No. of Seatbelts 5Down Hill Assist Control Immobilizer Hill Start Assist Control Child Lock Traction Control ISOFIX Child Seat Anchors Vehicle Stability Control &#10;Exterior&#10;Alloy Wheels Adjustable Headlights Colored Outside Door Handles Piano BlackFog Lights Side Mirrors With Indicators DRLs Rear Spoiler Sun Roof / Moon Roof  / &#10;Instrumentation&#10;Tachometer Multi Info &#10;Infotainment&#10;CD/DVD Player  / Front Speakers USB and Auxillary Cable Rear Speakers Display Size 9.0 inRear Seat Entertainment &#10;Comfort and Convenience&#10;Air Conditioner Cruise Control Climate Control Driving Modes Rear AC Vents Key Type Smart EntryHeater Keyless Entry Heated Seats Push Start Defogger Central Locking CoolBox Power Door Locks Navigation Power Steering Optional Navigation Power Windows Front Camera Power Mirrors Rear Camera Power Boot Rear Central Control Cup Holders Rear Folding Seat Arm Rest Rear Headrest 3Handbrake ElectricRear Wiper Interior Lighting Seat Material Type Hi-Grade LeatherFront Power Outlet Steering Adjustment Rear Power Outlet Steering Switches ",
            "category": "Cars",
            "sub_cat": "Honda",
            "price": "6649000.00",
            "quantity": "30",
            "image": "https://cache2.pakwheels.com/system/car_generation_pictures/6345/original/Honda_Civic_Front_Right_Angled.jpg?1647970561"
        },
        {
            "title": "Toyota Corolla Altis X Manual 1.6 ",
            "description": "MILEAGE (KM/LITER)&#10;12 to 14&#10;Transmission&#10;Manual&#10;Fuel Type&#10;Petrol&#10;Engine&#10;1600 cc&#10;Toyota Corolla Altis X Manual 1.6 Price in Pakistan&#10;The price of Toyota Corolla Altis X Manual 1.6 in Pakistan is PKR 3,909,000. This price of Corolla Altis X Manual 1.6 is ex-factory and does not include freight, taxes and other documentation charges.&#10;&#10;Variant        Ex-Factory Price        On Road Price&#10;Toyota Corolla Altis X Manual 1.6&#10;PKR 3,909,000&#10;Get Corolla Altis X Manual 1.6 On Road Price&#10;Toyota Corolla Altis X Manual 1.6 2021 Price | Toyota Corolla Altis X Manual 1.6 2020 Price | Toyota Corolla Altis X Manual 1.6 2018 Price&#10;&#10;Toyota Corolla Altis X Manual 1.6 Colors&#10;Toyota Corolla Altis X Manual 1.6 is available in 7 different colours - Attitude Black, Bronze Mica, Dorado Gold, Phantom Brown, Silver Metallic, Strong Blue, and Super White&#10;&#10;Attitude Black&#10;&#10;Bronze Mica&#10;&#10;Dorado Gold&#10;&#10;Phantom Brown&#10;&#10;Silver Metallic&#10;&#10;Strong Blue&#10;&#10;Super White&#10;&#10;Toyota Corolla Altis X Manual 1.6 Specifications & Features&#10;Specifications&#10;Features&#10;Specifications&#10;Dimensions&#10;Overall Length 4620 mmKerb Weight 1275 KGOverall Width 1775 mmBoot Space 470 LOverall Height 1475 mmSeating Capacity 5 personsWheel Base 2700 mmNo. of Doors 5 doorsGround Clearance 175 mm&#10;Engine/ Motor&#10;Engine Type PetrolNo. of Cylinders 4Displacement 1600 ccCylinder Configuration In LineHorse Power 120 HP @ 6000 RPMCompression Ratio 10.0:1Torque 154 Nm @ 5200 RPMValves per Cylinder 4Fuel System Sequential Multiport Fuel InjectionValve Mechanism DOHC 16 Valves with dual VVT-iMax Speed 180 KM/H&#10;Transmission&#10;Transmission Type ManualGearbox 6 - speed&#10;Steering&#10;Steering Type Rack & Pinion with Electronic MotorMinimum Turning Radius 5.4mPower Assisted Electronic Power Steering&#10;Suspension & Brakes&#10;Suspension Front: Macpherson Strut, Rear: Torsion BeamBrakes Front: Ventilated Disc, Rear: Solid Disc&#10;Wheels and Tyres&#10;Wheel Type Steel Rims with Wheels CapsTyre Size 195/65/R15Wheel Size 15 inSpare Tyre PCD 5 x 100mmSpare Tyre Size 15 in&#10;Fuel Economy&#10;Mileage City 12 KM/LFuel Tank Capacity 55 LMileage Highway 14 KM/L&#10;Features&#10;Safety&#10;No. of Airbags 2Anti-Lock Braking System (ABS) No. of Seatbelts 5Down Hill Assist Control Immobilizer Hill Start Assist Control Child Lock Traction Control ISOFIX Child Seat Anchors Vehicle Stability Control &#10;Exterior&#10;Alloy Wheels Adjustable Headlights Colored Outside Door Handles YesFog Lights Side Mirrors With Indicators DRLs Rear Spoiler Sun Roof / Moon Roof  / &#10;Instrumentation&#10;Tachometer Multi Info &#10;Infotainment&#10;CD/DVD Player  / Front Speakers USB and Auxillary Cable Rear Speakers Display Size 9.0 inRear Seat Entertainment &#10;Comfort and Convenience&#10;Air Conditioner Cruise Control Climate Control Driving Modes Rear AC Vents Key Type Keyless entryHeater Keyless Entry Heated Seats Push Start Defogger Central Locking CoolBox Power Door Locks Navigation Power Steering Optional Navigation Power Windows Front Camera Power Mirrors Rear Camera Power Boot Rear Central Control Cup Holders Rear Folding Seat Arm Rest Rear Headrest YesHandbrake Center LeverRear Wiper Interior Lighting Seat Material Type Fabric with manual adjustmentFront Power Outlet Steering Adjustment Rear Power Outlet Steering Switches ",
            "category": "Cars",
            "sub_cat": "Corolla",
            "price": "3909000.00",
            "quantity": "65",
            "image": "https://cache1.pakwheels.com/system/car_generation_pictures/5361/original/Corolla-X-Cars-Cropped-Pictures-for-Website.jpg?1606903674"
        },
        {
            "title": "Toyota Corolla Altis Grande X CVT-i 1.8 Beige Interior",
            "description": "MILEAGE (KM/LITER)&#10;12 to 14&#10;Transmission&#10;Automatic (CVT)&#10;Fuel Type&#10;Petrol&#10;Engine&#10;1800 cc&#10;Toyota Corolla Altis Grande X CVT-i 1.8 Beige Interior Price in Pakistan&#10;The price of Toyota Corolla Altis Grande X CVT-i 1.8 Beige Interior in Pakistan is PKR 4,859,000. This price of Corolla Altis Grande X CVT-i 1.8 Beige Interior is ex-factory and does not include freight, taxes and other documentation charges.&#10;&#10;Variant        Ex-Factory Price        On Road Price&#10;Toyota Corolla Altis Grande X CVT-i 1.8 Beige Interior&#10;PKR 4,859,000&#10;Get Corolla Altis Grande X CVT-i 1.8 Beige Interior On Road Price&#10;Toyota Corolla Altis Grande X CVT-i 1.8 Beige Interior 2021 Price | Toyota Corolla Altis Grande X CVT-i 1.8 Beige Interior 2020 Price | Toyota Corolla Altis Grande X CVT-i 1.8 Beige Interior 2019 Price | Toyota Corolla Altis Grande X CVT-i 1.8 Beige Interior 2018 Price&#10;&#10;Toyota Corolla Altis Grande X CVT-i 1.8 Beige Interior Colors&#10;Toyota Corolla Altis Grande X CVT-i 1.8 Beige Interior is available in 8 different colours - Attitude Black, Bronze Mica, Dorado Gold, Graphite Grey, Phantom Brown, Silver Metallic, Strong Blue, and Super White&#10;&#10;Attitude Black&#10;&#10;Bronze Mica&#10;&#10;Dorado Gold&#10;&#10;Graphite Grey&#10;&#10;Phantom Brown&#10;&#10;Silver Metallic&#10;&#10;Strong Blue&#10;&#10;Super White&#10;&#10;Toyota Corolla Altis Grande X CVT-i 1.8 Beige Interior Specifications & Features&#10;Specifications&#10;Features&#10;Specifications&#10;Dimensions&#10;Overall Length 4620 mmKerb Weight 1275 KGOverall Width 1775 mmBoot Space 470 LOverall Height 1475 mmSeating Capacity 5 personsWheel Base 2700 mmNo. of Doors 5 doorsGround Clearance 170 mm&#10;Engine/ Motor&#10;Engine Type PetrolNo. of Cylinders 4Displacement 1800 ccCylinder Configuration In LineHorse Power 138 HP @ 6400 RPMCompression Ratio 10.0:1Torque 173 Nm @ 4000 RPMValves per Cylinder 4Fuel System Sequential Multiport Fuel InjectionValve Mechanism DOHC 16 Valves with dual VVT-iMax Speed 180 KM/H&#10;Transmission&#10;Transmission Type Automatic (CVT)Gearbox -CVT &#10;Steering&#10;Steering Type Rack & Pinion with Electronic MotorMinimum Turning Radius 5.4mPower Assisted Electronic Power Steering&#10;Suspension & Brakes&#10;Suspension Front: Macpherson Strut, Rear: Torsion BeamBrakes Front: Ventilated Disc, Rear: Solid Disc&#10;Wheels and Tyres&#10;Wheel Type Alloy wheels with Imported Japanese TyresTyre Size 205/55/R16Wheel Size 16 inSpare Tyre PCD 5 x 100mmSpare Tyre Size 16 in&#10;Fuel Economy&#10;Mileage City 12 KM/LFuel Tank Capacity 55 LMileage Highway 14 KM/L&#10;Features&#10;Safety&#10;No. of Airbags 2Anti-Lock Braking System (ABS) No. of Seatbelts 5Down Hill Assist Control Immobilizer Hill Start Assist Control Child Lock Traction Control ISOFIX Child Seat Anchors Vehicle Stability Control &#10;Exterior&#10;Alloy Wheels Adjustable Headlights Colored Outside Door Handles YesFog Lights Side Mirrors With Indicators DRLs Rear Spoiler Sun Roof / Moon Roof  / &#10;Instrumentation&#10;Tachometer Multi Info &#10;Infotainment&#10;CD/DVD Player  / Front Speakers USB and Auxillary Cable Rear Speakers Display Size 9.0 inRear Seat Entertainment &#10;Comfort and Convenience&#10;Air Conditioner Cruise Control Climate Control Driving Modes Rear AC Vents Key Type Keyless entryHeater Keyless Entry Heated Seats Push Start Defogger Central Locking CoolBox Power Door Locks Navigation Power Steering Optional Navigation Power Windows Front Camera Power Mirrors Rear Camera Power Boot Rear Central Control Cup Holders Rear Folding Seat Arm Rest Rear Headrest YesHandbrake Center LeverRear Wiper Interior Lighting Seat Material Type Leather seat with manual adjustmentFront Power Outlet Steering Adjustment Rear Power Outlet Steering Switches ",
            "category": "Cars",
            "sub_cat": "Corolla",
            "price": "4859000.00",
            "quantity": "39",
            "image": "https://cache1.pakwheels.com/system/car_generation_pictures/5361/original/Corolla-X-Cars-Cropped-Pictures-for-Website.jpg?1606903674"
        },
        {
            "title": "KENWOOD KRF-24457GDMRG TWO DOOR NON INVERTER",
            "description": "Item Condition: New&#10;Shipping Info: 24 - 48 Hours&#10;Stock Info: Available&#10;warranty: THREE YEARS COMPRESSOR, ONE YEAR PARTS & SERVICE                                                     Colour / Material          RED",
            "category": "Refrigerator",
            "sub_cat": "Kenwood",
            "price": "52899.00",
            "quantity": "56",
            "image": "https://www.mega.pk/items_images/KENWOOD+KRF-24457GDMRG+TWO+DOOR+NON+INVERTER+Price+in+Pakistan%2C+Specifications%2C+Features%2C+Reviews_-_22456.webp"
        },
        {
            "title": "Haier Top Mount Refrigerator 368EBD",
            "description": "Features&#10;&#10;Full Electric Solution (FES)&#10;Best Performance&#10;Door Hinge: Right&#10;Fast Cooling&#10;Intelligent Function&#10; &#10;&#10;Specifications&#10;&#10;Top Mount&#10;R134a Refrigerant&#10;Direct Cool&#10;Free Standing&#10;Conventional&#10;Gold Color&#10;No.of Crispers in Fridge: 1&#10;Color of Crispers in Fridge: Transparent&#10;No.of Shelves in Fridge: 3&#10;Type of Shelves in Fridge: Wire&#10;No.of Shelves in Freezer: 2&#10;No. of Racks in Fridge Door: 4&#10;No.of Racks in Freezer Door: 2&#10;No. of Egg Racks: 2",
            "category": "Refrigerator",
            "sub_cat": "Haier",
            "price": "55700.00",
            "quantity": "28",
            "image": "https://www.alfatah.com.pk/wp-content/uploads/2020/07/haier-368ebd-refrigerator.jpg"
        },
        {
            "title": "Haier Top Mount Refrigerator 368EPC-W",
            "description": "Features&#10;&#10;Right Door Hinge&#10;Fast Cooling&#10;Transparent Color of Crispers in Fridge&#10;Lighting&#10;Intelligent Function&#10;Glass Shelves&#10; &#10;&#10;Specifications&#10;&#10;Top Mount&#10;Direct Cool&#10;R134a Refrigerant&#10;Free Standing&#10;No.of Crispers in Fridge: 1&#10;No.of Shelves in Fridge: 3&#10;No.of Shelves in Freezer: 2&#10;No. of Racks in Fridge Door: 4&#10;No.of Racks in Freezer Door: 2&#10;No. of Egg Racks: 2",
            "category": "Refrigerator",
            "sub_cat": "Haier",
            "price": "59999.00",
            "quantity": "8",
            "image": "https://www.alfatah.com.pk/wp-content/uploads/2021/07/Untitled-1-5.png"
        }
    ]


class Command(BaseCommand):
    # Show this when the user types help
    help = "Create Role and its permissions"

    # A command must define handle()
    def handle(self, *args, **options):
        for item in PRODUCTS:
            title = item.get('title')
            price = Decimal(item.get('price')).quantize(Decimal('.01'))
            image= item.get('image')
            description = item.get("description") 
            category = item.get('category')
            
            quantity= random.randint(2, 100)
            store = random.randint(1,3)
            cat, create = Category.objects.get_or_create(title = category)
            user = UserAccount.objects.get(pk=store)

            if user is not None:
                product, create = Product.objects.get_or_create(name=title, vendor = user, title= title, description= description, category=cat,price= price, quantity= quantity, image= image )
                product.save()
                print (product)