from .models import Category



def get_main_categories(request):
    main_category = Category.objects.filter(main_category=None)
    return {'main_category' : main_category}