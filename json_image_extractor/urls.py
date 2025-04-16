from django.contrib import admin
from django.urls import path
from api.views import ExtractJSONFromImageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/extract-data/', ExtractJSONFromImageView.as_view(), name='extract-data'),
]
