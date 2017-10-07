from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponseForbidden

class I2PAccessRestrictedMixin(object):
    """
    Mixin which restricts access for everybody, except whitelisted
    """
    redirect_url = None

    def dispatch(self, request, *args, **kwargs):
        b32 = request.META["HTTP_X_I2P_DESTB32"][:-8]

        if b32 in settings.I2P_ACCESSLIST["whitelist"]:
            return super(I2PAccessRestrictedMixin, self).dispatch(request,
                    *args, **kwargs)

        if settings.I2P_ACCESSLIST["regex"] and \
                b32.startswith(settings.I2P_ACCESSLIST["regex"]) and \
                b32 not in settings.I2P_ACCESSLIST["blacklist"]:
            return super(I2PAccessRestrictedMixin, self).dispatch(request,
                    *args, **kwargs)

        if not self.redirect_url: return HttpResponseForbidden()
            
        return HttpResponseRedirect(self.redirect_url)

