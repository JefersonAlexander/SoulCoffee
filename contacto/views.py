
from django.shortcuts import redirect, render
from django.core.mail import EmailMessage
from .forms import FormularioContacto

# Create your views here.
def contacto(request):
    formulario_contacto= FormularioContacto()
    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            telefono=request.POST.get("telefono")
            contenido=request.POST.get("contenido")

            email=EmailMessage("Mensaje desde la app soul coffee",

            "El usuario con nombre {} con la dirección {} escribe lo siguiente: \n\n {}".format(nombre,email,contenido),

            "", ["    "], reply_to=[email]) 
           
            try:
               email.send()
               return redirect("/contacto/?valido")

            except:
                  return redirect("/contacto/?novalido")
    
    return render(request, "contacto/contacto.html", {'miFormulario':formulario_contacto})
