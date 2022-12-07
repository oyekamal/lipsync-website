from django.shortcuts import render, redirect, get_object_or_404
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
    if not request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'GET':
            form = FileUploadForm
            mydict = {
                'form': form,
            }
            return render(request, 'store/upload.html', context=mydict)

        else:
            try:
                request.POST._mutable = True
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
    if not request.user.is_authenticated:
        return redirect('/')
    else:
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


def list_of_files(request):
    files = File.objects.all()
    # context = {'data', data}
    if not request.user.is_authenticated:
        return redirect('/')
    else:
        files = File.objects.all()
        return render(request, 'store/list_of_files.html', context={'files': files})

def video_details(request, slug):
    if not request.user.is_authenticated:
        return redirect('/')
    else:
        file = get_object_or_404(File, slug=slug)
        return render(request, 'store/video_details.html', context={'file': file})
