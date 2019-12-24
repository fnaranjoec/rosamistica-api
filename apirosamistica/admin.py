from django.contrib import admin
from . import models


from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


#from .forms import CustomUserCreationForm, CustomUserChangeForm
#from .models import CustomUser

"""
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'cellphone']


admin.site.register(CustomUser, CustomUserAdmin)
"""


# Register your models here.
#admin.site.register(models.Tblpersona)




###############################  VISTAS ###########
#admin.site.register(models.Vwclientecreditos)



###############################  STORE PROCEDURES ###########
#admin.site.register(models.SPMenu)




