from django.shortcuts import render

from django.http import HttpResponseRedirect
# Create your views here.

from .forms import ReviewForm

from .models import Review

from django.views import View

from django.views.generic.base import TemplateView

from django.views.generic import DetailView, ListView

from django.views.generic.edit import FormView


# Class-based view
class ReviewView(FormView):
    form_class = ReviewForm
    template_name = 'reviews/reviews.html'
    success_url = '/thank-you'


    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


# class ReviewView(View):
#     def get(self, request):
#         form = ReviewForm()
#         return render(request, "reviews/reviews.html", {
#             "form": form
#         })

#     def post(self, request):   
#         form = ReviewForm(request.POST)
#         # form = ReviewForm(request.POST)

#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/thank-you")

#         return render(request, "reviews/reviews.html", {
#             "form": form
#         })
        



# def reviews(request):
#     # if request.method == "POST":
#     #     entered_username = request.POST["username"]
#     #     print(entered_username)

#     #     if entered_username == "" and len(entered_username) >= 100:
#     #         return render(request, "reviews/reviews.html", {
#     #             "has_error": True
#     #         })
         
#         # return HttpResponseRedirect("/thank-you")
#     if request.method == "POST":
#         existing_model = Review.objects.get(pk=1)   
#         form = ReviewForm(request.POST, instance=existing_model)
#         # form = ReviewForm(request.POST)

#         if form.is_valid():
#             form.save()   # when using modelform
#             print(form.cleaned_data)   # dictionary

#             # save data in database
#             # review = Review(
#             #     user_name = form.cleaned_data['user_name'],
#             #     review_text = form.cleaned_data['review_text'],
#             #     rating = form.cleaned_data['rating'] 
#             #     )
#             # review.save()

#             return HttpResponseRedirect("/thank-you")
#     else:
#         form = ReviewForm()
            
    
#     # return render(request, "reviews/thankyou.html")
#     return render(request, "reviews/reviews.html", {
#         "form": form
#         })



# def thank_you(request):
#     return render(request, "reviews/thankyou.html")


# using class-based view
# class ThankYouView(View):
#     def get(self, request):
#         return render(request, "reviews/thankyou.html")

class ThankYouView(TemplateView):
    template_name = "reviews/thankyou.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This Works!"
        return context

class ReviewListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    # # if you want to fiter data
    # def get_queryset(self):
    #     context  = super().get_queryset()
    #     data = context.filter(rating__gt=4)
    #     return data


# class ReviewListView(TemplateView):
#     template_name = "reviews/review_list.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)


#         reviews = Review.objects.all()
#         context['reviews'] = reviews

#         return context


# class ReviewTextView(TemplateView):
#     template_name = "reviews/review_text.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         review_id = kwargs["id"]   # gets id
#         selected_review = Review.objects.get(pk=review_id)
#         context["review"] = selected_review
    
#         return context

class ReviewTextView(DetailView):
    template_name = "reviews/review_text.html"
    model = Review