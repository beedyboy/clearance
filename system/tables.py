import django_tables2 as tables
from .models import FacultyData
from django_tables2.utils import A # alias for accessor


class FacultyTable(tables.Table):
    edit_Action = tables.LinkColumn('system:fac_link_edit', text='Edit', args=[A('pk')], attrs={'a':{'class':'btn btn-info btn-sm'}, 'td':{'align': 'center'}}, orderable=False)
    view_Action = tables.LinkColumn('system:fac_link_view', text='View', args=[A('pk')], attrs={'a':{'class':'btn btn-primary btn-sm'}, 'td':{'align': 'center'}}, orderable=False)
    class Meta:
        model = FacultyData
        attrs = {'class':'table table-responsive','border': '2'}
        exclude = { 'id', }
        template_name = 'django_tables2/bootstrap4.html'