from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Product
import datetime
from django.urls import path
from django.contrib.auth.decorators import login_required

# View Functions
def index(request):
    if request.method == "POST":
        if request.POST.get("login_s"):
            return redirect("login")
        if request.POST.get("register_s"):
            return redirect("register")
    else:
        return render(request, "index.html")


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("search")
        else:
            messages.info(
                request, "The Username and/or Password entered are incorrect!"
            )
            return redirect("login")
    else:
        return render(request, "login.html")


def register(request):
    if request.method == "POST":
        fname = request.POST["f_name"]
        lname = request.POST["l_name"]
        username = request.POST["username"]
        password = request.POST["pass"]
        verifypass = request.POST["confirmpass"]
        email = request.POST["email"]

        if password == verifypass:
            # User is the thing being imported, filter goes in the db and checks
            # if the email entered already exists.
            if User.objects.filter(email=email).exists():
                messages.info(
                    request, "Email already in use! Please go back and log in!"
                )
                # Send em back to register
                return redirect("register")
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username not available! Try a different one!")
                return redirect("register")
            else:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                    first_name=fname,
                    last_name=lname,
                )
                user.save()
                return redirect("login")
        else:
            messages.info(request, "Passwords did not match!")
            return redirect("register")

    else:
        return render(request, "register.html")


@login_required
def search(request):
    return render(request, "search.html")


@login_required
def product(request, pk):
    a = 2


@login_required
def search_results(request):
    p1 = Product(
        img_src="https://cache.mrporter.com/variants/images/30629810019697407/in/w358_q60.jpg",
        listing_id=1,
        category="Men's Jacket",
        title="Gucci Sweater",
        current_auction_price=69.98,
        time_created="23h:42m:15s",
    )
    p2 = Product(
        img_src="https://ca.louisvuitton.com/images/is/image/HKN44WUSO618_PM2_Front%20view",
        listing_id=2,
        category="Men's Sweater",
        title="LV Sweater",
        current_auction_price=122.12,
        time_created="22m:44s",
    )
    p3 = Product(
        img_src="https://i.pinimg.com/originals/04/7b/7c/047b7cb4a8ce00ab8174824e1c8625de.jpg",
        category="Men's Hoodies",
        title="OVO Hoodie",
        current_auction_price=1322.12,
        time_created="03h:22m:44s",
    )
    p4 = Product(
        img_src="https://eu.louisvuitton.com/images/is/image/HHD20WQJQ631_PM2_Front%20view",
        category="Men's Jeans",
        title="LV Jeans",
        current_auction_price=61.08,
        time_created="03h:42m:25s",
    )
    p5 = Product(
        img_src="https://cdn.shopify.com/s/files/1/2482/7148/products/Bape_Classic_Shark_Tee_BlackGrey_2048x2048.jpg?v=1567473485",
        category="Men's Shirt",
        title="Bape Shirt",
        current_auction_price=123.28,
        time_created="13h:02m:00s",
    )
    p6 = Product(
        img_src="https://media.gucci.com/style/DarkGray_Center_0_0_800x800/1576864808/522514_Z402L_4635_001_100_0000_Light-GG-velvet-jacket.jpg",
        category="Men's Blazer",
        title="Gucci Blazer",
        current_auction_price=869.98,
        time_created="00h:00m:15s",
    )
    p7 = Product(
        img_src="https://img.ihahabags.ru/202107/s-886722-prada-sweater-long-sleeved-for-unisex.jpg",
        category="Men's Sweater",
        title="Prada Sweater",
        current_auction_price=1001.28,
        time_created="13h:42m:19s",
    )

    products = [p1, p2, p3, p4, p5, p6, p7]

    context = {"products": products}

    return render(request, "search_results.html", context)


@login_required
def profile(request):
    return render(request, "profile.html")
