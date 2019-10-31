from .forms import PostForm
from django.utils import timezone
from .models import Persona
from django.shortcuts import render, get_object_or_404, redirect
def post_list(request):
    personas = Persona.objects.all().order_by('published_date')
    return render(request, 'blog/post_list.html', {'personas': personas})

def post_detail(request, pk):
    persona = get_object_or_404(Persona, pk=pk)
    return render(request, 'blog/post_detail.html', {'persona': persona})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            persona = form.save(commit=False) 
            persona.published_date = timezone.now()
            persona.save()
            return redirect('post_detail', pk=persona.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    persona = get_object_or_404(Persona, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            persona.published_date = timezone.now()
            persona.save()
            return redirect('post_detail', pk=persona.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def post_draft_list(request):
    personas = Persona.objects.filter(published_date__isnull=True).order_by('fecha_de_alta')
    return render(request, 'blog/post_draft_list.html', {'personas': personas})

def post_publish(request, pk):
    persona = get_object_or_404(Persona, pk=pk)
    persona.publish()
    return redirect('post_detail', pk=pk)

def post_remove(request, pk):
    persona = get_object_or_404(Persona, pk=pk)
    persona.delete()
    return redirect('post_list')


def search(request):  
    dni_busqueda =  request.GET.get('search')
    resultados = Persona.objects.filter(dni=dni_busqueda)
    return render(request,"blog/busqueda.html",{'resultados':resultados})





