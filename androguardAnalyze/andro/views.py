import subprocess
from django.conf import settings
from django.core.files.storage import default_storage
from django.shortcuts import render
from django.views import View
# Create your views here.
from .forms import UploadFileForm
from .models import Document


class Analyze(View):
    def get(self, request):
        form = UploadFileForm()
        return render(request, "andro/mainPage.html", {"form": form})

    def post(self, request):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            if not default_storage.exists(settings.MEDIA_ROOT + "/apks/" + str(file)):
                instance = Document(apk=request.FILES['file'])
                instance.save()
            process = subprocess.Popen(['python', 'test.py', str(file)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            output = process.stdout.read().decode('utf-8')
            output = output.split('breakAttribute')
            name = output[0]
            permissions = output[1]
            activities = output[2]
            signature = output[3]
            signature_name = output[4]
            return render(request, "andro/MainPage.html", {"form": form, "name": name, "permissions": permissions, "activities": activities, "signature": signature, "signature_name": signature_name})
        return render(request, "andro/MainPage.html", {"form": form})
