from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def nPage(request):
    if request.method == "POST":
        title = request.POST.get('quantity')
        text = request.POST.get('text')
        for entry in util.list_entries():
            if title == entry:
                return render(request, "encyclopedia/Createnewpage.html", {
                        "message": "Entry Already Exists"
                })
        util.save_entry(title, text)
    return render(request, "encyclopedia/Createnewpage.html")

