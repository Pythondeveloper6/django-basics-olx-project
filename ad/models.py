from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

AD_CONDITION = (
    ('New','New'),
    ('i','LikeNew'),
    ('Good Condition','GoodCondition'),
    ('Bad Condition','BadCondition'),
)



class Ad(models.Model):
    code = models.CharField(max_length=12,blank=True, null=True)
    owner = models.ForeignKey(User,related_name='ad_owner', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField( upload_to='ad/')
    content = models.TextField(max_length=1000)
    price = models.IntegerField(default=1)
    category = models.ForeignKey('Category',limit_choices_to={'main_category':True},related_name='ad_category', on_delete=models.CASCADE)
    condition = models.CharField(max_length=15,choices=AD_CONDITION,blank=True, null=True)
    brand = models.ForeignKey('Brand', related_name='ad_brand',blank=True, null=True, on_delete=models.CASCADE)
    views_count = models.IntegerField(default=0)
    trending = models.BooleanField(default=False)
    liked_users = models.ManyToManyField(User, blank=True, null=True)

    def save(self, *args, **kwargs): 
        ## logic
        self.code = '##'+((str(self.id)).center(10,'0'))
        super(Ad, self).save(*args, **kwargs) 


    def __str__(self):
        return self.name



class Comment(models.Model):
    author = models.ForeignKey(User, related_name='comment_author', on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, related_name='comment_product', on_delete=models.CASCADE)
    comment = models.TextField(max_length=100)
    created_at =  models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = ("Comment")
        verbose_name_plural = ("Comments")
        ordering = ('-created_at',)

    def __str__(self):
        return str(self.ad)






class AdImages(models.Model):
    ad = models.ForeignKey(Ad, related_name='ad_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='ad_images/')



class Category(models.Model):
    name = models.CharField(max_length=50)
    main_category = models.ForeignKey('self', limit_choices_to={'main_category':None},related_name='maincategory', on_delete=models.CASCADE , blank=True, null=True)
    image = models.CharField(max_length=20)

    ## relation sub category 

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name




class Order(models.Model):
    user = models.ForeignKey(User,related_name='order_owner', on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, related_name='order_product', on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    

    class Meta:
        verbose_name = ("Order")
        verbose_name_plural = ("Orders")

    def __str__(self):
        return str(self.ad)
