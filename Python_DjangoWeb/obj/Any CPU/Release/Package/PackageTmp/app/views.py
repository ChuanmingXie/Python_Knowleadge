"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from .models import conentList


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def detail(request):
    book_list = Book.objects.order_by('-pub_date')[:5]
    context = {'book_list': book_list}
    return render(request, 'lib/detail.html', context)



def knowleadge(request):
    """Renders the Knowledge page."""
    assert isinstance(request,HttpRequest)   
    list = conentList.objects.order_by('-edited_data')[:5]
    return render(
        request,
        'app/knowleadge.html',
        {
            'title':'章节列表',
            'contentlist': list,
            'year':datetime.now().year,
        }
    )

def createKnow(request):
    """Renders the Create Knowledge page."""
    assert isinstance(request,HttpRequest)
    context = {'title':'新建章节',}
    return render(request, 'app/createknow.html', context)

def detailKnow(request, id):
    """Renders the detial Knowledge page."""
    assert isinstance(request,HttpRequest)
    context = {'title':'章节详情',}
    return render(request, 'app/detailknow.html', context)

def editsKnow(request, id):
    """Renders the edits Knowledge page."""
    assert isinstance(request,HttpRequest)
    context = {'title':'编辑章节',}
    return render(request, 'app/editKnow.html', context)

def deleteKnow(request, id):
    """Renders the delete Knowledge page."""
    assert isinstance(request,HttpRequest)
    context = {'title':'删除章节',}
    return render(request, 'app/deleteKnow.html', context)



def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
