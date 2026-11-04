from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .forms import JoinForm
from .models import Event, News, Opportunity, Project

def home(request):
    news = News.objects.filter(is_published=True)[:3]
    events = Event.objects.filter(status="planned", starts_at__gte=timezone.now())[:3]
    opportunities = Opportunity.objects.filter(is_published=True)[:3]
    return render(request, "center/home.html", {"news": news, "events": events, "opportunities": opportunities})

def news_list(request):
    items = News.objects.filter(is_published=True)
    return render(request, "center/news_list.html", {"items": items})

def news_detail(request, pk):
    item = get_object_or_404(News, pk=pk, is_published=True)
    return render(request, "center/news_detail.html", {"item": item})

def events_list(request):
    upcoming = Event.objects.filter(status="planned", starts_at__gte=timezone.now())
    past = Event.objects.filter(starts_at__lt=timezone.now()).exclude(status="cancelled")
    return render(request, "center/events.html", {"upcoming": upcoming, "past": past})

def event_detail(request, pk):
    item = get_object_or_404(Event, pk=pk)
    return render(request, "center/event_detail.html", {"item": item})

def opportunities(request):
    items = Opportunity.objects.filter(is_published=True)
    return render(request, "center/opportunities.html", {"items": items})

def projects(request):
    items = Project.objects.filter(is_published=True)
    return render(request, "center/projects.html", {"items": items})

def about(request):
    return render(request, "center/about.html")

def join(request):
    form = JoinForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        # This starter version confirms submission without sending/storing personal data.
        messages.success(request, "გმადლობთ! თქვენი შეტყობინება მიღებულია.")
        return redirect("join")
    return render(request, "center/join.html", {"form": form})
