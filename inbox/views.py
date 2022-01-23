from django.shortcuts import render
from inbox.forms import formMessage
from django.shortcuts import render
from django.http.response import *
from django.db.models import Q
from projects.models import * 

def index(request):

    search = request.POST.get("search")

    projects = post.objects.all().order_by("created",)


    if search:
        projects = post.objects.filter(
            Q(title__icontains = search)
        ).distinct()

    data = {
        'form': formMessage()
    }

    if request.method == 'POST':

        formulario = formMessage(data=request.POST)
        if formulario.is_valid():

            formulario.save()
            data["mensaje"] = "Your message was sent successfully. We will contact you soon."

        else:
            data["form"] = formulario

    return render(request, 'index.html', {'data' :data, 'projects':projects})