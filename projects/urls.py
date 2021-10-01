from django.urls import path
from . import views

urlpatterns = [
    path('AllProjects/', views.all_projects_view, name='AllProjects' ),
    path('AddProject/', views.add_project_view, name='AddProject'),
    path('SingleProject/<str:pk>', views.single_project_view, name='SingleProject'),
    path('EditProject/<str:pk>', views.edit_project_view, name='EditProject'),
    path('DeleteProject/<str:pk>', views.delete_project_view, name='DeleteProject'),

]
