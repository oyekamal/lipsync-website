from django.shortcuts import render
from .forms import UserForm
# Create your views here.


def home(request):

    return render(request, 'store/home.html')

def test(request):
    form = UserForm
    mydict = {
        'form': form,
    }
    return render(request, 'store/test.html',context=mydict)