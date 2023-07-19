from django.core.exceptions import ValidationError
from django.test import TestCase

from lost_and_found.objects_posts.models import Post, Object


#  Arrange, Act, Assert

class PhoneTests(TestCase):
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

    def test_create_when_valid_expect_to_be_created(self):
        post = self._create_post(self.VALID_POST_DATA)
        post.full_clean()
        post.save()

        self.assertIsNotNone(post.pk)

    def test_create_when_phone_is_none_expect_exception(self):
        invalid_data = {
            'author_phone': None,
        }
        post = self._create_post(self.VALID_POST_DATA, **invalid_data)

        with self.assertRaises(ValidationError):
            # Needed explicit call in tests
            post.full_clean()

    def test_create_when_phone_dont_start_with_0_or_plus_expect_exception(self):
        invalid_data = {
            'author_phone': '1' + self.VALID_POST_DATA['author_phone'][1:],
        }
        post = self._create_post(self.VALID_POST_DATA, **invalid_data)

        with self.assertRaises(ValidationError):
            # Needed explicit call in tests
            post.full_clean()

    def test_create_when_title_has_1_more_than_valid_chars(self):
        post = self._create_post(self.VALID_POST_DATA, title='t' * Post.MAX_TITLE_LEN + 't')

        with self.assertRaises(ValidationError):
            # Needed explicit call in tests
            post.full_clean()
