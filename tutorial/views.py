from django.http import JsonResponse
from django.views.generic import ListView
from django.views.generic import DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import People


@method_decorator(login_required, name="dispatch")
class Index(ListView):
    model = People
    template_name = "people_list.html"


@method_decorator(login_required, name="dispatch")
class PeopleDetailView(DetailView):
    model = People
    template_name = "people_detail.html"

    def render_to_response(self, context, **response_kwargs):
        p = context['object']
        return JsonResponse({"name": p.name})
