from .models import Project

def assigned_projects(request):
    user = request.user
    projects = user.members.all()
    return {'projects': projects}
