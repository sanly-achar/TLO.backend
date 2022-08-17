from django.shortcuts import render, redirect
from .models import *
from .forms import *


def index(request):

    slider = Slider.objects.all()
    main_page = MainPageImage.objects.all()
    info = Info.objects.all()
    news = News.objects.all()
    new_product = Product.objects.filter(new=True)
    sale_product = Product.objects.filter(sale=True)
    category = Category.objects.all()
    contact = Contacts.objects.all()

    form = ContactUsForm()
    if request.method=="POST":
        form=ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')



    context = {
        'slider':slider,
        'main_page': main_page,
        'info':info,
        'form':form,
        'news':news,
        'new_product':new_product,
        'sale_product':sale_product,
        'category':category,
        'contact':contact,
    }
    print(main_page)

    
    return render(request, 'content/ru/index.html', context)


def about_us(request):

    about = About.objects.all()
    category = Category.objects.all()
    contact = Contacts.objects.all()


    context = {
        'about':about,
        'category':category,
        'contact':contact,


    }

    return render(request, 'content/ru/about_us.html', context)




def product(request):

    category = Category.objects.all()
    contact = Contacts.objects.all()


    context = {
        'category':category,
        'contact':contact,

    }
    print(category)
    
    return render(request, 'content/ru/product.html', context)


def single_product(request, id):

    product = Product.objects.filter(category=id)
    category = Category.objects.all()
    contact = Contacts.objects.all()

    

    # form = ProductContactUsForm()
    # if request.method=="POST":
    #     form=ContactUsForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('index')

    form = None
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        product_id = request.POST.get('product_id')
        message = request.POST.get('message')

        if zip(name, phone_number, email):
            form = ProductContactUs.objects.create(name=name, phone=phone_number, email=email, product_id=product_id, message=message )
            return redirect('index')




    context = {
        'product':product,
        'form':form,
        'contact':contact,
        'category':category,

    }
    print(product)
    return render(request, 'content/ru/product_detail.html', context)



def contact(request):
    contact = Contacts.objects.all()
    category = Category.objects.all()
    contact = Contacts.objects.all()


    form = None
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        product_id = request.POST.get('product_id')
        message = request.POST.get('message')
        if zip(name, phone_number, email):
            form = ContactUs.objects.create(name=name, phone=phone_number, email=email, message=message,)
            return redirect('index')




    context = {
        'contact':contact,
        'category':category,
        'form':form,
        'category':category,



    }

    return render(request, 'content/ru/contact.html', context)
    


