from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Review, Beer
from .forms import ReviewForm
import datetime
# views are supposedly just python functions that decide what to show.
# Create your views here.

# Queries are normally performed by using the .objects attribute in the given domain entity class
# (e.g. Review.objects).

# gets a list of the latest 9 reviews and renders it using `reviews/list.html'.
def review_list(request):
    latest_review_list = Review.objects.order_by('-pub_date')[:9]
    context = {'latest_review_list':latest_review_list}
    return render(request, 'reviews/review_list.html', context)

# gets a review given its ID and renders it using review_detail.html
def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'reviews/review_detail.html', {'review': review})

# gets all the beers sorted by name and passes it to beer_list.html to be rendered.
def beer_list(request):
    beer_list = Beer.objects.order_by('-name')
    context = {'beer_list':beer_list}
    return render(request, 'reviews/beer_list.html', context)

# gets a beer from the DB given its ID and renders it using beer_detail.html
def beer_detail(request, beer_id):
    beer = get_object_or_404(Beer, pk=beer_id)
    form = ReviewForm()
    return render(request, 'reviews/beer_detail.html', {'beer': beer, 'form': form})

#@login_required is needed to make sure user is signed in so that they can add a review.
@login_required
def add_review(request, beer_id):
#retrieve beer we will add review for if not availbale display 404 error.
    beer = get_object_or_404(Beer, pk=beer_id)
    # create review form instance
    form = ReviewForm(request.POST)
    # validate data
    if form.is_valid():
        rating = form.cleaned_data['rating']
        comment = form.cleaned_data['comment']
        user_name = request.user.username
        review = Review()
        review.beer = beer
        review.user_name = user_name
        review.rating = rating
        review.comment = comment
        review.pub_date = datetime.datetime.now()
        review.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('reviews:beer_detail', args=(beer.id,)))

    return render(request, 'reviews/beer_detail.html', {'beer': beer, 'form': form})
