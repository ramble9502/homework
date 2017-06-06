from django.shortcuts import render,redirect
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .form import UserForm, UserProfileForm, LmessageForm
from .models import *
from django.shortcuts import get_object_or_404
import datetime
from django.http import HttpResponseForbidden
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@csrf_protect
def index(request):
    return render(request, 'index.html', locals())


@csrf_protect
def register(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return HttpResponseRedirect('/accounts/login')

        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'register_index.html', {'user_form': user_form, 'profile_form': profile_form})


@csrf_protect
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/accounts/login')


def login(request):

    if request.user.is_authenticated():
        return HttpResponseRedirect('/index/')

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/index/')
    else:
        return render_to_response('login.html')


@login_required
def get_user_profile(request):
    user = get_object_or_404(User, username=request.user)
    return render(request, 'userindexpage.html', {"user": user})


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/accounts/login')


@login_required
def divelayout(request):
    lmessage = Lmessage.objects.all()
    user = get_object_or_404(User, username=request.user)
    extra_context = {"bartenderstory": bartenderstory,
                     "user": user, "lmessage": lmessage}
    return render_to_response('dive_index.html', extra_context)


@login_required
def bartenderstory(request):
    bartenderstory = StoryOfBartender.objects.all()
    user = get_object_or_404(User, username=request.user)
    extra_context = {"bartenderstory": bartenderstory, "user": user}
    return render_to_response("bartenderstory_index.html", extra_context)


@login_required
def brewwine(request):
    brewwine = BrewWine.objects.all()
    user = get_object_or_404(User, username=request.user)
    extra_context = {"brewwine": brewwine, "user": user}
    return render_to_response("brewwine_index.html", extra_context)


@csrf_exempt
def create_lmessage(request):
    if request.method == 'POST':
        date_time = datetime.datetime.now()
        comment = request.POST['comment']
        user = User.objects.get(username=request.POST['user'])
        Lmessage.objects.create(user=user, datetime=date_time, comment=comment)
    return render_to_response('dive_index.html',locals())


@csrf_exempt
def record_dive_score(request):
    if request.method == 'POST':
        date_time=datetime.datetime.now()
        score=request.POST['score']
        user=User.objects.get(username=request.POST['user'])
        Divescore.objects.create(user=user,datetime=date_time,score=score)
    return render_to_response('dive_index.html',locals())



@csrf_exempt
def record_test_score(request):
    if request.method == 'POST':
        date_time=datetime.datetime.now()
        score=request.POST['score']
        user=User.objects.get(username=request.POST['user'])
        Testscore.objects.create(user=user,datetime=date_time,score=score)
    return render_to_response('question_index.html',locals())





def lmessage_layout(request):
    user = get_object_or_404(User, username=request.user)
    lmessage=Lmessage.objects.order_by('-datetime')
    extra_context={'lmessage':lmessage,"user":user}
    return render_to_response('lmessage_index.html',extra_context)



@login_required
def deletecomment(request,id):
    obj=Lmessage.objects.get(pk=id);
    obj.delete()
    return redirect('/lmessage_layout')


def questionask(request):
    user = get_object_or_404(User, username=request.user)
    extra_context={'user':user}
    return render_to_response('question_index.html',extra_context)



@login_required
def testscorelayout(request):
    user = get_object_or_404(User, username=request.user)
    testscore=Testscore.objects.order_by('-datetime')
    extra_context={'user':user,'testscore':testscore}
    return render_to_response('test_score.html',extra_context)


@login_required
def divescorelayout(request):
    user = get_object_or_404(User, username=request.user)
    divescore=Divescore.objects.order_by('-datetime')
    extra_context={'user':user,'divescore':divescore}
    return render_to_response('dive_score.html',extra_context)


