from django.shortcuts import render,redirect
from .forms import HeartForm,SigninForm, SignupForm,FeedbackForm,ProfileForm
from .utils import load_model
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,update_session_auth_hash,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from .models import PredictionHistory



def predict(request):
    prediction = None
    if request.method == "POST":
        form = HeartForm(request.POST)
        if form.is_valid():
            features = [
                form.cleaned_data["age"],
                int(form.cleaned_data["sex"]),
                form.cleaned_data["cp"],
                form.cleaned_data["trtbps"],
                form.cleaned_data["chol"],
                int(form.cleaned_data["fbs"]),
                form.cleaned_data["restecg"],
                form.cleaned_data["thalachh"],
                int(form.cleaned_data["exng"]),
                form.cleaned_data["oldpeak"],
                form.cleaned_data["slp"],
                form.cleaned_data["caa"],
                form.cleaned_data["thall"],
            ]
            model = load_model()
            y_pred = model.predict([features])[0]
            prediction = "Heart Attack Risk: YES" if y_pred==1 else "Heart Attack Risk: NO"
        # ... after making prediction ...
            PredictionHistory.objects.create(
            user=request.user,
            features=str(features),  # Or JSON dumps if using JSONField
            prediction=prediction
        )
    else:
        form = HeartForm()
    return render(request, "predict.html", {"form": form, "prediction": prediction})

def home(request):
    return render(request, 'home.html')



def signup(request):
    return render(request, 'signup.html')
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request, 'signup_success.html', {'username': user.username})
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})
def signin(request):
    error = None
    if request.method == "POST":
        form = SigninForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('predict')  # Redirect to prediction after login
            else:
                error = "Invalid username or password."
    else:
        form = SigninForm()
    return render(request, 'signin.html', {'form': form, 'error': error})
def about(request):
    return render(request,"about.html")

def contact(request):
    submitted = False
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # You can handle the feedback data here:
            # For example: send email, save in database, etc.
            # For now, just acknowledge submission.
            submitted = True
            form = FeedbackForm()  # reset form after submission
    else:
        form = FeedbackForm()
        
    context = {
        'form': form,
        'submitted': submitted,
    }
    return render(request, 'contact.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return render(request, 'profile.html', {
                'form': form,
                'success': 'Your profile was updated successfully!'
            })

    else:
        form = ProfileForm(instance=request.user)
        history = PredictionHistory.objects.filter(user=request.user).order_by('-date')[:10]

    return render(request, 'profile.html', {
        'form': form,
        'history': history,
    })

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            return render(request, 'change_password.html', {'form': form, 'success': 'Your password was changed successfully!'})
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('signin') 
    