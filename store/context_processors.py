from .models import CATEGORY_CHOICES

def add_variable_to_context(request):
    categories = CATEGORY_CHOICES
    return {
        'categories': categories,
    }