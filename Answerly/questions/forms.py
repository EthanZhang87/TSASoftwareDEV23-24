from django.forms import ModelForm
from .models import Question, Event, Profile, QuestionImage
from django import forms
from django.contrib.auth.models import User


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
        exclude = ['author', 'participants']

class QuestionImageForm(ModelForm):
    class Meta:
        model = QuestionImage
        fields = "__all__"
        exclude = ['user']


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = "__all__"
        exclude = ['host']
        widgets = {
            'date': forms.widgets.DateInput(attrs={'type': 'date'})
        }

class UserUpdateForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['username']


class ImageUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


    