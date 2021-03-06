from django.shortcuts import render_to_response
from django.template import RequestContext
from polls.forms import PollForm
from polls.models import Poll
from django.http import HttpResponse
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver




def view_index(request):
	form = PollForm()
	if request.method == "POST":
		form = PollForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse("<h4>El registro se agrego correctamente</h4><br><br><a href='/'>Agregar uno nuevo</a>")
		else:
			return render_to_response("index.html",{'form':form},
				context_instance=RequestContext(request))
			
	else:
		return render_to_response("index.html",{'form':form},
			context_instance=RequestContext(request))


@receiver(pre_save, sender=Poll)
def my_handler_pre(sender, **kwargs):
	print "Se va a agregar un registro"

@receiver(post_save, sender=Poll)
def my_handler_post(sender, **kwargs):
	print "Se ha agregado un registro"
