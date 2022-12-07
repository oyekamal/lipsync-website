from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('',views.home, name='home'),
    path('test/',views.test, name='test'),
    path('upload/',views.Fileuploadrederer, name='upload'),
    path('mouth/',views.Mouthrederer, name='mouth'),
    path('files/',views.list_of_files, name='files'),
    

]