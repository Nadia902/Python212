from django.shortcuts import render
import requests


def exchange(request):
    url = 'https://api.exchangerate.host/latest'
    response = requests.get(url).json()
    currencies = response.get('rates')

    if request.method == 'GET':
        context = {
            'currencies': currencies
        }
        return render(request, context=context, template_name='exchange/index.html')

    if request.method == 'POST':
        from_amount = request.POST.get('from-amount')
        from_curr = request.POST.get('from-curr')
        to_curr = request.POST.get('to-curr')

        context = {
            'currencies': currencies,
            'from_curr': from_curr,
            'to_cur': to_curr
        }
        return render(request, context=context, template_name='exchange/index.html')