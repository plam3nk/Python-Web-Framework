import pyperclip
from django.shortcuts import render, redirect, resolve_url
from django.urls import reverse
from pyperclip import copy

from petstagram.common.forms import PhotoCommentForm
from petstagram.common.models import PhotoLike
from petstagram.common.utils import get_user_liked_photos, get_photo_url
from petstagram.photos.models import Photo


def apply_likes_count(photo):
    photo.likes_count = photo.photolike_set.count()

    return photo


def apply_user_liked_photo(photo):
    # TODO: fix this for user when authentication is available.
    photo.is_liked_by_user = photo.likes_count > 0

    return photo


def index(request):
    photos = [apply_likes_count(photo) for photo in Photo.objects.all()]
    photos = [apply_user_liked_photo(photo) for photo in photos]

    context = {
        'photos': photos,
        'comment_form': PhotoCommentForm(),
    }
    return render(
        request,
        template_name='common/home-page.html',
        context=context
    )


def like_photo(request, photo_id):
    user_liked_photos = get_user_liked_photos(photo_id)
    if user_liked_photos:
        user_liked_photos.delete()
    else:
        # Method 2
        PhotoLike.objects.create(
            photo_id=photo_id,
        )

        return redirect(get_photo_url(request, photo_id))

    return redirect('index')

    # Method 1
    # photo_like = PhotoLike(
    #     photo_id=photo_id,
    # )
    # photo_like.save()

    # Method 3 'Wrong - additional call to DB'
    # Correct, only if validation is needed
    # photo = Photo.objects.get(pk=photo_id)
    # PhotoLike.objects.create(
    #     photo=photo
    # )


def share_photo(request, photo_id):
    photo_details_url = reverse('photo-details', kwargs={
        'pk': photo_id
    })
    # pyperclip.copy(redirect(get_photo_url(request, photo_id)))
    return redirect(get_photo_url(request, photo_id))


def comment_photo(request, photo_id):
    pass
