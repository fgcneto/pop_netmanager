from pop_erp.apps.core.list_descriptors import \
    search_list_descriptors_by_application
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
from django.shortcuts import render


@login_required
@cache_page(60)
def index(request):
    return render(request,
                  'netmanager/index.html',
                  {'extend': 'netmanager/menu_sidebar.html'})


@login_required
def listar(request):
    s1 = request.path.split("/")
    context = search_list_descriptors_by_application(
        s1[len(s1) - 2], s1[len(s1) - 1])
    return render(request, 'core/list.html', context)
