from .models import Project

def assigned_projects(request):
    if request.user.is_authenticated:
        user = request.user
        projects = user.members.all()
        return {'projects': projects}
    else:
        return {'projects': []}
