from django.contrib import admin

# Register your models here.


from .models import Ad , Category , AdImages , Brand




admin.site.register(Ad)
admin.site.register(Category)
admin.site.register(AdImages)
admin.site.register(Brand)