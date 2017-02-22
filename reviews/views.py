from django.shortcuts import get_object_or_404, render
from .models import Review, Beer
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
    return render(request, 'reviews/beer_detail.html', {'beer': beer})
