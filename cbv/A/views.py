from typing import Any
from django.http.response import HttpResponse as HttpResponse 
from django.shortcuts import render
from django.views import View 
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.list import ListView
from .models import Car,Kelas,Food
from django.views.generic import DetailView , FormView , CreateView , DeleteView , UpdateView
from .forms import KelasForm
from django.urls import reverse_lazy





def roott(request):
    return HttpResponse('hello')



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
        return render(request,'method_not_allowed.html')        #alan ag runserver bokoni va beri too root mibini chon ba method get rafti behet on html custom shodeye khodfero neshoon mide 
    
'''
    templateview miad khieli sade b karbar template neshon mide va ag niaz bashe bvasash context ham ersal mikone
    az inja bayad ezafash konim------->     from django.views.generic.base import TemplateView
    
'''    







class Home(TemplateView):
    template_name='home.html'       #age kheili sade faghat mikhayd safeye html i neshon bedid az yek khat kod faghat estefade konid.
   
    ''' age khasti context ersal koni bayad az ye method estefade koni k tooye dele khode in templateview vojod dare 
        be esme    get_context_data()     bayad override beshe, behesh meghdar ezafe mikonim va dar akahar ham return esh mikonikm
        def get_context_data(self, **kwargs):
        kwargs.setdefault("view", self)
        if self.extra_context is not None:
            kwargs.update(self.extra_context)
        return kwargs
    '''
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)  # esme moteghayere context ro khodemon entekhab kardim . miaym toosh chi mirizim? hameye chizai k tooye class vaaled anjam shode bod ro mirizim tooye context, bad behesh y item jadid ezazfe mikonim  b esme `cars` ke mikhaym in cars hameye  etelaate modele car ro beehmon neshon bede va dar akhar ham on context ro return mikonim.
        context['cars'] = Car.objects.all()
        return context
    




#inja in class ro be url two vasl kardam. vaghti rooye barname mirim be url two, redirect mishe be safeye gooogle.com    
class Two(RedirectView):
    url = 'https://google.com'
#age bekhaym az namespaceha estefade konim bayad az patterm_name estefade konim bejaye line bala; intori    pattern_name='home:home'
    
    
    
    
    
class KelasList(ListView):
    template_name='kelas.html'
    model = Kelas
    context_object_name = 'Kelasha'         #esme ekhtesasie contex i k mikhaym befrestim b html
    ordering ='name'
    queryset = Kelas.objects.all()
    
    
    
'''
    DetailView ya bar asase primery key ya bar asase dlug mire etelaato mikhone miare va faghat yedone object ro barmigardoone.
'''    
class KelasDetail(DetailView):  
    model=Kelas
    context_object_name = 'joziat_kelas'
    template_name = 'kelasdetail.html'
    pk_url_kwarg = "pk"
    # slug_url_kwarg = "slug"
    # pk_url_kwarg = "pk"



class FormKelasView(FormView):
    form_class = KelasForm
    success_url=reverse_lazy('cbv:roott')         # This is the URL to redirect to after the form is successfully submitted and processed. reverse_lazy is used to resolve the URL.
    template_name='form.html'
    
    '''
        form_valid Method: This method is called when the submitted form is valid (i.e., it has passed all validations).
        Inside this method, self._create_new_kelas(data=form.cleaned_data) is called to create a new Kelas object with the cleaned data from the form.
        After creating the new Kelas object, it calls the parent class’s form_valid method to handle the standard behavior (like redirecting to the success URL).
    '''
    def form_valid(self,form):
        self._create_new_kelas(data=form.cleaned_data)
        return super().form_valid(form)
    
    
    '''
        _create_new_kelas Method: This is a helper method that takes the cleaned data from the form and creates a new Kelas object in the database.
    '''
    def _create_new_kelas(self, data):
        Kelas.objects.create(name=data['name'] , coach=data['coach'] , price=data['price'])
        
        

class FoodFormView(CreateView):
    model = Food
    fields = '__all__'
    success_url = reverse_lazy('cbv:food_list')
    template_name='foodform.html'
    
    
    
class FoodListView(ListView):
        queryset=Food.objects.all()
        template_name='foodlist.html'
        context_object_name='foods'
    

    
class DeleteFoodView(DeleteView):
    model = Food
    success_url=reverse_lazy('cbv:food_list')
    template_name='confirmdelete.html'
    
    
 
 
class UpdateFoodView(UpdateView):
    model = Food
    fields='__all__'
    success_url = reverse_lazy('cbv:food_list')
    template_name='foodupdate.html'