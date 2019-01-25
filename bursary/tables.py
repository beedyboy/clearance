import django_tables2 as tables
from .models import SchoolFees
from django_tables2.utils import A # alias for accessor
#from django.utils.translation import gettext as _


class FeesTable(tables.Table):
    sid = tables.Column(verbose_name='Session Year')
    fid = tables.Column(verbose_name='Faculty')
    did = tables.Column(verbose_name='Department')
    amount = tables.Column(verbose_name='Total Amount(#)')
    edit_Action = tables.LinkColumn('bursary:edit_fee', text='Edit', args=[A('pk')], attrs={'a':{'class':'btn btn-info btn-sm'}, 'td':{'align': 'center'}}, orderable=False)
    #current = tables.LinkColumn('system:session_current', accessor=A('current'),  args=[A('pk')], attrs={'a':{'class':'btn btn-primary btn-sm'}, 'td':{'align': 'center'}}, orderable=False)
    class Meta:
        model = SchoolFees
        attrs = {'class':'table table-responsive','border': '2'}
        exclude = { 'id', }
        template_name = 'django_tables2/bootstrap4.html'

