from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

#def proj(request):
    #return render(request, 'proj.html')

#def tree(request):
    #return render(request, 'tree.html')