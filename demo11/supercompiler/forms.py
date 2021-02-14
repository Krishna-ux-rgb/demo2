from django import forms


class InputForm(forms.Form):
    inputArea = forms.CharField(widget= forms.Textarea(attrs= {'style' : 'height : 500px; width : 650px ; font-size : 22px;'  }))
    choiceList = (('c99','C-99'),('python3','Python3'),('cpp',"C++"),('java','Java'))
    versions = (('0','JDK 1.8.0_66'),('1','JDK 9.0.1'),('2','JDK 10.0.1'),('0','GCC 5.3.0'),('1','GCC 7.2.0'),('2','GCC 8.1.0'),('0','Python3.5.1'),('1','Python3.6.3'),('2','Python3.6.5'))
    language = forms.ChoiceField(choices = choiceList)
    version = forms.ChoiceField(choices = versions)
