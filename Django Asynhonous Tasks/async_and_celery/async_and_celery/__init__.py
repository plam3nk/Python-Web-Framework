from .celery import app as celery_app

__all__ = ('celery_app', )

'''
1. Install Celery
2. Register Celery in INSTALLED_APPS
3. Set BROKER_URL
4. Create 'celery.py'
5. Project's '__init__.py' register **celery**
6. Create 'shared_task'
'''