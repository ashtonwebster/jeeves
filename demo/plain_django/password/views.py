from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
import pdb

from models import UserProfile, Password


#def index(request):

    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    #context = RequestContext(request, {
        #'latest_question_list': latest_question_list,
    #})
    #return HttpResponse(template.render(context))

@login_required
def index(request):
    profile = UserProfile.objects.get(username=request.user.username)
    return render_to_response(   "index.html"
           , RequestContext(request, { 'name' : profile.username } ))

@login_required
def passwords(request):
    # display all passwords for user
    profile = UserProfile.objects.get(username=request.user.username)
    passwords_list = Password.objects.filter(user=profile).all()
    return render_to_response("passwords.html", 
            RequestContext(request, {"passwords" : passwords_list}))
                
@login_required
def password(request):
    # enter a new password
    profile = UserProfile.objects.get(username=request.user.username)

    if request.method == 'POST':
        url = request.POST.get('url', None)
        password = request.POST.get('password', None)
        username = request.POST.get('username', None)

        if url == None or password == None or username == None:
            return render_to_response("password.html",
                RequestContext(request, {}));
        
        Password.objects.create(user=profile, site_url = url,
                site_username = username, site_password = password)
        return HttpResponseRedirect('passwords')

    elif request.method == 'GET':
        return render_to_response( 'password.html', 
                RequestContext(request, {}))
    else:
        raise Exception("invalid request type")



def register_account(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("index")

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()

            UserProfile.objects.create(
                username=user.username,
                email=request.POST.get('email', ''),
            )

            user = authenticate(username=request.POST['username'],
                         password=request.POST['password1'])
            login(request, user)
            return HttpResponseRedirect("index")
    else:
        form = UserCreationForm()

    return render_to_response("registration/account.html", RequestContext(request,
        {
            'form' : form,
            'which_page' : "register"
        }))

