from functools import wraps

from django.conf import settings
from django.utils.decorators import available_attrs
from django.http import HttpResponseRedirect, HttpResponseForbidden


def restrict_with_redirect(redirect_url=None):
    """
    Decorator for views that checks b32 of incoming connection
    redirecting to the URL if necessary. 
    """

    def decorator(view_func):
        @wraps(view_func, assigned=available_attrs(view_func))
        def _wrapped_view(request, *args, **kwargs):
            b32 = request.META["HTTP_X_I2P_DESTB32"][:-8]

            if b32 in settings.I2P_ACCESSLIST["whitelist"]:
                return view_func(request, *args, **kwargs)

            if settings.I2P_ACCESSLIST["regex"] and \
                    b32.startswith(settings.I2P_ACCESSLIST["regex"]) and \
                    b32 not in settings.I2P_ACCESSLIST["blacklist"]:
                return view_func(request, *args, **kwargs)

            if not redirect_url: return HttpResponseForbidden()
                
            return HttpResponseRedirect(redirect_url)
        return _wrapped_view
    return decorator

restricted = restrict_with_redirect()

