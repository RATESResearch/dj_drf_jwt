from django.apps import AppConfig
from dj_drf_jwt.settings import *

class DjangoDrfJwtConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dj_drf_jwt'
    
