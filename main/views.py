from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .models import UserProfile

def home(request):
    """Render the home page."""
    return render(request, 'main/home.html')

def dashboard(request):
    """Render the dashboard page for authenticated users."""
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'main/dashboard.html')

def login_view(request):
    """Handle user login."""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                # Optional: Add an error message if authentication fails
                form.add_error(None, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    
    return render(request, 'main/login.html', {'form': form})

