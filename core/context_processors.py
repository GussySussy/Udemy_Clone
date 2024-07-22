from courses.models import Category

def global_context(request):
    return {
        'global_categories'  : Category.objects.all()
    }