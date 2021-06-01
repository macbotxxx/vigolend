from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from .models import UserAddress

# from vigolend.users.forms import UserChangeForm, UserCreationForm

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'country_of_residence','account_type','date_joined','last_login')
    list_display_links = ('first_name', 'last_name', 'country_of_residence','account_type','date_joined','last_login')

@admin.register(UserAddress)
class UserAddresssAdmin(admin.ModelAdmin):
    list_display = ('user', 'address_line_1', 'address_line_2', 'state', 'city', 'zip_post_code', 'country')
    list_display_links = ('user', 'address_line_1', 'address_line_2', 'state', 'city', 'zip_post_code', 'country')