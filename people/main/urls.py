from django.urls import path
from .views import export_csv, home, import_csv

urlpatterns = [
    path('', home),
    path('import/', import_csv),
    path('export/', export_csv),
]
