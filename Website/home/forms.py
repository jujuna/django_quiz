from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


from django.forms import ModelForm

User = get_user_model()




class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'სახელი'}))
    email = forms.EmailField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'მაილი'}))

    
    
    def __init__(self, *args, **kwargs):
            super(SignUpForm, self).__init__(*args, **kwargs)
            self.fields['password1'].widget.attrs['placeholder'] ="პაროლი"
            self.fields['password2'].widget.attrs['placeholder'] ="გაიმეორეთ პაროლი"
            self.fields['mob'].widget.attrs['placeholder'] ="ტელეფონი"
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'inp'
            for k, field in self.fields.items():
                if 'required' in field.error_messages:
                    field.error_messages['required'] = 'შეავსე ველი'
            self.fields["password2"].help_text=""
            
            
            
    error_messages = {
        'password_mismatch': "პაროლები არ ემთხვევა",
    }
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2','mob', )

        

    def clean_mob(self, *args, **kwargs):
        mob=self.cleaned_data['mob']
        if len(mob)<8:
            raise ValidationError("ნომერი ნაკლებია 8 სიმბოლოზე  ")
        return mob


