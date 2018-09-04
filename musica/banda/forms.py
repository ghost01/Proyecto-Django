from django import forms
from .models import Producto, Perfil
from django.contrib.auth.models import User 


class contacto_form(forms.Form):
	correo = forms.EmailField(widget = forms.TextInput(attrs={"class":"form-control"}))
	titulo = forms.CharField(widget = forms.TextInput(attrs={"class":"form-control"}))
	texto = forms.CharField(widget = forms.Textarea(attrs={"class":"form-control"}))

class login_form(forms.Form):
	usuario = forms.CharField(widget = forms.TextInput( attrs={"class":"form-control"}))
	clave   = forms.CharField(widget = forms.PasswordInput(render_value=False, attrs={"class":"form-control"}))

class agregar_producto_form(forms.ModelForm):
	class Meta:
		model = Producto
		fields = '__all__'

class register_form(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
	email = forms.EmailField(widget=forms.TextInput(attrs={"class":"form-control"}))
	password_1 = forms.CharField(label= 'Password',widget=forms.PasswordInput(render_value=False, attrs={"class":"form-control"}))
	password_2 = forms.CharField(label= 'Confirmar Password',widget=forms.PasswordInput(render_value=False, attrs={"class":"form-control"}))

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			u = User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError('Nombre de Usuario ya Registrado')

	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			email = User.objects.get(email=email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError('Correo Electronico ya Existe')

	def clean_password_2(self):
		password_1 = self.cleaned_data['password_1']
		password_2 = self.cleaned_data['password_2']

		if password_1 == password_2:
			pass
		else:
			raise forms.ValidationError('Los password no coinciden')

class perfil_form(forms.ModelForm):
	class Meta:
		model = Perfil
		fields = ['imagen', 'documento','edad']
		exclude = ['user']
