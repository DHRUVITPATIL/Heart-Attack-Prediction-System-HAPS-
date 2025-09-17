from django import forms
from django.contrib.auth.models import User


class HeartForm(forms.Form):
    age = forms.IntegerField(label="Age")
    sex = forms.ChoiceField(choices=[(1, "Male"), (0, "Female")])
    cp = forms.IntegerField(label="Chest pain type")
    trtbps = forms.IntegerField(label="Resting blood pressure")
    chol = forms.IntegerField(label="Serum cholesterol")
    fbs = forms.ChoiceField(choices=[(1,"Yes"), (0,"No")],label="Fasting blood sugar > 120 mg/dl")
    restecg = forms.IntegerField(label="Resting ECG")
    thalachh = forms.IntegerField(label="Max heart rate achieved")
    exng = forms.ChoiceField(choices=[(1, "Yes"), (0, "No")], label="Exercise-induced angina")
    oldpeak = forms.FloatField(label="ST depression")
    slp = forms.IntegerField(label="Slope of peak exercise ST segment")
    caa = forms.IntegerField(label="Number of major vessels")
    thall = forms.IntegerField(label="Thalassemia")


class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    class Meta:
        model = User
        fields = ('username', 'email')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        if password and password2 and password != password2:
            self.add_error('password2', "Passwords must match")
        return cleaned_data

class SigninForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")

class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your Name")
    email = forms.EmailField(label="Your Email")
    message = forms.CharField(widget=forms.Textarea(attrs={"rows": 5}), label="Your Message")

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'readonly': 'readonly'}),  # username not editable, remove if you want it editable
        }