from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.core.paginator import Paginator
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import razorpay

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def animals(request):
    return render(request, 'animals.html')


def dog(request):
    # Fetch the products including additional information
    products = Products.objects.filter(category='Dog')

    # Define the number of items to display per page
    items_per_page = 4

    page_number = request.GET.get('page')  # Get the page number from the query parameters

    paginator = Paginator(products, items_per_page)
    page = paginator.get_page(page_number)

    page_range = 5
    if page.number <= page_range // 2:
        pages = range(1, page_range + 1)
    elif page.number >= paginator.num_pages - page_range // 2:
        pages = range(paginator.num_pages - page_range + 1, paginator.num_pages + 1)
    else:
        pages = range(page.number - page_range // 2, page.number + page_range // 2 + 1)

    context = {
        'prop': page,
        'page_range': pages,
    }

    return render(request, 'dog.html', context)

def cat(request):
    # Fetch the products for cats
    cats = Products.objects.filter(category='Cat')  # Assuming you have a 'category' field for differentiation

    # Define the number of items to display per page
    items_per_page = 4

    page_number = request.GET.get('page')  # Get the page number from the query parameters

    paginator = Paginator(cats, items_per_page)
    page = paginator.get_page(page_number)

    page_range = 5
    if page.number <= page_range // 2:
        pages = range(1, page_range + 1)
    elif page.number >= paginator.num_pages - page_range // 2:
        pages = range(paginator.num_pages - page_range + 1, paginator.num_pages + 1)
    else:
        pages = range(page.number - page_range // 2, page.number + page_range // 2 + 1)

    context = {
        'cats': page,
        'page_range': pages,
    }

    return render(request, 'cat.html', context)

def birds(request):
    # Fetch the products for birds
    birds = Products.objects.filter(category='Birds').order_by('id')  # Assuming 'Bird' is the category for bird products

    # Define the number of items to display per page
    items_per_page = 4

    page_number = request.GET.get('page')  # Get the page number from the query parameters

    paginator = Paginator(birds, items_per_page)
    page = paginator.get_page(page_number)

    page_range = 5
    if page.number <= page_range // 2:
        pages = range(1, page_range + 1)
    elif page.number >= paginator.num_pages - page_range // 2:
        pages = range(paginator.num_pages - page_range + 1, paginator.num_pages + 1)
    else:
        pages = range(page.number - page_range // 2, page.number + page_range // 2 + 1)

    context = {
        'prop': page,
        'page_range': pages,
    }

    return render(request, 'birds.html', context)

def rabbit(request):
    # Fetch the products for rabbits
    rabbits = Products.objects.filter(category='Rabbit').order_by('id')
    # Define the number of items to display per page
    items_per_page = 4

    page_number = request.GET.get('page')  # Get the page number from the query parameters

    paginator = Paginator(rabbits, items_per_page)  # Use 'rabbits' for pagination
    page = paginator.get_page(page_number)

    page_range = 5
    if page.number <= page_range // 2:
        pages = range(1, page_range + 1)
    elif page.number >= paginator.num_pages - page_range // 2:
        pages = range(paginator.num_pages - page_range + 1, paginator.num_pages + 1)
    else:
        pages = range(page.number - page_range // 2, page.number + page_range // 2 + 1)

    context = {
        'rabbits': page,  # Use 'page' for pagination
        'page_range': pages,
    }

    return render(request, 'rabbit.html', context)

def fish(request):
    # Fetch the fish products including additional information
    fishes = Products.objects.filter(category='Fish').order_by('id')
    # Define the number of items to display per page
    items_per_page = 4

    page_number = request.GET.get('page')  # Get the page number from the query parameters

    paginator = Paginator(fishes, items_per_page)  # Change 'products' to 'fishes'
    page = paginator.get_page(page_number)

    page_range = 5
    if page.number <= page_range // 2:
        pages = range(1, page_range + 1)
    elif page.number >= paginator.num_pages - page_range // 2:
        pages = range(paginator.num_pages - page_range + 1, paginator.num_pages + 1)
    else:
        pages = range(page.number - page_range // 2, page.number + page_range // 2 + 1)

    context = {
        'fishes': page,  # Assuming 'prop' is used in your template
        'page_range': pages,
    }

    return render(request, 'fishes.html', context)


def accessories(request):
    # Fetch the accessories products including additional information
    accessories = Products.objects.filter(category='Accessory')  # Fetch all accessories

    items_per_page = 4
    page_number = request.GET.get('page')  # Get the page number from the query parameters

    paginator = Paginator(accessories, items_per_page)  # Use 'accessories' for pagination
    page = paginator.get_page(page_number)

    page_range = 5
    if page.number <= page_range // 2:
        pages = range(1, page_range + 1)
    elif page.number >= paginator.num_pages - page_range // 2:
        pages = range(paginator.num_pages - page_range + 1, paginator.num_pages + 1)
    else:
        pages = range(page.number - page_range // 2, page.number + page_range // 2 + 1)

    context = {
        'accessories': page,  # Use 'page' for pagination
        'page_range': pages,
    }

    return render(request, 'accessories.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Create and save a new ContactMessage instance to the database
            ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            return redirect('success_page')  # Redirect to the success page after submission
    else:
        form = ContactForm()

    return render(request, 'contact_us.html', {'form': form})


def success(request):
    return render(request, 'success.html')


def privacy_policy(request):
    # You can add your privacy policy logic here if needed
    return render(request, 'privacy_policy.html')


def terms_of_service(request):
    # You can add your terms of service logic here if needed
    return render(request, 'terms_of_service.html')


def faqs(request):
    # Retrieve FAQs from the database

    return render(request, 'faqs.html', {'faqs': faqs})


from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account for {username} created Successfully')
            return redirect('profile')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})
@login_required
def profile(request):
    return render(request, 'profile.html')
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # This will save the product to the database
            return redirect('product_list')  # Redirect to a page displaying the list of products
    else:
        form = ProductForm()

    return render(request, 'add_product.html', {'form': form})

def product_list(request):
    # Fetch all products
    all_products = Products.objects.all()

    # Define the number of items to display per page
    items_per_page = 20

    page_number = request.GET.get('page')

    paginator = Paginator(all_products, items_per_page)
    page = paginator.get_page(page_number)

    # Calculate the page range for pagination links
    page_range = 5
    if page.number <= page_range // 2:
        pages = range(1, page_range + 1)
    elif page.number >= paginator.num_pages - page_range // 2:
        pages = range(paginator.num_pages - page_range + 1, paginator.num_pages + 1)
    else:
        pages = range(page.number - page_range // 2, page.number + page_range // 2 + 1)

    context = {
        'products': page,
        'page_range': pages,
    }

    return render(request, 'product_list.html', context)

@login_required
def change_password(request):
    if request.method == 'POST':
        new_password1 = request.POST['new_password1']
        new_password2 = request.POST['new_password2']

        if new_password1 == new_password2:
            user = request.user
            user.set_password(new_password1)
            user.save()

            # Update the session to reflect the password change
            update_session_auth_hash(request, user)

            messages.success(request, 'Your password has been changed successfully.')
        else:
            messages.error(request, 'Passwords do not match.')

    return render(request, 'profile.html')

def checkout(request):
    if request.method == 'POST':
        order_amount = 50000
        order_currency = 'INR'
        client = razorpay.Client(auth=('rzp_test_hntieMJ65xzBmL','xqCsAZu62cAWRqIWdnnVnj28'))
        payment = client.order.create({'amount':order_amount,'currency':order_currency,'payment_capture':'1' })
        return render(request,"payment/checkout.html",{'payment':payment})
    return render(request,"payment/checkout.html")


@csrf_exempt
def payment_sucess(request):
    return render(request,"payment/success.html")