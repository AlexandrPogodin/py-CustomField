from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound

from .models import List
from .forms import ListForm


def index(request):
    form = ListForm()
    lists = List.objects.all().order_by('-id')
    all_lists = []
    for list in lists:
        list_info = {
            'id': list.id,
            'list': list.list,
        }
        all_lists.append(list_info)
    list = ''
    if len(all_lists) > 0:
        list = all_lists[0]
        list = list['list']
        newlist = list.replace(' ', '')
        newlist = newlist.split(',')
        print(newlist)
        for i in len(newlist):
            newlist[i] = int(newlist[i])
        print(newlist)
    context = {'list': newlist, 'form': form}
    return render(request, 'listvalid/index.html', context)


def save(request):
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('home')
