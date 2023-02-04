from django.shortcuts import get_object_or_404, redirect, render

from applipsync.models import File, GentleJson, Question, Video, VideoFrame, Mouth, Blog, Category
from django.db.models import Q


from .forms import (
    FileUploadForm,
    FileUploadFormCreate,
    MouthForm,
    QuestionForm,
    UserForm,
)

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
                return redirect("/")
            return render(request, "store/upload.html", {"form": form})


def use(request):
    return render(request, "store/use.html")

def Aboutrederer(request):
    return render(request, "store/about.html")

def Blog_list(request):
    blogs = Blog.objects.all()
    Categories = Category.objects.all()
    return render(request, "store/blog.html", context={"blogs": blogs, "Categories": Categories})

def error_404_view(request, exception=None):
    return render(request, "store/404.html")


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
                request.POST._mutable = True

                request_data = request.POST.copy()
                request_data["user"] = request.user.id
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


def Questionrederer(request):

    if request.method == "GET":
        form = QuestionForm
        mydict = {
            "form": form,
        }
        return render(request, "store/question.html", context=mydict)
    else:
        try:
            request_data = request.POST.copy()
            request_file = request.FILES.copy()
            form = QuestionForm(request_data, request_file)
            if form.is_valid():
                form.save()
                return render(
                    request, "store/question.html", {"form": form, "success": True}
                )
            else:
                print(form.errors)
        except Exception as e:
            print(e)
        return render(request, "store/question.html", {"form": form})


def list_of_files(request):
    # files = File.objects.all()
    # context = {'data', data}
    if not request.user.is_authenticated:
        return redirect("/")
    else:
        files = File.objects.filter(user=request.user)
        return render(request, "store/list-of-files.html", context={"files": files})

def list_of_mouth(request):
    if not request.user.is_authenticated:
        return redirect("/")
    else:
        mouths = Mouth.objects.filter(
            Q(user=request.user) | Q(user__username="admin")
        )
        return render(request, "store/list-of-mouth.html", context={"mouths": mouths})
    
def list_of_admin_mouth(request):
    mouths = Mouth.objects.filter(Q(user__username="admin"))
    return render(request, "store/list-of-mouth.html", context={"mouths": mouths})



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

        return render(request, "store/video-details.html", context=data)

def mouth_details(request, slug):
    print("Mouth Details")
    if not request.user.is_authenticated:
        mouth =Mouth.objects.filter(user__username="admin",title=slug)
        if mouth:
            
            data = {
                "mouth": mouth[0],
            }
            return render(request, "store/mouth-details.html", context=data)
        else:
            return redirect("/")
    else:
        mouth = get_object_or_404(Mouth, title=slug)

        data = {
            "mouth": mouth,
        }

        return render(request, "store/mouth-details.html", context=data)
    
    
def blog_details(request, slug):
    print("blog Details")
    blog = get_object_or_404(Blog, slug=slug)
    categories= blog.categories.all()
    categories_name = " "
    if categories:
        for cat in categories:
            categories_name = categories_name + cat.name + ", "
            
    tags = blog.tags.all()
    tags_name = " "
    if tags:
        for tag in tags:
            tags_name = tags_name + tag.name + ", "
    return render(request, "store/blog-details.html", context={"blog": blog, "categories":categories_name, "tags":tags_name})
