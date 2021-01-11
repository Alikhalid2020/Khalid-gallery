from django.http  import HttpResponse
from django.shortcuts import render,redirect
import datetime as dt
from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .models import Image,Location,categories

# Create your views here.
def gallery(request):
    images = Image.all_images()
    locations = Location.objects.all()
    return render(request, 'index.html', {"images":images,"locations":locations})

def location(request,location):
    locations = Location.objects.all()
    selected_location = Location.objects.get(id = location)
    images = Image.objects.filter(location = selected_location.id)
    return render(request, 'location.html', {"location":selected_location,"locations":locations,"images":images})


def search(request):
    if 'imagesearch' in request.GET and request.GET["imagesearch"]:
        search_term = request.GET.get("category")
        category = request.GET.get("imagesearch")
        searched_images = Image.search_by_category(category)
        message = f"{category}"
        print(searched_images)
        return render(request,'search.html',{"images":searched_images,"category":search_term})
    else:
        message = "You haven't searched for any image category"
        return render(request, 'search.html', {"message": message})

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def gallery_today(request):
    date = dt.date.today()
    images= Image.objects.all()
    return render(request, 'all-images/today-images.html', {"date": date,"images":images})


#......
# View Function to present gallery from past days
def past_days_gallery(request, past_date):

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(gallery_of_day)

    return render(request, 'all-images/past-images.html', {"date": date})