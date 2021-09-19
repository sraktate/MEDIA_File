from django.shortcuts import render,redirect
from .forms import DocumentForm
from .models import Document

def model_form_upload(request):
    form = DocumentForm()
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Home')
    template_name = 'app2/model_form_upload.html'
    context = {'form': form}
    return render(request,template_name,context)

def fileview(request):
    file = Document.objects.all()
    template_name = 'app2/uploade_file.html'
    context = {'file': file}
    return render(request,template_name,context)

 