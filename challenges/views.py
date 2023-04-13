from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


monthly_challenges = {
    "january" : "See boobies",
    "february" : "Hear boobies",
    "march" : "Feel boobies",
    "april" : "Squeeze boobies",
    "may" : "Taste boobies",
    "june" : "Bouncy boobies",
    "july" : "Big boobies",
    "august" : "Small boobies",
    "september" : "Soft boobies",
    "october" : "Smoosh boobie",
    "november" : "Love boobies",
    "december" : None
}

# Create your views here.

def index(request):
    months = list(monthly_challenges.keys())
    
    return render(request, "challenges/index.html", {
        "months" : months
    })

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("No boobies for this month!")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
    except:
        raise Http404()