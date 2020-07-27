from django.contrib import admin

# Register your models here.


from .models import Ad , Category , AdImages , Brand


class AdAdmin(admin.ModelAdmin):
    list_display = ('code','name','price','views_count')
    list_filter = ('category','brand','condition')
    search_fields = ('name','content')






admin.site.register(Ad , AdAdmin)
admin.site.register(Category)
admin.site.register(AdImages)
admin.site.register(Brand)