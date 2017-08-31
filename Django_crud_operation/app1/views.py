import urllib
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from models import people_detail
from django.contrib import messages


def index(request, template="index2.html"):

    context = {}
    username = request.GET.get('account_username_search')
    start_date = request.GET.get('adjustment_start_date')
    print start_date
    warning_message = ""

    people_detail_list = people_detail.objects.all()
    if username:
        people_detail_list = people_detail_list.filter(id=username)
        context['st_account'] = username
    if start_date:
        people_detail_list = people_detail_list.filter(start_date__gte=start_date)
    people_detail_list = people_detail_list.order_by('-start_date')
    paginator = Paginator(people_detail_list, 10)
    page = request.GET.get('page')
    try:
        people_records = paginator.page(page)
    except PageNotAnInteger:
        people_records = paginator.page(1)
    except EmptyPage:
        people_records = paginator.page(paginator.num_pages)
    query_params = request.GET.dict()
    if query_params.has_key("page"):
        del query_params["page"]

    if not people_records:
        warning_message = "No Results found!!!"

    context['people_records'] = people_records
    context['start_date'] = start_date
    context['warning_message'] = warning_message
    context['query_string'] = urllib.urlencode(query_params)
    all_adjustment_accounts = people_detail.objects.all()\
                                        .values_list('id', "username")\
                                        .distinct()
    context['all_adjustment_accounts'] = dict(all_adjustment_accounts)
    return render(request, template, context)


def add_new_record(request, template="adjustment.html"):
    """
    this is for add new account record on people account model
    """
    if request.method == "POST":
        add_username = request.POST.get('username')
        start_date = request.POST.get('add_new_date')
        add_fullname = request.POST.get('fullname')
        add_state = request.POST.get('state')
        add_country = request.POST.get('country')
        add_city = request.POST.get('fullname')
        add_age = request.POST.get('age')
        people_detail.objects.create(username=add_username,
                                  age=add_age,
                                  fullname=add_fullname,
                                  city=add_city, state=add_state,
                                  start_date=start_date, country=add_country)

        messages.add_message(request, messages.SUCCESS, "Record for added successfully")
    return redirect('index')