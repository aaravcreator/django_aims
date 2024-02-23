from django.shortcuts import HttpResponse,render
import random

# view function
def index(request):
    if request.method =="POST":
        print(request.POST)
        username = request.POST.get('username')
        full_name = request.POST.get('full_name')
        print(f'Username is {username} and full name is {full_name}')
    random_value = random.randint(1,100)
    # return HttpResponse(f"OK FROM Django , the random value is <h1>{random_value}</h1>")
    context = {
        'random_data':random_value,
        'person_list':["RAM","SHYAM","HARI"]
    }
    return render(request,'index.html',context)


def account_view(request,username):

    return HttpResponse(f"THIS IS ACCOUNT PAGE of <h1>{username}</h1>")

def square(request,num):
    return HttpResponse(f"The square of <strong>{num}</strong> is {num*num}")