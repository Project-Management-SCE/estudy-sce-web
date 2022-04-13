from django import forms

opt_role = (
   ( "student", "סטודנט"),
   ("lecturer", "מרצה")
)

class UserForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)
    verify_pass = forms.CharField(widget=forms.PasswordInput())
    password = forms.CharField(widget=forms.PasswordInput())
    role = forms.ChoiceField(choices=opt_role, widget=forms.Select(attrs={'class': "form-select form-select-sm" ,'aria-label':".form-select-sm example"}))

    def clean_password(self):
      password = self.cleaned_data['password']
      verify_pass = self.cleaned_data['verify_pass']
      if len(password) < 8:
        raise forms.ValidationError("The Password must be more of 8 charaters")
        
      if password != verify_pass:
        raise forms.ValidationError("The Password are not the same.")
      return password

    def clean_name(self):
      name = self.data['name']
      for ch in name:
        if not ch.isalpha():
          raise forms.ValidationError("write name correct without space and numeric chararters")
      return name