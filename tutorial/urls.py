from django.conf.urls import url, include
from .views import Index, PeopleDetailView


urlpatterns = [
    url(r"^$", Index.as_view(), name="index"),
    url(r"^people/(?P<pk>\d+)/$", PeopleDetailView.as_view(), name="people")
]
