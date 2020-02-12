from django import forms
#Importo la libreria forms

#creo una clase form que va a ser el formulario, en lugar de heredar de model hereda de form
class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu nombre'}
    ), min_length=3, max_length=100) #El widget nos permite decorar el text imput, el attrs son los atributos y traemos la clase form-control de bootstrap
    email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu mail'}), min_length=3, max_length=100)
    phone = forms.CharField(label="Telefono", required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu telefono'}
    ), min_length=3, max_length=100)
    subject = forms.CharField(label="Asunto", required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Escribe el asunto'}
    ), min_length=3, max_length=100)
    content = forms.CharField(label="Contenido", required=True, widget=forms.Textarea(
        attrs={'class':'form-control', 'rows': 3, 'placeholder':'Escribe tu mensaje'}
        ), min_length=3, max_length=1000)