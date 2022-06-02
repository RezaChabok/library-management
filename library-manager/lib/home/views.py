
from django.shortcuts import render ,redirect
from .forms import LoginForm
from django.contrib.auth import login, authenticate, logout
from borrower.models import borrower_details
from books.models import book_manager
from shelf.models import shelf_details


def book_view(request,_isbn):
    if not request.user.is_authenticated:
        return redirect('/login')
    get_isbn =_isbn
    dbisbn = book_manager.objects.all().filter(isbn=get_isbn).first()
    book_address = shelf_details.objects.all().filter(id=dbisbn.id).first()
    context = {
        'book':dbisbn,
        'address':book_address,
    }
    print(book_address)
    return render(request,'home/book_detail.html',context)

def search_View(request):
    if not request.user.is_authenticated or not request.user.is_staff:
        return redirect('/login')


    context = {
        'search':None,
        'status':None,
    }

    if request.method == 'POST':
        from_time = request.POST.get('from')
        to_time = request.POST.get('to')
        book_title = request.POST.get('title')
        if from_time and to_time:
            context['search'] = borrower_details.objects.search(from_time ,to_time )
        if (book_title):
             context['status'] = book_manager.objects.get_status(book_title).first()
        print(context['status'])
    
    return render(request,'home/search.html',context)

def home_View(request):

    if not request.user.is_authenticated:
        return redirect('/login')

    list_borrower = borrower_details.objects.filter(userid__userid__id=request.user.id)
    list_borrowed = borrower_details.objects.filter(userstaff__userstaff__id=request.user.id)


    context = {
        'lb':list_borrower,
        'ld' : list_borrowed,
    }

   
    
    return render(request,'home/home.html',context)



def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')

    form_login = LoginForm(request.POST or None)

    if form_login.is_valid():
        username = form_login.cleaned_data.get('username')
        password = form_login.cleaned_data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            form_login.add_error('username', 'this username is not valid or not register')
    context = {
        'title': 'Login',
        'form_login': form_login
    }

    return render(request, 'home/user_login.html', context)

def log_out_user(request):
    logout(request)
    return redirect('/login')
