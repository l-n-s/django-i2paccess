from django.http import HttpResponse
from django.views import View

from i2paccess.decorators import restricted
from i2paccess.mixins import I2PAccessRestrictedMixin

@restricted
def secretfunction(request):
    return HttpResponse("This page is top secret!")

class SecretClass(I2PAccessRestrictedMixin, View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("This page is top secret!")

