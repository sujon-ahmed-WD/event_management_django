from django.shortcuts import redirect, render

# Create your views here.
def hom(request):
    return render(request,'home.html')

def no_permission(request):
    return render(request,'no_permission.html')
# def dashboard_redirect(request):
#     return redirect('home')