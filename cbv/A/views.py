from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from django.views import View
# Create your views here.


'''
    class View chandta method dare mesle http_not_allowed() , setup() , dispatch() , option()     
    option() baraye neshoon dadae header hast 
    age beri tooye mostanadate class View , mitoni code haye method option ro bbini ke inan:
    
        def options(self, request, *args, **kwargs):
        response = HttpResponse()
        response.headers["Allow"] = ", ".join(self._allowed_methods())
        response.headers["Content-Length"] = "0"
        if self.view_is_async:
            async def func():
                return response
            return func()
        else:
            return response
    
    
    
    hala ag bkhaym method option ro custom konim masalan b headers hash item ezafe konimm bayad method option ro override bokonim
'''




class ghazal(View):
    def post(self,request):
        return render(request,'ghazal.html')

    def options(self, request, *args, **kwargs):
        response= super().options(request, *args, **kwargs)
        #hala az in response b header ha dastresi dariim
        response.headers['host'] = 'localhost'
        response.headers['user'] = request.user
        return response
    
    
    #method http_method_not_allowed() zamani ejra mishe k on method ro ma behesh dastresi nadade bashim vali darkhast behesh ersal shode besorate default code sh ine:
        """
            def http_method_not_allowed(self, request, *args, **kwargs):
        logger.warning(
            "Method Not Allowed (%s): %s",
            request.method,
            request.path,
            extra={"status_code": 405, "request": request},
        )
        response = HttpResponseNotAllowed(self._allowed_methods())
        """
    #ma mitoonim hartori k khastim custom esh konim
    def http_method_not_allowed(self, request, *args, **kwargs):
        return render(request,'method_not_allowed.html')