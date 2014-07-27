from django.contrib import admin
from models import Avatar, Region

class AvatarAdmin(admin.ModelAdmin):
    pass

class RegionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Avatar, AvatarAdmin)
admin.site.register(Region, RegionAdmin)