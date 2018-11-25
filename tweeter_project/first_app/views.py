from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import User, Tweet
from . import forms

# Create your views here.
def index(request, N=20):
    data = Tweet.objects.all().order_by('date')[:N]
    arg = {'tweet': data}
    return render(request, 'index.html', arg)

def form_user_view(request):
	form = forms.NewUserForm()
	if request.method == 'POST':
		form = forms.NewUserForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return index(request)
		else:
			print('Error -form is invalid')
	return render(request, 'form.html', {'form': form})

'''def form_name_view(request):
	form = forms.FormName()

	# use flask to get data
	if request.method == 'POST':
		form = forms.FormName(request.POST)
		if form.is_valid():
			print('validation success')
			print('NAME : {}'.format(form.cleaned_data['name']))
			print('EMAIL : {}'.format(form.cleaned_data['email']))
			print('TEXT : {}'.format(form.cleaned_data['text']))

	return render(request,'form.html',{'form':form})'''




