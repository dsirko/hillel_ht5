from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views import View

class LoginView(View):

    def get(self, request):
        """
        Method to handle GET requests, takes a request object as a parameter, and returns a rendered login form.
        """
        form = AuthenticationForm()
        return render(request, "login.html", {"form": form})

    def post(self, request):
        """
        A description of the entire function, its parameters, and its return types.
        """
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("/login")
        return render(request, "login.html", {"form": form})

class LogoutView(View):
    def post(self, request):
        """
        A function that logs out the user and redirects them to the login page.
        request: The request object containing user information.
        Returns: A redirect response to the login page.
        """
        logout(request)
        return redirect("/login")

class RegisterView(View):
    def get(self, request):
        """
        A function to handle GET requests, it creates a UserCreationForm form and renders the 'register.html' template with the form.
        Parameters: request: the HTTP request object
        Returns: The rendered 'register.html' template with the UserCreationForm form
        """
        form = UserCreationForm()
        return render(request, "register.html", {"form": form})

    def post(self, request):
        """
        A function to handle POST requests for user creation.
        Parameters: request: HttpRequest object containing the request data.
        Returns: HttpResponse object with appropriate response based on form validation.
        """
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            message = {"message": "User successfully created!", "color": "green"}
            return render(request, "login.html", {"message": message})
        return render(request, "register.html", {"form": form})
