from django.shortcuts import render

# Create your views here.

def lista_productos(request):
    productos=[
        {'nombre':'camisa', 'precio':20, 'en_oferta':True},
        {'nombre':'Pantalon', 'precio':10, 'en_oferta':False},
        {'nombre':'Blusa', 'precio':70, 'en_oferta':True},
        {'nombre':'Zapatos', 'precio':1000, 'en_oferta':True},

    ]
    return render(request,'productos/lista_productos.html',{'productos':productos})