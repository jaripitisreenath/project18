from django import forms
l=[('MALE','male'),('female','FEMALE')]
c=[('PYTHON','python'),('JAVA','java'),('MERN','mern')]
class FormName(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField(max_value=18)
    email=forms.EmailField()
    #gender=forms.ChoiceField(choices=l)
    gender=forms.ChoiceField(choices=l,widget=forms.RadioSelect)
    cources=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)
    
