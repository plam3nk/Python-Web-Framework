import time

from celery import shared_task


@shared_task
def example_background_job():
    print('background_job started')
    time.sleep(5)
    print('background_job ended')


# In our app
# example_background_job()

# With Celery
# example_background_job.delay()
