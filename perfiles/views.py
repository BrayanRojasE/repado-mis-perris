from django.shortcuts import render
from django.utils import timezone
from .models import RegistroRescatados

def post_list(request):
    RegistroRescatado = RegistroRescatados.objects.filter().order_by()
    return render(request, 'perfiles/post_list.htm', {'RegistroRescatado': RegistroRescatado})
