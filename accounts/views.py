import django.http.request
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.contrib.auth.decorators import login_required
User=get_user_model()

# Create your views here.
def index(request):
	return render(request, "accounts/index.html")
def add(request):
    c_value=None
    if request.method == "POST":
        a_value = int(request.POST.get("a_value", ""))
        b_value = int(request.POST.get("b_value", ""))
        c_value = a_value + b_value
        print(c_value)
        return render(request,'accounts/add.html', {"a_value":a_value,"b_value":b_value,"c_value":c_value}) 
    return render(request,'accounts/add.html')

def sub(request):
    c_value=None
    if request.method == "POST":
        a_value = int(request.POST.get("a_value", ""))
        b_value = int(request.POST.get("b_value", ""))
        c_value = a_value - b_value
        print(c_value)
        return render(request,'accounts/sub.html', {"a_value":a_value,"b_value":b_value,"c_value":c_value}) 
    return render(request,'accounts/sub.html')

def multi(request):
    c_value=None
    if request.method == "POST":
        a_value = int(request.POST.get("a_value", ""))
        b_value = int(request.POST.get("b_value", ""))
        c_value = a_value * b_value
        print(c_value)
        return render(request,'accounts/multi.html', {"a_value":a_value,"b_value":b_value,"c_value":c_value}) 
    return render(request,'accounts/multi.html')

def div(request):
    c_value=None
    if request.method == "POST":
        a_value = int(request.POST.get("a_value", ""))
        b_value = int(request.POST.get("b_value", ""))
        c_value = a_value / b_value
        print(c_value)
        return render(request,'accounts/div.html', {"a_value":a_value,"b_value":b_value,"c_value":c_value}) 
    return render(request,'accounts/div.html')

def modulus(request):
    c_value=None
    if request.method == "POST":
        a_value = int(request.POST.get("a_value", ""))
        b_value = int(request.POST.get("b_value", ""))
        c_value = a_value % b_value
        print(c_value)
        return render(request,'accounts/modulus.html', {"a_value":a_value,"b_value":b_value,"c_value":c_value}) 
    return render(request,'accounts/modulus.html') 

def floordivision(request):
    c_value=None
    if request.method == "POST":
        a_value = int(request.POST.get("a_value", ""))
        b_value = int(request.POST.get("b_value", ""))
        c_value = a_value // b_value
        print(c_value)
        return render(request,'accounts/floordivision.html', {"a_value":a_value,"b_value":b_value,"c_value":c_value}) 
    return render(request,'accounts/floordivision.html') 



def dashboard(request):
	return render(request, "accounts/dashboard.html")

def signup_view(request):
    if request.user.is_authenticated:
        return redirect("index")

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")
        confirm_password = request.POST.get("confirm_password", "")

        if not username or not email or not password or not confirm_password:
            messages.error(request, "All fields are required.")
            return redirect("signup")
                    
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("signup")

        if len(password) < 8:
            messages.error(request, "Password must be at least 8 characters.")
            return redirect("signup")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("signup")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        login(request, user)
        messages.success(request, "Account created successfully.")
        return redirect("index")

    return render(request, "accounts/signup.html")

def login_view(request):
    if request.user.is_authenticated:
        return redirect("index")

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        if not username or not password:
            messages.error(request, "Username and password are required.")
            return redirect("login")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully.")

            next_url = request.GET.get("next")
            return redirect(next_url or "index")
        else:
            messages.error(request, "Invalid username or password.")
            return redirect("login")

    return render(request, "accounts/login.html")

@login_required
def logout_view(request):
     logout(request)
     messages.success(request, "Logged out successfully.")
     return redirect("login")

def about_view(request):
    return render(request,"accounts/about.html")

def contactus_view(request):
    return render(request,"accounts/contactus.html")

def forgotpassword(request):
    return render(request,"accounts/forgotpassword.html")

def termsandconditions_view(request):
    return render(request,"accounts/termsandconditions.html")

def help_center(request):
    return render(request, "accounts/help_center.html")

def careers(request):
    return render(request, "accounts/careers.html")

def faq(request):
    return render(request, "accounts/faq.html")

def subscriptions(request):
    return render(request, "accounts/subscriptions.html")
def product_view(request):
    return render(request,"accounts/product.html")

def accessbility_view(request):
    return render(request,"accounts/accessbility.html")

def cookie_policy(request):
    return render(request, "accounts/cookie_policy.html")

def privacy_policy(request):
    return render(request, "accounts/privacy_policy.html")

def error_404_view(request):
    return render(request, "accounts/404.html")

def blog_view(request):
    return render(request, "accounts/blog.html")

def media_view(request):
    return render(request, "accounts/media.html")

def whyus_view(request):
    return render(request, "accounts/whyus.html")

def events_view(request):
    return render(request, "accounts/events.html")

def clients_view(request):
    return render(request, "accounts/clients.html")

def mission_view(request):
    return render(request, "accounts/mission.html")

def documentation_view(request):
    return render(request, "accounts/documentation.html")

def reports_view(request):
    return render(request, "accounts/reports.html")

@login_required
def dashboard_view(request):
    return render(request, "accounts/dashboard.html")



        



