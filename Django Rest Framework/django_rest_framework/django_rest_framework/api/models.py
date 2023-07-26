from django.db import models


# Create your models here.

class Author(models.Model):
    first_name = models.CharField(
        max_length=30,
    )

    last_name = models.CharField(
        max_length=30,
    )

    followers_count = models.IntegerField()

    def increment_followers(self):
        self.followers_count += 1
        self.save()

# # Create
# author = Author(first_name='Plamen', last_name='Kostov')
#
# # Update
# author.first_name = 'Ivan'
#
# # Delete
#
# author.delete()
#
# # Read
# author
#
# # Action
# author.increment_followers()
