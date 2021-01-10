from django.http  import HttpResponse
from django.shortcuts import render,redirect
# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def gallery_of_day(request):
    date = dt.date.today()
    return render(request, 'all-gallery/today-gallery.html', {"date": date,})


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

    return render(request, 'all-gallery/past-gallery.html', {"date": date})