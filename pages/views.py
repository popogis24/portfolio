from django.shortcuts import render
from django.http import FileResponse

# Create your views here.
def home(request):
    return render(request, 'pages/home.html')  # This is the path to the home.html file

def about(request):
    return render(request, 'pages/about.html')  # This is the path to the about.html file

def download_cv(request):
    #baixa o arquivo meucv.pdf
    file_path = '/Users/andersonstolfi/Documents/portfolio/pages/archive/Resume_CV_AndersonStolfi_.pdf'
    return FileResponse(open(file_path, 'rb'), as_attachment=True)  # This is the path to the meucv.pdf file
