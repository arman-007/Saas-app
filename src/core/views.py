from django.http import HttpResponse
from django.shortcuts import render

from visits.models import PageVisits


def home_page_view(request, *args, **kwargs):
    qs = PageVisits.objects.all()
    page_visit_qs = PageVisits.objects.filter(path=request.path)
    context = {
        "page_title" : "HomePage",
        "page_visit_count" : page_visit_qs.count(),
        "percent_page_visit" : (page_visit_qs.count() * 100) / qs.count(),
        "total_visit_count" : qs.count(),
    }
    html_template = "home.html"
    PageVisits.objects.create(
        path=request.path
    )
    return render(request, html_template, context)