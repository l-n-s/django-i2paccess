django-i2paccess
================

Control which I2P destinations are allowed to use your Django application.

Can be used to create private I2P webapps and to fight spam in I2P with 
PoW-like concept.

 
Installation
------------

    $ pip3 install https://github.com/l-n-s/django-i2paccess/zipball/master

Usage
-----

In your `settings.py` files add the following config:

    I2P_ACCESSLIST = {
        "whitelist": ["choosenone1pgcujqsk22hpxgyq3t6gjnu4wcu6cqagtame2spoq"],
        "blacklist": ["bob6d4psz73qurfnzv2tivotzxx63nylwdvsxrywpemxqedzk4wa"],
        "regex": "bob",
    }

All options are reqired, could be empty of course.

* whitelist -- list of allowed destinations
* blacklist -- list of blocked destinations
* regex     -- destinations which are started with this string are allowed

In your `views.py` you can now import and use decorator or mixin to restrict
access to specific views:

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


