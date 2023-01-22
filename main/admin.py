from django.contrib import admin
from main.models import *
# Register your models here.



class AdminModelSingle(admin.ModelAdmin):
    pass


admin.site.register(Category, AdminModelSingle)
admin.site.register(Good, AdminModelSingle)
admin.site.register(Cart, AdminModelSingle)
admin.site.register(CartItem, AdminModelSingle)
admin.site.register(WishItem, AdminModelSingle)
admin.site.register(Contact, AdminModelSingle)
admin.site.register(Message, AdminModelSingle)
admin.site.register(Blog, AdminModelSingle)
admin.site.register(Service, AdminModelSingle)
admin.site.register(Member, AdminModelSingle)
admin.site.register(About, AdminModelSingle)
admin.site.register(Info, AdminModelSingle)
admin.site.register(Nagrada, AdminModelSingle)