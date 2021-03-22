
        
from django.shortcuts import render
from .models import shortURL
from .forms import for_newUrl
from datetime import datetime
import random, string


#Create your views here.
def shorturl(request):
    # Post: request used for things like user name and password get request used for search 

    if request.method == 'POST':
    if request.method == 'POST':
        form = for_newUrl(request.POST)
        if form.is_valid():
            original website=form.cleaned_data['original_url']
            slug = ''.join(random.choice(string.ascii_letters)
                           for x in range(10))
            url = form.cleaned_data["url"]
            new_url = UrlData(url=url, slug=slug)
            new_url.save()
            request.user.urlshort.add(new_url)
           return redirect('/')
           # return render(request, 'urlcreated.html', {'chars':random_chars})
    else:
 #Creating object
         d = datetime.now()
        form = for_newUrl()
    data = UrlData.objects.all()
    context = {
        'form': form,
        'data': data
    }
 return render(request, 'index.html', context)


def home(request):
    return render(request, 'home.html')

def redirect(request, url):
    current_obj = ShortURL.objects.filter(short_url=url)
    if len(current_obj) == 0:
        return render(request, 'pagenotfound.html')
    context = {'obj':current_obj[0]}
    return render(request, 'redirect.html', context)


            

