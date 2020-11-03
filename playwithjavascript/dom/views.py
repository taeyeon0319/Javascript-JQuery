from django.shortcuts import render

# Create your views here.
def dom(request):
    return render(request, 'dom/dom.html')

def showBig(request):
    return render(request, 'dom/showBig.html')

def main(request):
    return render(request, 'dom/main.html')

def history(reqeust):
    return render(reqeust, 'dom/history.html')