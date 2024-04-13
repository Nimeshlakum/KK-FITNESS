from django.shortcuts import render , HttpResponse , get_list_or_404
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import *
from django.contrib import messages
from myapp.forms import *

#user login !!!
def user_login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            use = users.objects.get(username=username)
            if use.password==password:
                login(request, use)
                return render(request,'core/user_home_page.html')  
            else:
                messages.error(request, 'Invalid username or password.')
                return render(request,'core/login_page.html')  
        except:
            messages.error(request, 'Invalid username or password.')
            return render(request,'core/login_page.html')
            
    return render(request,'core/login_page.html')

# def user_login(request):
#     if request.method=="POST":        
#         username = request.POST["username"]
#         password = request.POST["password"]
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             messages.success(request,"Login Successful")
#             return render(request,'core/user_home_page.html') 
#         else:
#             messages.error(request,"Invalid Credentials")
#             return render(request,'core/login_page.html')  
               
#     return render(request,'core/login_page.html')

#admin login !!!
def admin_login_(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            admi = admins.objects.get(username=username)
            if admi.password==password:
                login(request, admi)
                return render(request,'core/admin_home_page.html')  
            else:
                messages.error(request, 'Invalid username or password.')
                return render(request,'core/admin_login_page.html')  
        except:
            messages.error(request, 'Invalid username or password.')
            return render(request,'core/admin_login_page.html')
            
    return render(request,'core/admin_login_page.html')

#user logout !!!
def user_logout(request):
    logout(request)
    return render(request,'core/login_page.html')

#admin logout !!!
def admin_logout(request):
    logout(request)
    return render(request,'core/admin_login_page.html')

#admin login_page !!!
def admin_login_page(request):
    return render(request,'core/admin_login_page.html')

#userr login_page !!!
def login_page(request):
    return render(request,'core/login_page.html')

#admin home-page !!!
def admin_home(request):
    admin_detail = admins.objects.all()
    return render(request,'core/admin_home_page.html',{'admin_detail':admin_detail})

#admin add-product-page !!!
def admin_add_product(request):
    pproduct = product.objects.all()
    return render(request,'core/admin_add_product_page.html',{'pproduct':pproduct})

#admin member-page !!!
def admin_member(request):
    member = membership_holders.objects.all()
    # yoga_member_ = yoga_class_member.objects.all()
    return render(request,'core/admin_member_page.html',{'member':member})

#admin membership-page !!!
def admin_membership(request):
    mmembership = membership.objects.all()
    return render(request,'core/admin_membership_page.html',{'mmembership':mmembership})

#admin message-page !!!
def admin_message(request):
    mess = message.objects.all()
    return render(request,'core/admin_message_page.html',{'mess':mess})

#admin order-page !!!
def admin_order(request):
    order_d = userorder.objects.all()
    return render(request,'core/admin_order_page.html',{'order_d':order_d})

#admin trainer-page !!!
def admin_trinaer(request):
    tra = trianer.objects.all()
    return render(request,'core/admin_trainer_page.html',{'tra':tra})

#admin yoga-page !!!
def admin_yoga_class(request):
    yoga_detail = yoga_class.objects.all()
    return render(request,'core/admin_yoga_class_page.html',{'yoga_detail' : yoga_detail})

#user regisrtation-page !!!
def user_registration(request):
    return render(request,'core/registration_page.html')

#user home-page !!!
def user_user_home(request):
    review = message.objects.all()
    membershipd= membership.objects.all()

    combine = {
        'review':review,
        'membershipd':membershipd,
    }
    return render(request,'core/user_home_page.html',combine)

#user about-us-page !!!
def user_about_us(request):
    return render(request,'core/user_about_page.html')

#user contact_us-page !!!
def user_contact_us(request):
    return render(request,'core/user_contact_page.html')

#user profile
def user_profile(request):
    return render(request,'core/user_profile.html')

#user membership-page !!!
def user_membership(request):
    m_detail = membership.objects.all()
    return render(request,'core/user_membership_page.html',{'m_detail':m_detail})

#user order-page !!!
def user_order(request):
    order_detail = userorder.objects.all()
    return render(request,'core/user_order_page.html',{'order_detail':order_detail})

#user product-page !!!
def user_product(request):
    p_detail = product.objects.all()
    return render(request,'core/user_product_page.html',{'p_detail':p_detail})

#user yoga-class-page !!!
def user_yoga_class(request):
    y_detail = yoga_class.objects.all()
    return render(request,'core/user_yoga_class_page.html',{'y_detail':y_detail})

#user product_order-page !!!
def product_order(request,id):
    order_detail = product.objects.get(id=id);
    combine = {
        'order_detail':order_detail,
    }
   
    return render(request,'core/home_product_order.html',{'combine':combine})

#user product_cart-page !!!
def product_cart_order(request):
    cart_detail = cart.objects.all()
    return render(request,'core/user_product_cart_order.html',{'cart_detail':cart_detail})

#admin edit-admin-page !!!
def edit_admin(request,id):
    adm_d = admins.objects.get(id=id)
    return render(request,'core/admin_admin_edit.html',{'adm_d':adm_d})

#admin edit_product-page !!!
def edit_product(request,id):
    pro_d = product.objects.get(id=id)
    return render(request,'core/admin_product_edit.html',{'pro_d':pro_d})

#admin edit_trainer-page !!!
def edit_trainer(request,id):
    tri_d = trianer.objects.get(id=id)
    return render(request,'core/admin_trainer_edit.html',{'tri_d':tri_d})

#admin edit_membership-page !!!
def edit_membership(request,id):
    me_d = membership.objects.get(id=id)
    return render(request,'core/admin_membership_edit.html',{'me_d':me_d})

#admin edit_yoga-page !!!
def edit_yoga(request,id):
    yoga_d = yoga_class.objects.get(id=id)
    return render(request,'core/admin_yoga_edit.html',{'yoga_d':yoga_d})

#user cart-page !!!
def usercart(request):
    cart_detail = cart.objects.all()
    return render(request,'core/user_cart.html',{'cart_detail':cart_detail})

#user product-cart-order-page !!!
def product_cart_order(request):
    cart_detail = cart.objects.all()
    return render(request,'core/user_product_cart_order.html',{'cart_detail':cart_detail})

#user add-proudct-to-cart-page !!!
def addproducttocart(request,id):
    cart_item = product.objects.get(id=id)
    cart_item = cart(product_id=id ,product_name=cart_item.name ,product_price=cart_item.price ,product_quantity=cart_item.quantity)
    cart.save(cart_item)
    return render(request,'core/user_home_page.html')

#user add-new-user-page !!!
def adduser(request):
    if request.method == 'POST':
        user_form = userform(request.POST)
        user = user_form.save()
        user.save()
        return render(request,'core/login_page.html',{'user_form':user_form})

#user problem(message)-page !!! 
def proble(request):
    if request.method == 'POST':
        contact_form = contactform(request.POST)
        message = contact_form.save()
        message.save()
    return render(request,'core/user_home_page.html',{'contact_form': contact_form})

#admin add-trainer-page !!!
def addtrainer(request):
    if request.method == 'POST':
        trainer_add_form = trainerform(request.POST)
        trianer = trainer_add_form.save()
        trianer.save()
        return render(request,'core/admin_trainer_page.html',{'trainer_add_form':trainer_add_form})     

#admin add-product-page !!!
def addproduct(request):
    if request.method == 'POST':
        product_form = productform(request.POST)
        product = product_form.save()
        product.save()
        return render(request,'core/admin_add_product_page.html',{'product_form':product_form})     

#admin add-membership-page !!!
def addmembership(request):
    if request.method == 'POST':
        membership_form = membershipform(request.POST)
        membership = membership_form.save()
        membership.save()
        return render(request,'core/admin_membership_page.html',{'membership_form':membership_form}) 
#admin add-yoga-class-page !!! 
def addyogaclass(request):
    if request.method == 'POST':
        yoga_class_form = yogaclassform(request.POST)
        yoga_class = yoga_class_form.save()
        yoga_class.save()
        return render(request,'core/admin_yoga_class_page.html',{'yoga_class_form':yoga_class_form}) 
    
#admin add-admin-page !!!
def addadmin(request):
    if request.method == 'POST':
        admin_form = adminform(request.POST)
        admin = admin_form.save()
        admin.save()
        return render(request,'core/admin_home_page.html',{'admin_form':admin_form}) 

#admin delete-user-page !!!
def del_user(request,id):
    dele_user = users.objects.get(id=id)
    dele_user.delete()
    return render(request,'core/admin_member_page.html') 

#admin delete message-page !!!
def del_message(request,id):
    del_message = message.objects.get(id=id)
    del_message.delete()
    return render(request,'core/admin_message_page.html') 

#admin delete-trainer-page !!!
def del_trainer(request,id):
    del_trianer = trianer.objects.get(id=id)
    del_trianer.delete()
    return render(request,'core/admin_trainer_page.html') 

#admin delete-product-page !!!
def del_product(request,id):
    del_product = product.objects.get(id=id)
    del_product.delete()
    return render(request,'core/admin_add_product_page.html') 

#admin delete-membership-page !!!
def del_membership(request,id):
    del_membership = membership.objects.get(id=id)
    del_membership.delete()
    return render(request,'core/admin_membership_page.html') 

#admin deldet-yoga-class-page !!!
def del_yoga_class(request,id):
    del_yoga_class_ = yoga_class.objects.get(id=id)
    del_yoga_class_.delete()
    return render(request,'core/admin_yoga_class_page.html')

#admin delete-admin-page !!!
def del_admin(request,id):
    del_admin_ = admins.objects.get(id=id)
    del_admin_.delete()
    return render(request,'core/admin_home_page.html')

#user delete-cart-item-page !!!
def del_cart_item(request,id):
    del_cart_item_ = cart.objects.get(id=id)
    del_cart_item_.delete()
    return render(request,'core/user_cart.html')

#admin update-admin-page !!!
def update_admin(request,id):
    Admin_ = admins.objects.get(id=id)
    form = adminform(request.POST, instance=Admin_)
    form.save()
    return render(request,'core/admin_home_page.html',{'Admin_':Admin_})

#admin update-product-page !!!
def update_product(request,id):
    product_ = product.objects.get(id=id)
    form = productform(request.POST, instance=product_)
    form.save()
    return render(request,'core/admin_product_page.html',{'product_':product_})

#admin update-trainer-page !!!
def update_trainer(request,id):
    trainer_ = trianer.objects.get(id=id)
    form = trainerform(request.POST, instance=trainer_)
    form.save()
    return render(request,'core/admin_trainer_page.html',{'trainer_':trainer_})

#admin update-membership-page !!!
def update_membership(request,id):
    membership_ = membership.objects.get(id=id)
    form = membershipform(request.POST, instance=membership_)
    form.save()
    return render(request,'core/admin_membership_page.html',{'membership_':membership_})

#admin update-yoga-classs-page !!!
def update_yoga(request,id):
    yoga_ = yoga_class.objects.get(id=id)
    form = yogaclassform(request.POST, instance=yoga_)
    form.save()
    return render(request,'core/admin_yoga_class_page.html',{'yoga_':yoga_})

#admin -page !!!
def add_to_cart(request):
    return render(request,'core/user_home_page.html')

#user purchase-membership-page !!!
def purchase_membership(request,id):
    membership_detail = membership.objects.get(id=id)
    return render(request,'core/purchase_membership.html',{'membership_detail':membership_detail})

#user book-yoga-class-page !!!
def book_yoga_class(request,id):
    yoga_class_detail = yoga_class.objects.get(id=id)
    return render(request,'core/book_yoga.html',{'yoga_class_detail':yoga_class_detail})

#user purchase-membership !!!
def user_purchase_membership(request):
    if request.method == 'POST':
        del_mem_order = userpurchasemembership(request.POST)
        membership_holders = del_mem_order.save()
        membership_holders.save()
    return render(request,'core/purchase_membership.html')

#user book-yoga-class-page !!!
def yoga_class_members(request):
    if request.method == 'POST':
        del_class_book = yogaclassbookmember(request.POST)
        yoga_class_member = del_class_book.save()
        yoga_class_member.save()
    return render(request,'core/book_yoga.html')

#user product-order-page !!!
def user_product_order(request):
    if request.method == 'POST':
        del_product_order = userorderform(request.POST)
        userorder = del_product_order.save()
        userorder.save()
    return render(request,'core/user_order_page.html')

