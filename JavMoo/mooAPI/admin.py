from django.contrib import admin
from .models import Actress,Category,CategoryGroup
class ActressAdmin(admin.ModelAdmin):
    list_display = ('name','age','uuid')
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('categoryName','uuid','group')
class CategoryGroupAdmin(admin.ModelAdmin):
    list_display = ('groupName',)

admin.site.register(Actress,ActressAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(CategoryGroup,CategoryGroupAdmin)
# Register your models here.
