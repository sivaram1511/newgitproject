from django.shortcuts import render

# Create your views here.
def home_page_view(request):
    return render(request,'testapp/home.html')
def java_exam_view(request):
    return render(request,"testapp/javaexams.html")
def python_exam_view(request):
    return render(request,"testapp/pythonexams.html")