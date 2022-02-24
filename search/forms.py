from django import forms
from search.models import Movie, SearchValue, Review

def min_5char(value):
    if(len(value)<5):
        raise forms.ValidationError('리뷰는 5글자 이상 입력해주세요')

def min_1char(value):
    if(len(value)<5):
        raise forms.ValidationError('제목은 1글자 이상 입력해주세요')

class MovieModel(forms.ModelForm):
    class Meta:
        model = SearchValue
        fields = ('title',)

class MovieReview(forms.Form):
    review = forms.CharField(widget=forms.Textarea, validators=[min_5char])


