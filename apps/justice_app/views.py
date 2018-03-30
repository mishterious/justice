# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime, localtime
from .models import *
from django.contrib import messages
import bcrypt


def index(request):

    return render(request,'justice_app/login_reg.html')


def login_reg(request):


    return render(request,'justice_app/login_reg.html')


def add_user(request):
    errors = User.objects.basic_validator(request.POST)
    print "FROM USER", request.POST
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
    else: 
        myrequest = request.POST

        # need to Bcrypt our password
        hash1 = bcrypt.hashpw(myrequest['password'].encode('utf8'), bcrypt.gensalt())
        user = User.objects.create(name=myrequest['name'], alias=myrequest['alias'], email=myrequest['email'], password=hash1, birthday=myrequest['birthday'])
        user.save()
    return redirect('/')


def login(request):
    if request.method == 'POST':
        myrequest = request.POST
        user = User.objects.filter(email=myrequest['email'])
        
        if len(user) == 0:
            errors = {}
            errors['user_not_registered'] = "Your email was never found, please try again!"
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/')
        else:
            hash2 = user[0].password
            if bcrypt.checkpw(myrequest['password'].encode('utf8'), hash2.encode('utf8')):
                print "1232345323145"
                request.session['id'] = user[0].id
                request.session['name'] = user[0].name
                request.session['alias'] = user[0].alias
                request.session['email'] = user[0].email
                request.session['birthday'] = user[0].birthday
                request.session['login'] = True
                return redirect('/choose')
            else:
                errors = {}
                errors['no_password_found'] = "Password hasn't match with any that we have here. Please try again!"
                for tag, error in errors.iteritems():
                    messages.error(request, error, extra_tags=tag)
                return redirect('/')

def dashboard(request):
    me = User.objects.get(id=request.session['id'])

    data = {
        'user': User.objects.get(id=request.session['id']),
        'mywishes': Wish.objects.filter(user=request.session['id']),
        'changes': Change.objects.filter(user=request.session['id']),
        'madewishes': Change.objects.filter(users=request.session['id'])
    }

    return render(request, 'justice_app/dashboard.html', data)

def choose(request):
    data = {
        'user': User.objects.get(id=request.session['id']),
        'changes': Change.objects.all()
    }

    return render(request, 'justice_app/index.html', data)


def health(request):
    if request.method == 'POST':
        request.session['health'] = request.POST['health']

        ch = Change.objects.filter(each_change=request.session['health'])
        print ch
        # if len(ch) == 0:
        #     u = User.objects.get(id=request.session['id'])
        #     r = Change.objects.create(each_change=request.session['health'], user=u)
        #     r.save()
        #     errors = {}
        #     errors['user_not_registered'] = "Your email was never found, please try again!"
        #     for tag, error in errors.iteritems():
        #         messages.error(request, error, extra_tags=tag)
        #     return redirect('/choose')
        # else:
        this_user = User.objects.get(id=request.session['id'])
        this_change = Change.objects.get(id=request.POST['health'])
        this_change.users.add(this_user)
        return render(request, 'justice_app/health.html')


def music(request):
    if request.method == 'POST':
        request.session['music'] = request.POST['music']

        ch = Change.objects.filter(each_change=request.session['music'])
        
        # if len(ch) == 0:
        #     u = User.objects.get(id=request.session['id'])
        #     r = Change.objects.create(each_change=request.session['music'], user=u)
        #     r.save()
        #     errors = {}
        #     errors['user_not_registered'] = "Your email was never found, please try again!"
        #     for tag, error in errors.iteritems():
        #         messages.error(request, error, extra_tags=tag)
        #     return redirect('/choose')
        # else:
        this_user = User.objects.get(id=request.session['id'])
        this_change = Change.objects.get(id=request.POST['music'])
        this_change.users.add(this_user)
        return render(request, 'justice_app/music.html')


def travel(request):
    if request.method == 'POST':
        request.session['travel'] = request.POST['travel']

        ch = Change.objects.filter(each_change=request.session['travel'])
        
        # if len(ch) == 0:
        #     u = User.objects.get(id=request.session['id'])
        #     r = Change.objects.create(each_change=request.session['travel'], user=u)
        #     r.save()
        #     errors = {}
        #     errors['user_not_registered'] = "Your email was never found, please try again!"
        #     for tag, error in errors.iteritems():
        #         messages.error(request, error, extra_tags=tag)
        #     return redirect('/choose')
        # else:
        this_user = User.objects.get(id=request.session['id'])
        this_change = Change.objects.get(id=request.POST['travel'])
        this_change.users.add(this_user)
        return render(request, 'justice_app/travel.html')


def startup(request):
    if request.method == 'POST':
        request.session['startup'] = request.POST['startup']

        ch = Change.objects.filter(each_change=request.session['startup'])
        
        # if len(ch) == 0:
        #     u = User.objects.get(id=request.session['id'])
        #     r = Change.objects.create(each_change=request.session['startup'], user=u)
        #     r.save()
        #     errors = {}
        #     errors['user_not_registered'] = "Your email was never found, please try again!"
        #     for tag, error in errors.iteritems():
        #         messages.error(request, error, extra_tags=tag)
        #     return redirect('/choose')
        # else:
        this_user = User.objects.get(id=request.session['id'])
        this_change = Change.objects.get(id=request.POST['startup'])
        this_change.users.add(this_user)
        return render(request, 'justice_app/health.html')


def add_reason(request):
    errors = Wish.objects.basic_validator(request.POST)
    print "FROM USER", request.POST
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
    else: 
        u = User.objects.get(id=request.session['id'])
        r = Wish.objects.create(improve=request.POST['improve'], my_reason=request.POST['my_reason'], desc=request.POST['desc'], user=u)
        r.save()

        data = {
                'user': User.objects.get(id=request.session['id']),
            }
        return redirect('/dashboard')


# def music(request):
#     myrequest = request.POST

#     data = {
#         'user': User.objects.get(id=request.session['id']),
#     }

#     return render(request, 'justice_app/index.html', data)

# def travel(request):
#     myrequest = request.POST

#     data = {
#         'user': User.objects.get(id=request.session['id']),
#     }

#     return render(request, 'justice_app/index.html', data)

# def startup(request):
#     myrequest = request.POST

#     data = {
#         'user': User.objects.get(id=request.session['id']),
#     }

#     return render(request, 'justice_app/index.html', data)



def add_quote(request):
    errors = Quote.objects.basic_validator(request.POST)
    print "FROM USER", request.POST
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
    else: 
        myrequest = request.POST
        u = User.objects.get(id=request.session['id'])
        r = Quote.objects.create(insp=myrequest['insp'], quote_by=myrequest['quote_by'], user=u)
        r.save()

        return redirect('/quotes')

def see_user_posts(request, id):
    num = 0
    counter = list(Quote.objects.filter(user=id))
    
    for i in counter:
        num = num+1

    data = {
        'user': User.objects.get(id=id),
        'quote': Quote.objects.filter(user=id),
        'count': num
    }
    return render(request, 'justice_app/posts.html', data)


def remove(request, id):

    u = User.objects.get(id=request.session['id'])
    remove = Quote.objects.get(id=id)
    remove.users.remove(u)

    return redirect('/quotes')


def add_to_list(request, id):

    u = User.objects.get(id=request.session['id'])
    quote = Quote.objects.get(id=id)
    quote.users.add(u)

    return redirect('/quotes')


def logout(request):
    request.session.clear()
    return redirect('/')