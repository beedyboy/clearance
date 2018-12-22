import django_tables2 as tables
from .models import FacultyData


class FacultyTable(tables.Table):
    class Meta:
        model = FacultyData
        template_name = 'django_tables2/bootstrap.html'