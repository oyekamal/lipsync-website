from django.shortcuts import render, redirect
from .forms import UserForm, FileUploadForm
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
    print(request)
    if request.method == 'GET':
        form = FileUploadForm
        mydict = {
            'form': form,
        }
        return render(request, 'store/upload.html', context=mydict)

    else:
        try:
            form = FileUploadForm(request.POST, request.FILES)
            if form.is_valid():

                form.save()
                print(form)
            else:
                print(form.errors())
            # {'csrfmiddlewaretoken': ['gue4rN9myMcCPO09Y0PrHK54FyUd2V0Fp8OAM6eRzJJw3bww2femxtKPF10WlGoU'], 'audio': ['software4.wav'], 'script': ['software4.txt'], 'remark': ['asd']}>
            # File.objects.create(audio=request.POST['audio'],script=request.POST['script'],remark=request.POST['remark'])
        except Exception as e:
            print(e)

        return redirect('/')
