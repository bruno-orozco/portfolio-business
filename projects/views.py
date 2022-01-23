from inbox.forms import *
from django.views.generic.edit import FormView
from django.views.generic import *
from projects.models import *

# Create your views here.

class formContact(FormView):
    """ Contact form view """

    template_name = 'contact.html'
    form_class = formMessage
    success_url = '/thanks/'

    def form_valid(self, form):
        """ Save form if is valid """

        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super().form_valid(form)

class thanks(TemplateView):
    """ Template redirect Contact  """

    template_name = "thanks.html"

class analyst(TemplateView):
    """ test """
    template_name = "analyst.html"

class UserDetailView(DetailView):
    """ Show the full content of the post"""
    
    queryset = post.objects.all() 

    template_name = 'projects.html'

    slug_field = 'title'

    slug_url_kwarg = 'title'

    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        """Add user's posts to context."""

        context = super().get_context_data(**kwargs)
        title = self.get_object()
        context['title'] = post.objects.filter(title=title)
        
        return context