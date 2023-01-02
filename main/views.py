from django.shortcuts import render
from django.http import JsonResponse
from main.models import *
from django.shortcuts import redirect
import requests
# Create your views here.

def indexHandler(request):
    cats = Category.objects.all()
    services = Service.objects.all()
    infos = Info.objects.all()
    contact = Contact.objects.all()[:1]
    blogs = Blog.objects.all()
    cart_items = []
    new_cart = None

    user_session_id = request.session.session_key
    if user_session_id:
        open_carts = Cart.objects.filter(session_id=user_session_id).filter(status=0)
        if open_carts:
            new_cart = open_carts[0]
            cart_items = CartItem.objects.filter(cart_id=new_cart.id).filter(status=0)


    return render(request, 'index-3.html', {
        'cats': cats,
        'new_cart': new_cart,
        'cart_items': cart_items,
        'services': services,
        'infos': infos,
        'contact': contact,
        'blogs': blogs,
                                          })

def aboutHandler(request):
    cats = Category.objects.all()
    about = About.objects.all()[:1]
    contact = Contact.objects.all()[:1]
    members = Member.objects.all()[:4]
    cart_items = []
    new_cart = None

    user_session_id = request.session.session_key
    if user_session_id:
        open_carts = Cart.objects.filter(session_id=user_session_id).filter(status=0)
        if open_carts:
            new_cart = open_carts[0]
            cart_items = CartItem.objects.filter(cart_id=new_cart.id).filter(status=0)


    return render(request, 'about.html', {
        'cats': cats,
        'new_cart': new_cart,
        'cart_items': cart_items,
        'about': about,
        'contact': contact,
        'members': members,
                                          })

def contactHandler(request):

    if request.POST:
        message = Message()
        message.name = request.POST.get('name', '')
        message.phone = request.POST.get('phone', '')
        message.message = request.POST.get('message', '')
        message.save()

    cats = Category.objects.all()
    contact = Contact.objects.all()[:1]

    cart_items = []
    new_cart = None

    user_session_id = request.session.session_key
    if user_session_id:
        open_carts = Cart.objects.filter(session_id=user_session_id).filter(status=0)
        if open_carts:
            new_cart = open_carts[0]
            cart_items = CartItem.objects.filter(cart_id=new_cart.id).filter(status=0)

    return render(request, 'contact.html', {
        'cats': cats,
        'contact': contact,
        'new_cart': new_cart,
        'cart_items': cart_items,

    })



def blogHandler(request):
    cats = Category.objects.all()
    blogs = Blog.objects.all()
    contact = Contact.objects.all()[:1]
    cart_items = []
    new_cart = None

    user_session_id = request.session.session_key
    if user_session_id:
        open_carts = Cart.objects.filter(session_id=user_session_id).filter(status=0)
        if open_carts:
            new_cart = open_carts[0]
            cart_items = CartItem.objects.filter(cart_id=new_cart.id).filter(status=0)

    return render(request, 'blog.html', {
        'cats': cats,
        'new_cart': new_cart,
        'contact': contact,
        'cart_items': cart_items,
        'blogs': blogs,

                                          })

def blogItemHandler(request,blog_id):
    cats = Category.objects.all()
    blog = Blog.objects.get(id = blog_id)
    contact = Contact.objects.all()[:1]
    blogs = Blog.objects.all()
    cart_items = []
    new_cart = None

    user_session_id = request.session.session_key
    if user_session_id:
        open_carts = Cart.objects.filter(session_id=user_session_id).filter(status=0)
        if open_carts:
            new_cart = open_carts[0]
            cart_items = CartItem.objects.filter(cart_id=new_cart.id).filter(status=0)


    return render(request, 'blog-details.html', {
        'cats': cats,
        'new_cart': new_cart,
        'cart_items': cart_items,
        'blog': blog,
        'contact': contact,
        'blogs': blogs,

    })

def catalogHandler(request):
    goods = Good.objects.all()
    contact = Contact.objects.all()[:1]
    cats = Category.objects.all()


    active_cats = request.GET.getlist('active_cat', [])
    active_cats = [int(i) for i in active_cats]
    tovar_count = 0
    if active_cats:
        new_goods = []
        for g in goods:
            if g.category.id in active_cats:
                new_goods.append(g)
        tovar_count = len(new_goods)
        goods = new_goods

    new_cart = None
    cart_items = []
    wish_list = []

    user_session_id = request.session.session_key
    if user_session_id:
        open_carts = Cart.objects.filter(session_id=user_session_id).filter(status=0)
        if open_carts:
            new_cart = open_carts[0]
            cart_items = CartItem.objects.filter(cart__id=new_cart.id).filter(status=0)
        wish_list = WishItem.objects.filter(session_id=user_session_id)



    return render(request, 'shop.html', {
        'goods': goods,
        'tovar_count': tovar_count,
        'cats': cats,
        'active_cats': active_cats,
        'new_cart': new_cart,
        'cart_items': cart_items,
        'contact': contact,
        'wish_list': wish_list,
                                          })

def catalogItemHandler(request, good_id):

    good = Good.objects.get(id= good_id)
    related_goods = Good.objects.filter(category__id=good.category.id).exclude(id=good_id)
    cats = Category.objects.all()
    contact = Contact.objects.all()[:1]
    new_cart = None
    cart_items = []
    wish_list = []

    user_session_id = request.session.session_key
    if user_session_id:
        open_carts = Cart.objects.filter(session_id=user_session_id).filter(status=0)
        if open_carts:
            new_cart = open_carts[0]
            cart_items = CartItem.objects.filter(cart__id=new_cart.id).filter(status=0)
        wish_list = WishItem.objects.filter(session_id=user_session_id)
    return render(request, 'product-details.html', {
        'cats': cats,
        'new_cart': new_cart,
        'contact': contact,
        'cart_items': cart_items,
        'wish_list': wish_list,
        'good': good,
        'related_goods': related_goods,
                                          })

def wishHandler(request):
    cats = Category.objects.all()
    contact = Contact.objects.all()[:1]
    new_cart = None
    cart_items = []
    wish_list = []

    user_session_id = request.session.session_key
    if user_session_id:
        open_carts = Cart.objects.filter(session_id=user_session_id).filter(status=0)
        if open_carts:
            new_cart = open_carts[0]
            cart_items = CartItem.objects.filter(cart__id=new_cart.id).filter(status=0)
        wish_list = WishItem.objects.filter(session_id=user_session_id)
    return render(request, 'wishlist.html', {
        'cats': cats,
        'new_cart': new_cart,
        'cart_items': cart_items,
        'wish_list': wish_list,
        'contact': contact,
                                          })


def cartHandler(request):
    contact = Contact.objects.all()[:1]
    cats = Category.objects.all()
    if not request.session.session_key:
        request.session.create()
    user_session_id = request.session.session_key
    open_carts = Cart.objects.filter(session_id=user_session_id).filter(status=0)
    new_cart = None
    if open_carts:

        new_cart = open_carts[0]
    else:
        new_cart = Cart()
        new_cart.session_id = user_session_id
        new_cart.save()

    if request.POST:
        return_url = request.POST.get('return_url', '')
        action = request.POST.get('action', '')

        if action == 'add_to_cart':
            good_id = int(request.POST.get('good_id', 0))
            amount = float(request.POST.get('amount', 0))
            cart_items = CartItem.objects.filter(cart__id=new_cart.id).filter(status=0).filter(good__id=good_id)

            if cart_items:
                new_cart_item = cart_items[0]
                new_cart_item.amount = new_cart_item.amount + amount
                new_cart_item.all_price = new_cart_item.price * new_cart_item.amount
                new_cart_item.save()
            else:
                new_cart_item = CartItem()
                new_cart_item.good_id = good_id
                new_cart_item.cart_id = new_cart.id
                new_cart_item.amount = amount
                new_cart_item.price = new_cart_item.good.price
                new_cart_item.all_price = new_cart_item.price * new_cart_item.amount
                new_cart_item.save()

        if action == 'remove_from_cart':
            good_id = int(request.POST.get('good_id', 0))
            cart_items = CartItem.objects.filter(cart__id=new_cart.id).filter(status=0).filter(good__id=good_id)
            for ci in cart_items:
                ci.delete()

        if action == 'clear_cart':
            cart_items = CartItem.objects.filter(cart__id=new_cart.id).filter(status=0)
            for ci in cart_items:
                ci.delete()

        if action == 'checkout':
            new_cart.first_name = request.POST.get('first_name', '')
            new_cart.last_name = request.POST.get('last_name', '')
            new_cart.city = request.POST.get('city', '')
            new_cart.phone = request.POST.get('phone', '')
            new_cart.created_at = datetime.now()
            new_cart.status = 1
            new_cart.save()

        if action == 'accepted':
            order_id = int(request.POST.get('order_id', 0))
            if request.user.is_authenticated:
                main_order = Cart.objects.get(id=order_id)
                if main_order:
                    main_order.status = 2
                    main_order.save()

        if action == 'add_to_wish_list':
            good_id = int(request.POST.get('good_id',0))
            wishItems = WishItem.objects.filter(good__id=good_id).filter(session_id=user_session_id)
            if wishItems:
                pass
            else:
                wish_item = WishItem()
                wish_item.session_id = user_session_id
                wish_item.good_id = good_id
                wish_item.save()


        if action == 'remove_from_wish_list':
            good_id = int(request.POST.get('good_id', 0))
            wish_items = WishItem.objects.filter(good__id=good_id).filter(session_id=user_session_id)
            if wish_items:
                for wi in wish_items:
                    wi.delete()


        if action in ['add_to_cart', 'remove_from_cart', 'clear_cart']:
            cart_items = CartItem.objects.filter(cart__id=new_cart.id).filter(status=0)
            all_price = 0
            all_amount = 0
            all_orig_price = 0
            if cart_items:
                for ci in cart_items:
                    all_amount += ci.amount
                    all_orig_price += ci.amount * ci.price

            new_cart.orig_price = all_orig_price

            all_price = all_orig_price # * (100 - new_cart.discount) / 100
            new_cart.amount = all_amount
            new_cart.orig_price = all_orig_price
            new_cart.price = all_price
            new_cart.save()

        if return_url:
            return redirect(return_url)

    cart_items = CartItem.objects.filter(cart__id=new_cart.id).filter(status=0)

    return render(request, 'cart.html', {
        'cats': cats,
        'new_cart': new_cart,
        'cart_items': cart_items,
        'contact': contact,
    })

def checkoutHandler(request):
    contact = Contact.objects.all()[:1]
    cats = Category.objects.all()
    new_cart = None
    cart_items = []
    user_session_id = request.session.session_key
    if user_session_id:
        open_carts = Cart.objects.filter(session_id=user_session_id).filter(status=0)
        if open_carts:
            new_cart = open_carts[0]
            cart_items = CartItem.objects.filter(cart__id=new_cart.id).filter(status=0)

    return render(request, 'checkout.html', {
        'cats': cats,
        'new_cart': new_cart,
        'cart_items': cart_items,
        'contact': contact,

    })


def checkoutSuccessHandler(request):
    cats = Category.objects.all()
    contact = Contact.objects.all()[:1]
    new_cart = None
    cart_items = []
    user_session_id = request.session.session_key
    if user_session_id:
        open_carts = Cart.objects.filter(session_id=user_session_id).filter(status=0)
        if open_carts:
            new_cart = open_carts[0]
            cart_items = CartItem.objects.filter(cart__id=new_cart.id).filter(status=0)

    return render(request, 'checkout_success.html', {
        'cats': cats,
        'new_cart': new_cart,
        'cart_items': cart_items,
        'contact': contact,

    })