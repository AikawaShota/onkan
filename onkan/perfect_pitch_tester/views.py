from django.shortcuts import render


def index(request):
    return render(request, 'perfect_pitch_tester/index.html')
