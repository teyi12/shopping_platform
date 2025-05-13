from .models import Category

def categories_dropdown(request):
    return {'categories': Category.objects.all()}
