from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from markdown2 import Markdown
import markdown2
import random

from . import util

def index(request):
    if request.method == "POST":
        title = request.POST.get("q")

        if title not in util.list_entries():
            return render(request, "encyclopedia/index.html",{
                    "message": "Entry Not Found"
            })
        else:
            return HttpResponseRedirect(reverse('EntryPage', args=[title]))
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "random": random.choice(util.list_entries())
    })

def nPage(request):
    if request.method == "POST":
        title = request.POST.get('quantity')
        text = request.POST.get('text')

        if util.get_entry(title) != None or (not(title and title.strip())):
            return render(request, "encyclopedia/Createnewpage.html", {
                    "message": "Entry Is Wrong"
            })
        else:
            util.save_entry(title, text)

        return HttpResponseRedirect(reverse('EntryPage', args=[title]))
    return render(request, "encyclopedia/Createnewpage.html")

def ShowPage(request, entry):
    EntryContent = util.get_entry(entry)
    return render(request, 'encyclopedia/EntryPage.html',{
        "pageContent": EntryContent,
        "EntryTitle": entry
    })

def EditPage(request, entry):
    EntryContent = util.get_entry(entry)
    if request.method == "POST":
        content = request.POST.get('text')
        util.save_entry(entry, content)
        return HttpResponseRedirect(reverse('EntryPage', args=[entry]))
    return render(request, 'encyclopedia/EditEntry.html',{
        "pageContent": EntryContent,
        "Title": entry
    })       

