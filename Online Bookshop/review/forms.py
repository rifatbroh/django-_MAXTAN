from django import forms
from review.constants import RATINGS

class ReviewForm(forms.Form):
    ratings = forms.IntegerField(widget=forms.Select(choices=RATINGS))
    description = forms.CharField(widget=forms.Textarea, required=False)
