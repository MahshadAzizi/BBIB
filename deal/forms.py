from django import forms
from user.models import User

BRANCHES = (
    ('100', '100'),
    ('101', '101'),
    ('102', '102')
)


class DealForm(forms.Form):
    value_transaction = forms.CharField(widget=forms.NumberInput)
    national_code = forms.CharField(widget=forms.TextInput)
    branch_code = forms.ChoiceField(choices=BRANCHES)

    def clean(self):
        branch_code = self.cleaned_data.get('branch_code')
        national_code = self.cleaned_data.get('national_code')
        user = User.objects.filter(branch_code=branch_code, national_code=national_code).first()
        if user is None:
            self._errors['branch_code'] = self.error_class(['user not found'])
            self._errors['national_code'] = self.error_class(['user not found'])
        return self.cleaned_data
