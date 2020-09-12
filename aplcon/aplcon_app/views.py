from django.shortcuts import render

# Create your views here.

#ホーム画面のView
def homeView(request):
  return render(request,'home.html')
