from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def portal(request):
    return render(request, 'projportal.html')

#def me(request):
    #return render(request, 'me.html')

#def proj(request):
    #return render(request, 'proj.html')

#def tree(request):
    #return render(request, 'tree.html')
