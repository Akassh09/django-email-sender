from django import forms

class subscribe(forms.Form):
    Name = forms.CharField(max_length=50)
    Email = forms.EmailField()

    def __str__(self):
        return self.Email