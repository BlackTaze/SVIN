from django.shortcuts import render
from .models import News, Rules, Review
from django.core.paginator import Paginator
from django.forms import modelform_factory
from django.views.generic.edit import FormView, CreateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse_lazy
from .forms import RegisterUserForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import redirect
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


def index(request):
    news_last = News.objects.latest("published")
    rules = Rules.objects.get(id=1)
    context = {"news_last": news_last, "rules":rules}
    return render(request,"SVIN_main/index.html",context)

def news(request):
    news = News.objects.all()
    paginator = Paginator(news,6)
    page_num = request.GET.get("page")
    page = paginator.get_page(page_num)
    context = {"page":page}
    return render(request,"SVIN_main/news.html",context)

def rules(request):
    rules = Rules.objects.all()
    context = {"rules": rules}
    return render(request, "SVIN_main/rules.html", context)

def contacts(request):
    return render(request, "SVIN_main/contacts.html")


class RegisterUser(CreateView):
    template_name = "registration/register.html"
    form_class = RegisterUserForm
    success_url = reverse_lazy("register")
    
class LoginUser(LoginView):
    template_name = "registration/login.html"
    authentification_form = AuthenticationForm
    user = User
   
    def get_success_url(self):
        return reverse_lazy("index")

def logout_user(request):
    logout(request)
    return redirect("index")

from django.contrib.auth.decorators import login_required

    
def votes(request):
    votes = Review.objects.all()
    context = {"votes" : votes}
    return render(request,"SVIN_main/votes.html",context)

@login_required
def submit_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('reviews')
    else:
        form = ReviewForm(user=request.user)
    return render(request, 'SVIN_main/submit_review.html', {'form': form})

def review_list(request):
    reviews = Review.objects.all()
    context = {
        'reviews': reviews
    }
    return render(request, 'SVIN_main/votes.html', context)