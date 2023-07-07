from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from petstagram.common.utils import get_user_liked_photos
from petstagram.photos.forms import PhotoCreateForm, PhotoEditForm, PhotoDeleteForm
from petstagram.photos.models import Photo


# Create your views here.

# photo_add, photo_details, photo_edit
@login_required
def photo_details(request, pk):
    photo = Photo.objects.filter(pk=pk) \
        .get()

    context = {
        'photo': photo,
        'has_user_liked_photo': get_user_liked_photos(pk),
        'likes_count': photo.photolike_set.count(),
    }

    return render(
        request,
        template_name='photos/photo-details-page.html',
        context=context,
    )


def get_post_photo_form(request, form, success_url, template_path, pk=None):
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(success_url)

    context = {
        'form': form,
        'pk': pk,
    }

    return render(
        request,
        template_path,
        context
    )


@login_required
def photo_add(request):
    if request.method == 'GET':
        form = PhotoCreateForm()
    else:
        form = PhotoCreateForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save()  # forms.save() returns the object saved.
            return redirect('photo-details', pk=photo.pk)

    context = {
        'form': form,
    }

    return render(
        request,
        template_name='photos/photo-add-page.html',
        context=context
    )


@login_required
def photo_edit(request, pk):
    photo = Photo.objects.filter(pk=pk) \
        .get()

    return get_post_photo_form(
        request,
        PhotoEditForm(request.POST or None, instance=photo),
        success_url=reverse('index'),
        template_path='photos/photo-edit-page.html',
        pk=pk,
    )


@login_required
def photo_delete(request, pk):
    photo = Photo.objects.filter(pk=pk) \
        .get()

    return get_post_photo_form(
        request,
        PhotoDeleteForm(request.POST or None, instance=photo),
        success_url=reverse('index'),
        template_path='photos/photo-delete-page.html',
        pk=pk,
    )
