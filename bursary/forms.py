from django import forms
from . import models
from system.models import FacultyData, DepartmentData, SessionData



class FeesCreationForm(forms.ModelForm):
    fid = forms.ModelChoiceField(queryset=FacultyData.objects.all(), empty_label="--Select Faculty--",
                                 widget=forms.Select(attrs={'class': 'form-control'}))

    did = forms.ModelChoiceField(queryset=DepartmentData.objects.all(), empty_label="--Select Faculty First--",
                                 widget=forms.Select(attrs={'class': 'form-control'}))

    sid = forms.ModelChoiceField(queryset=SessionData.objects.all(), empty_label="--Select Session--",
                                 widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = models.SchoolFees
        fields = ['sid', 'fid', 'did', 'amount']

        widgets = {
            'amount': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Amount'})

        }

    def __init__(self, *args, **kwargs):
        super(FeesCreationForm, self).__init__(*args, **kwargs)
        self.fields['did'].queryset = DepartmentData.objects.none()

       # Get did queryset for the selected fid
        if 'fid' in self.data:
            try:
                fd = int(self.data.get('fid'))
                self.fields['did'].queryset =  DepartmentData.objects.filter(fid_id=fd).order_by('id')
            except (ValueError, TypeError):
                pass # invalid input from the client; ignore and use empty queryset
        elif self.instance.pk:
            self.fields['did'].queryset = self.instance.fid.departmentdata_set.order_by('id')
            #backward relation - for this faculty selected, check its deparm
            #every department has its faculty
            # #in other word, which dept has their foreign key pointing to the current instance of faculty
