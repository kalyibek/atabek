from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from . import models, forms

def show_all_med_img(request):
    med_img_shows = models.MedicalShows.objects.all()
    context = {
        'shows': med_img_shows
    }
    return render(request, 'index.html', context)


def med_shows_detail(request, id):
    show = get_object_or_404(models.MedicalShows, id=id)
    context = {
        'show': show
    }
    return render(request, 'detail.html', context)


def add_medshows(request):
    if request.method == 'POST':
        form = forms.ShowForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('medshows'))

    form = forms.ShowForm()
    context = {
        'form': form
    }

    return render(request, "add.html", context)


def show_update(request, id):
    show_object = get_object_or_404(models.MedicalShows, id=id)

    if request.method == 'POST':
        form = forms.ShowForm(instance=show_object, data=request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('medshows'))

    form = forms.ShowForm(instance=show_object)
    context = {
        'form': form,
        'object': show_object
    }

    return render(request, 'update.html', context)


def delete_medshow(request, id):
    show = get_object_or_404(models.MedicalShows, id=id)
    show.delete()

    return HttpResponseRedirect(reverse('medshows'))
