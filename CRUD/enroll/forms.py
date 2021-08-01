from django import forms


from enroll.models import Student


class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','email','password']
        # fields = '__all__'
        # exclude = ['name']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'})
        }