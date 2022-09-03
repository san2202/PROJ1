from django import forms
from app1.models import  UserInfo,Student

COURSES = (
    ("1","python"),
    ("2","django"),
    ("3","sql")
)

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = "__all__"

class studentform(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

class studentInfo(forms.Form):
    sid=forms.IntegerField(label="Enter number")
    sname=forms.CharField(label="Enter your Name:",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Full Name'}))
    fee=forms.IntegerField(label="Enter fee:",widget=forms.NumberInput(attrs={'class':'form-control','placeholder':' Enter fees'}))
    doj=forms.DateField(label="Enter :",widget=forms.SelectDateWidget)
  


class StudentF(forms.Form):
    sid=forms.IntegerField(label="Enter number")
    sname=forms.CharField(label="Enter your Name:",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Full Name'}))
    email=forms.EmailField(label="Enter your email-id:",widget=forms.EmailInput(attrs={'class':'form-control','placeholder':' Enter your Email ID'}))
    contact=forms.IntegerField(label="Enter your mobile number:",widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter your contact number'}))


  
class Practice(forms.Form):
    sid=forms.IntegerField(label="Enter number")
    sname=forms.CharField(label="Enter your Name:",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Full Name'}))
    courses=forms.ChoiceField(choices=COURSES)



