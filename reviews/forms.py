from re import error
from django import forms


# class ReviewForm(forms.Form):
#     user_name = forms.CharField(
#         label='Your Name', 
#         max_length=50,
#         required=True,
#         error_messages={
#             'required': 'Your name must not be empty!',
#             'max_length': "Please enter a shorter name!"
#         }
#         )
#     review_text = forms.CharField(
#         label='Your Feedback',
#         widget=forms.Textarea,
#         max_length=200
#         )
#     rating = forms.IntegerField(
#         label='Your rating', 
#         min_value=1, 
#         max_value=5
#         ) 

from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review   # model name is Review
        fields = "__all__"   # if u want all fields

        labels = {
            'user_name': "Your Name",
            'review_text': 'Your Feedback',
            'rating': 'Your Rating'
        }

        error_messages = {
            "user_name": {
                'required': 'Your name must not be empty!',
                'max_length': "Please enter a shorter name!"
            }
        }
        
        # fields = ['username', 'review_text', 'rating']
        # exclude = ['owner_comment']  # if you want to exclude any field
