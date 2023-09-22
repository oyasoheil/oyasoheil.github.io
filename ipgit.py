from django.shortcuts import render

def index(request):
  num1 = request.POST.get('num1')
  num2 = request.POST.get('num2')

  sum = int(num1) + int(num2)

  return render(request, 'index.html', {'sum': sum})
