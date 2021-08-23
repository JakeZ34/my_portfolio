from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

#def me(request):
    #return render(request, 'me.html')

#def proj(request):
    #return render(request, 'proj.html')

#def tree(request):
    #return render(request, 'tree.html')

def linkedin(request):
    return render(request, )

def github(request):
    return render(request, 'https://github.com/JakeZ34')