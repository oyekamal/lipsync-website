from django.shortcuts import render, redirect
from .forms import UserForm, FileUploadForm, MouthForm
from applipsync.models import File
# Create your views here.


def home(request):

    return render(request, 'store/home.html')


def test(request):
    print(" testing...")
    if request.method == 'GET':
        print(" -------------- GET --------------------------------    ")
        form = UserForm
        mydict = {
            'form': form,
        }
        return render(request, 'store/test.html', context=mydict)
    elif request.method == "POST":
        print(" -------------- post --------------------------------    ")
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        return redirect('/')


def Fileuploadrederer(request):
    print( "request before   ",request.POST)
    if request.method == 'GET':
        form = FileUploadForm
        mydict = {
            'form': form,
        }
        return render(request, 'store/upload.html', context=mydict)

    else:
        try:
            request.POST._mutable=True
            request.POST['host'] = f"{request.scheme}://{request.META['HTTP_HOST']}"
            # request.POST._mutable=False
            request_data = request.POST.copy()
            request_file = request.FILES.copy()
            request_data['host'] = f"{request.scheme}://{request.META['HTTP_HOST']}"
            print("reqeust after", request_data)
            print("reqeust after", request_file)
            form = FileUploadForm(request_data, request_file)

            
            if form.is_valid():
                form.save()
            else:
                print(form.errors())

        except Exception as e:
            print(e)

        return redirect('/')

def Mouthrederer(request):
    print( "request before   ",request.POST)
    if request.method == 'GET':
        form = MouthForm
        mydict = {
            'form': form,
        }
        return render(request, 'store/upload.html', context=mydict)

    else:
        try:
            request_data = request.POST.copy()
            request_file = request.FILES.copy()

            form = MouthForm(request_data, request_file)

            
            if form.is_valid():
                form.save()
            else:
                print(form.errors())

        except Exception as e:
            print(e)

        return redirect('/')

