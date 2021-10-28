from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import songForm,userForm
from playwithmodels.models import User,song
from django.views import View
from django.views.generic import CreateView,UpdateView,DeleteView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class Home(View):
	def get(self,request):
		form=songForm()
		ctx={'form':form}
		return render(request,'playwithmodels/home.html',ctx)
	def post(self,request):
		form=songForm(request.POST)
		ctx={'form':form}
		if not form.is_valid():
			return HttpResponse('some error')
		song=request.POST['title']
		user=request.POST['user']
		author=User.objects.get(pk=user)
		print(author)
		form.save()
		return HttpResponse(f'song "{song}" save with author "{author}" success!')

class HomeU(View):
	def get(self,request):
		form=userForm()
		ctx={'form':form}
		return render(request,'playwithmodels/home.html',ctx)
	def post(self,request):
		form=userForm(request.POST)
		print(request.POST)
		ctx={'form':form}
		if not form.is_valid():
			return HttpResponse('some error')
		user=request.POST['name']
		form.save()
		return HttpResponse(f'User "{user}" saved !')

class SongList(ListView):
	model=song
	fields='__all__'
	success_url=' '


class CreateSong(LoginRequiredMixin,CreateView):
	model=song
	fields=['title']
	success_url='/CreateSong'

	def form_valid(self, form):
		u=self.request.user.id
		form.instance.user=User.objects.get(id=u)
		return super().form_valid(form)


class UpdateSong(LoginRequiredMixin,UpdateView):
	model=song
	fields='__all__'
	success_url='/ListSong'

class DeleteSong(DeleteView):
	model=song
	fields='__all__'
	success_url='/CreateSong'

	def get_queryset(self):
		return super(self.song.user==request.user).form_valid()


