from django.shortcuts import render
from django.http import HttpResponse

def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        return HttpResponse(
            f"Usuario: {username} | Password: {password}"
        )

    return render(request, 'accounts/login.html')