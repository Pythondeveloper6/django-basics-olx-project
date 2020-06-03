from django.contrib import admin

# Register your models here.


from .models import Ad , Category , AdImages




admin.site.register(Ad)
admin.site.register(Category)
admin.site.register(AdImages)