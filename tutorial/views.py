from django.http import JsonResponse
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import People


class Index(ListView):
    model = People
    template_name = "people_list.html"


class PeopleDetailView(DetailView):
    model = People
    template_name = "people_detail.html"

    def render_to_response(self, context, **response_kwargs):
        p = context['object']
        return JsonResponse({"name": p.name})
