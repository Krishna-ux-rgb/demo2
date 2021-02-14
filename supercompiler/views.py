from django.shortcuts import render
from .forms import InputForm
# Create your views here.
import requests
import json



def compilerapp(request):
    iff = InputForm()
    return render(request , "supercompiler/compilerhome.html" , {'inputForm' : iff})

def executeTheCode(request):
    if request.method == 'POST':
        iff = InputForm(request.POST)
        if iff.is_valid():
            code = iff.cleaned_data['inputArea']
            lang = iff.cleaned_data['language']
            version = iff.cleaned_data['version']
            payload = {'clientId' : "9583a02cf6e53497a4ecea8ad7b7f424" , "clientSecret" : "aecfecefad5209437415aa51649420aa5ab4b4fd7b041d591964e2e9db475fdc" , 'script' : code, 'language' : lang, "versionIndex" : version }
            headers = {'content-type' : 'application/json'}
            response = requests.post("https://api.jdoodle.com/v1/execute" , data = json.dumps(payload) , headers = headers)
            result = json.loads(response.text)
        return render(request, "supercompiler/compilerhome.html" , {'inputForm' : iff , 'result' : result['output']} )

