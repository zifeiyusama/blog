from django.shortcuts import render

# Create your views here.
def preview(request):
    return render(request, 'editor/editor.html')
