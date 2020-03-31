from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = reques.POST.get('password2')
        print(username, password, password2)

        # create object of user
        user = User()
        user.username = username
        #user.password = password
        user.set_password(password)
        user.save()
        return render(request, 'accounts/signup_complete.html')

    else:
        context_values = {'form':'this is form'}
        return render(request, 'accounts/signup.html', context_values)
'''
    render
1. request template
2. redering template - replace context_value to template
3. HTTP Response - display completed content on screen
'''