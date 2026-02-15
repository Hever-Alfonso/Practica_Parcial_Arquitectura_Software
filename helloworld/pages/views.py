from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import ProductForm


class HomePageView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "Home - Online Store",
            "subtitle": "Welcome Home",
        })
        return context


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "About us - Online Store",
            "subtitle": "About us",
            "description": "This is an about page ...",
            "author": "Developed by: Your Name",
        })
        return context


class Product:
    products = [
        {"id": "1", "name": "TV", "description": "Best TV", "price": 1200},
        {"id": "2", "name": "iPhone", "description": "Best iPhone", "price": 999},
        {"id": "3", "name": "Chromecast", "description": "Best Chromecast", "price": 49},
        {"id": "4", "name": "Glasses", "description": "Best Glasses", "price": 89},
    ]


class ProductIndexView(View):
    template_name = 'pages/products/index.html'

    def get(self, request):
        viewData = {}
        viewData["title"] = "Products - Online Store"
        viewData["subtitle"] = "List of products"
        viewData["products"] = Product.products
        return render(request, self.template_name, viewData)


class ProductShowView(View):
    template_name = 'pages/products/show.html'

    def get(self, request, id):
        # 1) Validar que id sea un número
        try:
            product_id = int(id)
        except (TypeError, ValueError):
            return HttpResponseRedirect(reverse("home"))

        # 2) Validar rango (porque tus ids son 1..len(Product.products))
        if product_id < 1 or product_id > len(Product.products):
            return HttpResponseRedirect(reverse("home"))

        # 3) Obtener producto seguro
        product = Product.products[product_id - 1]

        # 4) Preparar contexto
        viewData = {}
        viewData["title"] = product["name"] + " - Online Store"
        viewData["subtitle"] = product["name"] + " - Product information"
        viewData["product"] = product

        return render(request, self.template_name, viewData)


class ProductCreateView(View):
    template_name = 'pages/products/create.html'

    def get(self, request):
        viewData = {}
        viewData["title"] = "Create product"
        viewData["form"] = ProductForm()
        return render(request, self.template_name, viewData)

    def post(self, request):
        form = ProductForm(request.POST)

        # ✅ CLAVE: si es válido, renderiza el template nuevo con el mensaje
        if form.is_valid():
            viewData = {}
            viewData["title"] = "Product created"
            viewData["subtitle"] = "Product created"
            viewData["product"] = form.cleaned_data  # por si quieres mostrarlo
            return render(request, "pages/products/created.html", viewData)

        # Si NO es válido, vuelve a create mostrando errores
        viewData = {}
        viewData["title"] = "Create product"
        viewData["form"] = form
        return render(request, self.template_name, viewData)


class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "Contact - Online Store",
            "subtitle": "Contact Us",
            "email": "support@onlinestore.com",
            "address": "123 Main Street, Medellín, Colombia",
            "phone": "+57 300 123 4567"
        })
        return context