import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'json_image_extractor.settings')

application = get_wsgi_application()
