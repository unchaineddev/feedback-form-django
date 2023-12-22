from django.shortcuts import render

from django.http import HttpResponseRedirect
# Create your views here.

from .forms import ReviewForm

from .models import Review

def reviews(request):
    # if request.method == "POST":
    #     entered_username = request.POST["username"]
    #     print(entered_username)

    #     if entered_username == "" and len(entered_username) >= 100:
    #         return render(request, "reviews/reviews.html", {
    #             "has_error": True
    #         })
         
        # return HttpResponseRedirect("/thank-you")
    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)   # dictionary

            # save data in database
            review = Review(
                user_name = form.cleaned_data['user_name'],
                review_text = form.cleaned_data['review_text'],
                rating = form.cleaned_data['rating'] 
                )
            review.save()

            return HttpResponseRedirect("/thank-you")
    else:
        form = ReviewForm()
            
    
    # return render(request, "reviews/thankyou.html")
    return render(request, "reviews/reviews.html", {
        "form": form
        })



def thank_you(request):
    return render(request, "reviews/thankyou.html")