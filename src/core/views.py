from django.http import HttpResponse
from django.shortcuts import render

from visits.models import PageVisits


def home_page_view(request, *args, **kwargs):
    if request.user.is_authenticated:
        print(request.user.first_name)
    qs = PageVisits.objects.all()
    page_visit_qs = PageVisits.objects.filter(path=request.path)
    try:
        percent  = (page_visit_qs.count() * 100) / qs.count()
    except:
        percent = 0
    context = {
        "page_title" : "HomePage",
        "page_visit_count" : page_visit_qs.count(),
        "percent_page_visit" : percent,
        "total_visit_count" : qs.count(),
    }
    html_template = "home.html"
    PageVisits.objects.create(
        path=request.path
    )
    return render(request, html_template, context)

def about_view(request, *args, **kwargs):
    qs = PageVisits.objects.all()
    page_visit_qs = PageVisits.objects.filter(path=request.path)
    try:
        percent  = (page_visit_qs.count() * 100) / qs.count()
    except:
        percent = 0
    context = {
        "page_title" : "About US",
        "page_visit_count" : page_visit_qs.count(),
        "percent_page_visit" : percent,
        "total_visit_count" : qs.count(),
    }
    html_template = "home.html"
    PageVisits.objects.create(
        path=request.path
    )
    return render(request, html_template, context)