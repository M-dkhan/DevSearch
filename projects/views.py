from django.http import response
from django.shortcuts import render,redirect

from projects.models import Projects
from .forms import AddProjectForm
# Create your views here.
def all_projects_view(request):
    
    projects = Projects.objects.all()
    
    context = {
        'projects':projects,
    }
    return render(request, 'projects/AllProjects.html', context)


def add_project_view(request):
    form = AddProjectForm()

    if request.method == 'POST':
        form = AddProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AllProjects')
    context = {
        'form':form,
    }
    return render(request, 'projects/AddProject.html',context)

def single_project_view(request, pk):
    project = Projects.objects.get(id=pk)

    context = {
        'project':project,
    }

    return render(request, 'projects/single_project.html', context)


def edit_project_view(request, pk):
    project = Projects.objects.get(id=pk)
    form = AddProjectForm(instance=project)
    
    if request.method == 'POST':
        form = AddProjectForm(request.POST, instance=project) 
        if form.is_valid():
            form.save()
            return redirect('AllProjects')
    context = {
        'project':project,
        'form':form,
    }
    return render(request, 'projects/EditProject.html', context)


def delete_project_view(request, pk):
    project = Projects.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('AllProjects')

    context = {
        'project':project,
    }

    return render(request, 'projects/DeleteProject.html', context)