from django.forms import ModelForm, Textarea
from reviews.models import Review

# File used to create Django ModelForm this allows us to dynamically create a form.


# method to create a form to submit our reviews. Specifies object to be used as base.
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['user_name', 'rating', 'comment']
        widgets = {
            'comment': Textarea(attrs={'cols': 40, 'rows': 15})
        }
