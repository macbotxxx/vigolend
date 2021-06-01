from .models import TeamMember
from django.shortcuts import render


def index(request):
    """
    View function for rendering homepage
    """
    return render(
        request, 'pages/home.html'
    )

def borrow(request):
    """
    View function for rendering Borrower page
    """
    return render(
        request, 'pages/borrow.html'
    )

def invest(request):
    """
    View function for rendering Invest page
    """
    return render(
        request, 'pages/invest.html'
    )

def about_us(request):
    """
    View function for rendering about us page
    """
    all_teams = TeamMember.objects.all()

    context = {
        'all_teams':all_teams,
    }
    return render(
        request, 'pages/about.html', context
    )

def teams(request):
    """
    View function for rendering our teams page
    """

    return render(
        request, 'pages/home.html', 
    )
