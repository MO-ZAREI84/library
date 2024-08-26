from django import forms 
class AuthorForm(forms.Form):
    name=forms.CharField()
    

    def clean_name(self):
        name=self.cleaned_data['name']
        is_valid= len(name) <=100
        if not is_valid:
            raise forms.ValidationError('is not possible')
        return name
