from django import forms
from .models import Course
from django.contrib.auth.models import User

STATUS_CHOICES = (
        ('پیش نویس', 'پیش نویس'),
        ('منتشر شده', 'منتشر شده'),
    )

class CourseForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs = {
            'class': 'form-control text-left',
            'placeholder': 'نام دوره'
        }
    ))
    slug = forms.CharField(widget=forms.TextInput(
        attrs = {
            'class': 'form-control text-left',
            'placeholder': 'آدرس اینترنتی'
        }
    ))
    author = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.Select(
        attrs = {
            'class': 'form-control text-left',
        }
    ))
    body = forms.CharField(widget=forms.Textarea(
        attrs = {
            'class': 'form-control text-left',
        }
    ))
    status = forms.CharField(widget=forms.Select(
        choices = STATUS_CHOICES,
        attrs = {
            'class': 'form-control text-left',
        }
    ))

    class Meta:
        model = Course
        fields = ['title', 'slug', 'author', 'body', 'status']