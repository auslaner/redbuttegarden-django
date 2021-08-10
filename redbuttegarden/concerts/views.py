from django.shortcuts import render, redirect


def concerts(request):
    return render(request, 'concerts/concert_page.html')

def concert_thank_you(request):
    referer = request.META.get('HTTP_REFERER')
    if referer and 'etix.com' in referer:
        return render(request, 'concerts/concert_thank_you.html')
    else:
        return redirect('/')
