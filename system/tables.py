import django_tables2 as tables
from .models import FacultyData, DepartmentData, SessionData, SemesterData
from django_tables2.utils import A # alias for accessor


class FacultyTable(tables.Table):
    edit_Action = tables.LinkColumn('system:fac_link_edit', text='Edit', args=[A('pk')], attrs={'a':{'class':'btn btn-info btn-sm'}, 'td':{'align': 'center'}}, orderable=False)
    view_Action = tables.LinkColumn('system:fac_link_view', text='View', args=[A('pk')], attrs={'a':{'class':'btn btn-primary btn-sm'}, 'td':{'align': 'center'}}, orderable=False)
    class Meta:
        model = FacultyData
        attrs = {'class':'table table-responsive','border': '2'}
        exclude = { 'id', }
        template_name = 'django_tables2/bootstrap4.html'

class DepartmentTable(tables.Table):
    fid = tables.Column(verbose_name='Faculty')
    dept_name = tables.Column(verbose_name='Department')
    edit_Action = tables.LinkColumn('system:fac_link_edit', text='Edit', args=[A('pk')], attrs={'a':{'class':'btn btn-info btn-sm'}, 'td':{'align': 'center'}}, orderable=False)
    view_Action = tables.LinkColumn('system:fac_link_view', text='View', args=[A('pk')], attrs={'a':{'class':'btn btn-primary btn-sm'}, 'td':{'align': 'center'}}, orderable=False)
    class Meta:
        model = DepartmentData
        attrs = {'class':'table table-responsive','border': '2'}
        exclude = { 'id', }

class SessionTable(tables.Table):
    session_name = tables.Column(verbose_name='Session Year')
    edit_Action = tables.LinkColumn('system:session_edit', text='Edit', args=[A('pk')], attrs={'a':{'class':'btn btn-info btn-sm'}, 'td':{'align': 'center'}}, orderable=False)
    #Eview_Action = tables.LinkColumn('system:fac_link_view', text='View', args=[A('pk')], attrs={'a':{'class':'btn btn-primary btn-sm'}, 'td':{'align': 'center'}}, orderable=False)
    class Meta:
        model = SessionData
        attrs = {'class':'table table-responsive','border': '2'}
        exclude = { 'id', }
        template_name = 'django_tables2/bootstrap4.html'


class SemesterTable(tables.Table):
    sid = tables.Column(verbose_name='Session')
    semester_name = tables.Column(verbose_name='Semester')
    edit_Action = tables.LinkColumn('system:fac_link_edit', text='Edit', args=[A('pk')], attrs={'a':{'class':'btn btn-info btn-sm'}, 'td':{'align': 'center'}}, orderable=False)
    #view_Action = tables.LinkColumn('system:fac_link_view', text='View', args=[A('pk')], attrs={'a':{'class':'btn btn-primary btn-sm'}, 'td':{'align': 'center'}}, orderable=False)
    class Meta:
        model = SemesterData
        attrs = {'class':'table table-responsive','border': '2'}
        exclude = { 'id', }
