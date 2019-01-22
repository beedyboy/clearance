from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model

from .forms import UserAdminCreationForm, UserAdminChangeForm
# Register your models here.

User = get_user_model()

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(BaseUserAdmin):

    form = UserAdminChangeForm # edit view
    add_form = UserAdminCreationForm #create view
    inlines = [ProfileInline]
    # class Meta:
    #     model =User
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('user_id', 'first_name',  'last_name', 'admin', )
    list_filter = ('admin', 'staff', 'active')
    fieldsets = (
        (None, {'fields': ('user_id', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name',)}),
        ('Permissions', {'fields': ('admin', 'staff',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user_id', 'password1', 'password2', 'first_name', 'last_name',)}
         ),
    )

    search_fields = ('user_id', 'first_name')
    ordering = ('user_id',)
    filter_horizontal = ()
User = get_user_model()

admin.site.register(User, UserAdmin)