from django.shortcuts import render, redirect
from models import User, Pet


# Create your views here.
def index(request):
	context= {
		'users': User.objects.all().order_by('-age'), 
		'pets': Pet.objects.all()
	}
	return render(request, 'main_app/index.html', context)

def newUser(request):
	return render(request, 'main_app/createUser.html')

def createUser(request):
	User.objects.create(name = request.POST['name'],age = request.POST['age'])
	return redirect('/')

def showUser(request, id):
	context = {
		'user': User.objects.get(id = id)
	}
	return render(request, 'main_app/show.html', context)

#######################pet stuff##################################################


def newPet(request):
	return render(request, 'main_app/createPet.html')



def createPet(request):
	Pet.objects.create(name = request.POST['name'])
	return redirect('/')


#######################pet  and user stuff##################################################



def adopt(request):
	pet1 = Pet.objects.get(id= request.POST['petid'])
	user1 = User.objects.get(id= request.POST['userid'])
	user1.pets.add(pet1)
	return redirect('/')









