from django.shortcuts import render

from .forms import EmailPostForm
from django.core.mail import send_mail
# Create your views here`
def index(request):
    context = None
    sent = False
    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            subject = "Отзыв о сайте nips"
            sender = form.cleaned_data['to']
            name = form.cleaned_data['name']
            messages = form.cleaned_data['comments']
            context = name

            message = "Отзыв от "+sender+"("+name+")"+" "+messages


            send_mail(subject, message, 'grekovdima7@gmail.com',['grekov_dima_89@mail.ru'])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'mainpage/firstpage.html', {
                                                    'form': form,
                                                    'sent': sent,
                                                    'name': context})
