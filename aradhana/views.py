from django.shortcuts import render,redirect,get_object_or_404
from .models import Student, Event
# Create your views here.
def index(request):
	students = Student.objects.all()
	events = Event.objects.all().order_by('name','category')
	context={'event_len':len(events),'students':len(students),'events':events}
	return render(request,'aradhana/details.html',context=context)

def events(request,eventID):
	event=get_object_or_404(Event,pk=eventID)
	students=event.student_set.all().order_by('name','school')
	total=len(students)
	context={'event':event,'students':students,'total':total}
	return render(request,'aradhana/event.html',context=context)