from django.http import HttpResponse         #! homepage step:1

def home(request):
    return HttpResponse(
        '<center><h1 style="background-color:powderblue;">Welcome to Home Page <br> Rocket was here 🚀 </h1></center>'
        )


#todo anasayfada gözükmesi icin view olusturdum.
#todo bu views i urls de tanimlamam lazim.