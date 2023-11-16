from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .forms import ReviewForm
from .models import Review
# from .models import Review

# Create your views here.


# class ReviewView(FormView):
#     form_class = ReviewForm
#     template_name = "reviews/review.html"
#     success_url = "/thank-you"
    
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)

# common way automatically saves the data and creates form so no need spesific form at form.py anymore but for configuration we still use form setup at form.py
class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm  #fields = '__all__' if no need config the form fields
    template_name = "reviews/review.html"
    success_url = "/thank-you"


    # def get(self, request):
    #     form = ReviewForm()
    #     return render(request, "reviews/review.html", {
    #         "form": form
    #     })

    # def post(self, request):
    #     form = ReviewForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect('/thank_you')


# def review(request):
#     if request.method == 'POST':
#        # existing_data = Review.objects.get(pk=1) # with model form method also we can update existing data like that
#         # form = ReviewForm(request.POST, instance=existing_data)
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             # review = Review(
#             #     user_name=form.cleaned_data['user_name'], review_text=form.cleaned_data['review_text'], rating=form.cleaned_data['rating'])
#             # review.save()
#             form.save() # now we can just save it with modelform no need extra connect to any model because its already connected a model
#             return HttpResponseRedirect('/thank_you')
#     else:
#         form = ReviewForm()

#     return render(request, "reviews/review.html", {
#         "form": form
#     })


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html" # now django will automatically render this template if it gets any GET request

    #if we need pass any context to a template we can do it like below for class based views
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "This works!"
        return context


    # def get(self, request):
    #     return render(request, "reviews/thank_you.html")

class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = 'reviews'

#filtering
    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(rating__gt=4)
        return data

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     reviews = Review.objects.all()
    #     context["reviews"] = reviews
    #     return context
    

class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review
    context_object_name = 'reviews'