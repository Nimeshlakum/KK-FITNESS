from django.urls import path
from myapp.views import *

app_name = 'myapp'

urlpatterns = [


    path("",login_page),
    path("login/",user_login),
    path("logout/",user_logout),
    path("registration/",user_registration),


    path("admin_login_page/",admin_login_page),
    path("admin_login/",admin_login_),
    path("admin_logout/",admin_logout),


    path("admin_home/",admin_home),
    path("admin_add_product/",admin_add_product),
    path("admin_member/",admin_member,name='admin_member'),
    path("admin_membership/",admin_membership),
    path("admin_message/",admin_message,name='admin_message'),
    path("admin_order/",admin_order),
    path("admin_trinaer/",admin_trinaer),
    path("admin_yoga_class/",admin_yoga_class),


    path("user_home/",user_user_home),
    path("about_us/",user_about_us),
    path("contact_us/",user_contact_us),
    path("user_profile/",user_profile),
    path("order/",user_order),
    path("product/",user_product),
    path("membership/",user_membership),
    path("yoga_class/",user_yoga_class),
    path("home_product_order/<int:id>",product_order),
    path("home_product_cart_order/",product_cart_order),
    path("adduser/",adduser),
    path("usermessage/",proble),


    path("addtrainer/",addtrainer),
    path("addmembership/",addmembership),
    path("addproduct/",addproduct),
    path("addyogaclass/",addyogaclass),
    path("addadmin/",addadmin),


    path("usercart/",usercart),
    path("addproducttocart/<int:id>",addproducttocart),


    path('delete_user/<int:id>',del_user, name='del_user'),
    path('delete_message/<int:id>',del_message, name='del_message'),
    path('delete_trainer/<int:id>',del_trainer, name='del_trainer'),
    path('delete_product/<int:id>',del_product, name='del_product'),
    path('delete_membership/<int:id>',del_membership, name='del_membership'),
    path('delete_yoga_class/<int:id>',del_yoga_class, name='del_yoga_class'),
    path('delete_admin/<int:id>',del_admin, name='del_admin'),
    path('delete_cart_item/<int:id>',del_cart_item, name='del_cart_item'),


    path('edit_admin/<int:id>',edit_admin, name='edit_admin'),
    path('edit_trianer/<int:id>',edit_trainer, name='edit_trainer'),
    path('edit_product/<int:id>',edit_product, name='edit_product'),
    path('edit_membership/<int:id>',edit_membership, name='edit_membership'),
    path('edit_yoga/<int:id>',edit_yoga, name='edit_yoga'),


    path('update_admin/<int:id>',update_admin, name='update_admin'),
    path('update_product/<int:id>',update_product, name='update_product'),
    path('update_trainer/<int:id>',update_trainer, name='update_trainer'),
    path('update_memberhip/<int:id>',update_membership, name='update_membership'),
    path('update_yoga_class/<int:id>',update_yoga, name='update_yoga'),


    path('add_to_cart/',add_to_cart,name="add-to_cart"),
    path('purchase_membership/<int:id>',purchase_membership,name='purchase_membership'),
    path('book_yoga_class/<int:id>',book_yoga_class,name='book_yoga_class'),
    path('user_purchase_membership/',user_purchase_membership,name='user_purchase_membership'),
    path('yoga_class_members/',yoga_class_members,name='yoga_class_members'),
    path('user_product_order/',user_product_order,name='user_product_order'),

]
