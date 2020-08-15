from .models import Footer



def get_footer(request):
    footer = Footer.objects.last()
    return {'footer': footer}