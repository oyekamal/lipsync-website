from applipsync.models import File, GentleJson, Video, VideoFrame
from django.shortcuts import get_object_or_404, redirect, render

from .forms import FileUploadForm, MouthForm, UserForm, FileUploadFormCreate

# Create your views here.


def home(request):

    return render(request, "store/home.html")


def test(request):
    print(" testing...")
    if request.method == "GET":
        print(" -------------- GET --------------------------------    ")
        form = UserForm
        mydict = {
            "form": form,
        }
        return render(request, "store/test.html", context=mydict)
    elif request.method == "POST":
        print(" -------------- post --------------------------------    ")
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    else:
        return redirect("/")


def Fileuploadrederer(request):
    if not request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method == "GET":
            form = FileUploadForm(request.user)
            mydict = {
                "form": form,
            }
            return render(request, "store/upload.html", context=mydict)

        else:
            try:
                request.POST._mutable = True
                request.POST["host"] = f"{request.scheme}://{request.META['HTTP_HOST']}"
                # request.POST._mutable=False
                request_data = request.POST.copy()
                request_file = request.FILES.copy()
                request_data["host"] = f"{request.scheme}://{request.META['HTTP_HOST']}"
                request_data["user"] = request.user.id
                print("reqeust after", request_data)
                print("reqeust after", request_file)
                form = FileUploadFormCreate(request_data, request_file)

                if form.is_valid():
                    form.save()
                    return render(
                        request, "store/upload.html", {"form": form, "success": True}
                    )
                else:
                    print("files ERROR------->")
                    print(form.errors)
                    # return redirect('/files/')

            except Exception as e:
                print("Exception......")
                print(e)
                return redirect('/')
            return render(request, "store/upload.html", {"form": form})


def Mouthrederer(request):
    if not request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method == "GET":
            form = MouthForm
            mydict = {
                "form": form,
            }
            return render(request, "store/mouth.html", context=mydict)
        else:
            try:
                request_data = request.POST.copy()
                request_file = request.FILES.copy()
                form = MouthForm(request_data, request_file)
                if form.is_valid():
                    form.save()
                    return render(
                        request, "store/mouth.html", {"form": form, "success": True}
                    )
                else:
                    print(form.errors)
            except Exception as e:
                print(e)
            return render(request, "store/mouth.html", {"form": form})


def list_of_files(request):
    files = File.objects.all()
    # context = {'data', data}
    if not request.user.is_authenticated:
        return redirect("/")
    else:
        files = File.objects.filter(user=request.user)
        return render(request, "store/list_of_files.html", context={"files": files})


def video_details(request, slug):
    if not request.user.is_authenticated:
        return redirect("/")
    else:
        video = None
        video_frame = None
        gentle_json = None
        file = get_object_or_404(File, slug=slug)
        gentle_json = GentleJson.objects.filter(file=file)
        if gentle_json:
            video_frame = VideoFrame.objects.filter(gentle_josn=gentle_json[0])
            gentle_json = gentle_json[0]
        if video_frame:
            video = Video.objects.filter(video_frame=video_frame[0])
            if video:
                video = video[0]
        data = {
            "file": file,
            "gentle_json": gentle_json,
            "video_frame": video_frame,
            "video": video,
        }

        return render(request, "store/video_details.html", context=data)
