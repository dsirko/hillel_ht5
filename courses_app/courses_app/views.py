from django.shortcuts import render


def courses_page(request):
    return render(request, 'courses_page.html')
