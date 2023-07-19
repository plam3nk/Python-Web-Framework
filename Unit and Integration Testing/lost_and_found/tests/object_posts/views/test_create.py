from django.test import TestCase
from django.urls import reverse

from lost_and_found.objects_posts.models import Object, Post


class CreateViewTest(TestCase):
    VALID_POST_DATA = {
        'title': 'Lost',
        'description': 'Lost again',
        'author_name': 'TestUser',
        'author_phone': '+359888888'
    }
    VALID_OBJ_DATA = {
        'name': 'Custom object',
        'image': 'http://customobject.com',
        'width': 15,
        'height': 20,
        'weight': 25
    }

    def test_create_post__when_valid__expect_to_be_created(self):
        # Act
        response = self.client.post(
            reverse('create'),
            data={
                **self.VALID_POST_DATA,
                **self.VALID_OBJ_DATA,
            }
        )

        # Assert
        post = Post.objects.get(
            **self.VALID_POST_DATA
        )
        obj = Object.objects.get(
            **self.VALID_OBJ_DATA,
            pk=post.object_id,
        )

        self.assertEqual(302, response.status_code)
        self.assertIsNotNone(post)
        self.assertIsNotNone(obj)