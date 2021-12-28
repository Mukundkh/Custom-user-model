from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm  
from accounts.forms import UserAdminCreationForm
from django.contrib.auth.decorators import login_required

@login_required()
def register(req):
    form = UserAdminCreationForm()
    if req.method == 'POST':
        form = UserAdminCreationForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    return render(req, 'accounts/register.html', {'form': form})