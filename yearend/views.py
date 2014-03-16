from django.shortcuts import render
from django.http import HttpResponseRedirect
import forms

from models import FamilyResponse, ChildResponse

# Create your views here.


def page1(request):
    family = _get_family(request.session.session_key)
    if request.method == 'POST':  # If the form has been submitted...
        # A form bound to the POST data
        form = forms.FamilyOverviewForm(request.POST, instance=family)
        if form.is_valid():  # All validation rules pass
            form.save()
            # Redirect after POST
            return HttpResponseRedirect('/yearend/p2?c=1')
    else:
        if family.how_many_children > 0:
            return HttpResponseRedirect('/yearend/thanks')

        # An unbound form, except for the rest of the model
        form = forms.FamilyOverviewForm(instance=family)

    context = {'display_form': form}
    return render(request, 'yearend/page1.html', context)


def page2(request):
    child = _get_child(request.session.session_key, request.GET['c'])

    if request.method == 'POST':  # If the form has been submitted...
        # A form bound to the POST data
        form = forms.ChildIntialForm(request.POST, instance=child)
        if form.is_valid():  # All validation rules pass
            form.save()
            # Redirect after POST
            return HttpResponseRedirect('/yearend/p3?c={}'.format(request.GET['c']))
    else:
        # An unbound form, except for the rest of the model
        form = forms.ChildIntialForm(instance=child)

    context = {'display_form': form}
    return render(request, 'yearend/page1.html', context)


def page3(request):
    child = _get_child(request.session.session_key, request.GET['c'])

    if request.method == 'POST':  # If the form has been submitted...
        # A form bound to the POST data
        form = forms.ChildUsefulForm(request.POST, instance=child)
        if form.is_valid():  # All validation rules pass
            form.save()
            # Redirect after POST
            return HttpResponseRedirect('/yearend/p4?c={}'.format(request.GET['c']))
    else:
        # An unbound form, except for the rest of the model
        form = forms.ChildUsefulForm(instance=child)

    context = {'display_form': form}
    return render(request, 'yearend/page1.html', context)


def page4(request):
    child = _get_child(request.session.session_key, request.GET['c'])

    if request.method == 'POST':  # If the form has been submitted...
        # A form bound to the POST data
        form = forms.ChildFollowForm(request.POST, instance=child)
        if form.is_valid():  # All validation rules pass
            form.save()
            # Redirect after POST
            return HttpResponseRedirect('/yearend/p5?c={}'.format(request.GET['c']))
    else:
        # An unbound form, except for the rest of the model
        form = forms.ChildFollowForm(instance=child)

    context = {'display_form': form}
    return render(request, 'yearend/page1.html', context)


def page5(request):
    child = _get_child(request.session.session_key, request.GET['c'])

    if request.method == 'POST':  # If the form has been submitted...
        # A form bound to the POST data
        form = forms.ChildCloseForm(request.POST, instance=child)
        if form.is_valid():  # All validation rules pass
            form.save()
            # Redirect after POST
            page_location = 'p6'
            family = _get_family(request.session.session_key)
            if family.how_many_children > child.child_index:
                page_location = 'p2?c={}'.format(int(request.GET['c']) + 1)

            return HttpResponseRedirect(page_location)
    else:
        # An unbound form, except for the rest of the model
        form = forms.ChildCloseForm(instance=child)

    context = {'display_form': form}
    return render(request, 'yearend/page1.html', context)

def page6(request):
    family = _get_family(request.session.session_key)
    if request.method == 'POST':  # If the form has been submitted...
        # A form bound to the POST data
        form = forms.FamilyCloseForm(request.POST, instance=family)
        if form.is_valid():  # All validation rules pass
            form.save()
            # Redirect after POST
            return HttpResponseRedirect('/yearend/p1')
    else:
        # An unbound form, except for the rest of the model
        form = forms.FamilyCloseForm(instance=family)

    context = {'display_form': form}
    return render(request, 'yearend/page1.html', context)

def thanks(request):
    return render(request, 'yearend/thanks.html', {})

def _get_family(session_key):
    try:
        family = FamilyResponse.objects.get(session_key=session_key)
    except:
        family = FamilyResponse()
        family.session_key = session_key

    return family


def _get_child(session_key, child_index):
    family = _get_family(session_key)

    try:
        child = ChildResponse.objects.get(
            family_response=family, child_index=child_index)
    except:
        child = ChildResponse()
        child.family_response_id = family.id
        child.child_index = child_index

    return child
