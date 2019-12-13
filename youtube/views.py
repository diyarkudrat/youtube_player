from django.shortcuts import render
from django.views.generic import TemplateView

from oauth2client.client import flow_from_clientsecrets, OAuth2WebServerFlow
from oauth2client.contrib import xsrfutil
from oauth2client.contrib.django_util.storage import DjangoORMStorage
from .models import CredentialsModel

class HomePageView(TemplateView):
    template_name = 'youtube/home.html'

class AuthorizeView(View):

    def get(self, request, *args, **kwargs):

        storage = DjangoORMStorage(
            CredentialsModel, 'id', request.user.id, 'credential')

        credential = storage.get()
        server_flow = OAuth2WebServerFlow(
            client_id = settings.GOOGLE_OAUTH2_CLIENT_ID,
            client_secret = settings.GOOGLE_OAUTH2_CLIENT_SECRET,
            url = 'https://www.googleapis.com/auth/youtube',
            redirect_uri = 'http://localhost:8888/oauth2callback/'
        )

    
