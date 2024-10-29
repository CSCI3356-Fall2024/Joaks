from django.http import HttpResponse

def supervisor_required(view_func):
    def wrapper(request, *args, **kwargs):
        # Check if the user is authenticated and has the 'supervisor' role
        if request.user.is_authenticated and request.user.role == 'supervisor':
            return view_func(request, *args, **kwargs)
        # Return a restricted page message if the user is not a supervisor
        return HttpResponse("This page is restricted.")
    return wrapper