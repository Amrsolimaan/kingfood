from django.shortcuts import render ,redirect,get_object_or_404
from .models import *
from django.core.mail import send_mail
from .forms import MessageForm

# views.py
from django.shortcuts import render, redirect
from .forms import MessageForm

def contact_view(request):
    products = product.objects.all()
    containers = container_of_five_product.objects.first()  # الحصول على جميع العناصر من container_of_five_product
    about = about_company.objects.first()
    contact_info = Contact.objects.all()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            # جمع البيانات من النموذج
            contact = form.save()  # حفظ البيانات في قاعدة البيانات
            return redirect('contact')  # إعادة التوجيه إلى صفحة النجاح
    else:
        form = MessageForm()
    context = {
        'products': products,
        'container': containers,  # تمرير جميع العناصر من container_of_five_product
        'about_': about,
        'contact_info': contact_info,
        'form': form
    }        
    return render(request, 'contact.html', context)



# ******************* HOME *******************


def home(request):
    products = product.objects.all().order_by('-id')[:4]
    containers = container_of_five_product.objects.first()  # الحصول على جميع العناصر من container_of_five_product
    about = about_company.objects.first()
    contact_info = Contact.objects.all()
    post_id = request.GET.get('products_id')
    posts_id = request.GET.get('container_of_five_product_id')

    if post_id:
        post = get_object_or_404(product, pk=post_id)
    elif posts_id:
        post = get_object_or_404(container_of_five_product, pk=posts_id)
    else:
        post = None

    context = {
        'products': products,
        'container': containers,  # تمرير جميع العناصر من container_of_five_product
        'about_': about,
        'contact_info': contact_info,
        'run': post,
    }
    
    return render(request, 'home.html', context)


# ************************************************************************************************


# ******************* ABOUT *******************

def about_views(request):
    products = product.objects.all()
    containers = container_of_five_product.objects.first()  # الحصول على جميع العناصر من container_of_five_product
    about = about_company.objects.first()
    contact_info = Contact.objects.all()
    Certificate = Certificates.objects.all()

    context = {
        'products': products,
        'container': containers,  # تمرير جميع العناصر من container_of_five_product
        'about_': about,
        'contact_info': contact_info,
        'Certificate': Certificate,
    }
    
    return render(request, 'about.html' ,context)


def shop_views(request):
    products = product.objects.all()
    containers = container_of_five_product.objects.first()  # الحصول على جميع العناصر من container_of_five_product
    about = about_company.objects.first()
    contact_info = Contact.objects.all()
    post_id = request.GET.get('products_id')

    if post_id:
        post = get_object_or_404(product, pk=post_id)
    else:
        post = None


    context = {
        'products': products,
        'container': containers,  # تمرير جميع العناصر من container_of_five_product
        'about_': about,
        'contact_info': contact_info,
        'post' : post,
    }
    
    return render(request, 'shop.html',context)

def product_views(request, id):
    products = product.objects.all()
    containers = container_of_five_product.objects.first()  # الحصول على جميع العناصر من container_of_five_product
    about = about_company.objects.first()
    contact_info = Contact.objects.all()

        
    post = get_object_or_404(product,pk=id)

    context = {
        'post': post,
        'products': products,
        'container': containers,  # تمرير جميع العناصر من container_of_five_product
        'about_': about,
        'contact_info': contact_info,        
    }
    return render(request, 'product.html', context)

def product5_views(request, id):
    posts = get_object_or_404(container_of_five_product,pk=id)
    products = product.objects.all()
    containers = container_of_five_product.objects.first()  # الحصول على جميع العناصر من container_of_five_product
    about = about_company.objects.first()
    contact_info = Contact.objects.all()
    
    context = {
        'posts': posts,
        'products': products,
        'container': containers,  # تمرير جميع العناصر من container_of_five_product
        'about_': about,
        'contact_info': contact_info,        
    }
    return render(request, 'product5.html', context)




def about_views(request):
    products = product.objects.all()
    containers = container_of_five_product.objects.first()  # الحصول على جميع العناصر من container_of_five_product
    about = about_company.objects.first()
    contact_info = Contact.objects.all()
    Certificate = Certificates.objects.all()

    context = {
        'products': products,
        'container': containers,  # تمرير جميع العناصر من container_of_five_product
        'about_': about,
        'contact_info': contact_info,
        'Certificate': Certificate,
    }
    
    return render(request, 'about.html' ,context)


def privacy_policy(request):
    products = product.objects.all()
    containers = container_of_five_product.objects.first()  # الحصول على جميع العناصر من container_of_five_product
    about = about_company.objects.first()
    contact_info = Contact.objects.all()
    Quality = quality.objects.all()
    post_id = request.GET.get('products_id')

    if post_id:
        post = get_object_or_404(product, pk=post_id)
    else:
        post = None


    context = {
        'products': products,
        'container': containers,  # تمرير جميع العناصر من container_of_five_product
        'about_': about,
        'contact_info': contact_info,
        'post' : post,
        'Quality' : Quality,
    }
    
    return render(request, 'privacy_policy.html',context)

