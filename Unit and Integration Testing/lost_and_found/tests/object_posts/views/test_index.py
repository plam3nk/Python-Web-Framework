from django.test import TestCase
from django.urls import reverse

from lost_and_found.objects_posts.models import Object, Post


class IndexViewTest(TestCase):
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

    def _create_post(self, data, **kwargs):
        obj = Object.objects.create(**self.VALID_OBJ_DATA)
        post_data = {
            **data,
            **kwargs,
            'object': obj,
        }
        return Post(**post_data)

    def test_index__when_no_posts__expect_empty_posts(self):
        response = self.client.get(
            reverse('index'),
        )

        context = response.context

        self.assertEqual(200, response.status_code)
        self.assertEqual(0, len(context['posts']))

        self.assertTemplateUsed(response, 'index.html')

    def test_index__when_single_posts__expect_single_posts(self):
        # Arrange
        # Set up DB
        post = self._create_post(self.VALID_POST_DATA)
        post.save()

        # Act
        response = self.client.get(
            reverse('index'),
        )

        # Assert
        context = response.context

        self.assertEqual(200, response.status_code)
        self.assertEqual(1, len(context['posts']))

        self.assertTemplateUsed(response, 'index.html')
