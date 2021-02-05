from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from variant.models import *
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.contenttypes.models import ContentType
from django.apps import apps
from django.forms.models import model_to_dict
from django.core.mail import send_mail




def home(request):
	return render(request, "variant/home.html")


def about(request):
	return render(request, "variant/about.html")

def contact(request):
	if request.method == "GET":
		form = ContactForm()
		return render(request, "variant/contact.html", {"form":form})

	form = ContactForm(request.POST)
	success = False
	if form.is_valid():
		name = form.cleaned_data["name"]
		email = form.cleaned_data["email"]
		message = form.cleaned_data["message"]
		try:
			send_mail(
					    "Website Inquiry",
					    name + "\n" + email + "\n" + message,
					    "admin@example.com",
					    ["admin@example.com"],
					    fail_silently=False,
					)
		except Exception as e:
			print(e)
		success = True


	return render(request, "variant/contact.html", {"form":form, "success":success})

def search(request):
	context = {}
	if not "q" in request.GET or request.GET["q"] == "":
		return render(request, "variant/search.html", context)
	text = request.GET["q"]
	results = Main.objects.filter(
		Q(variant_id__icontains=text) | Q(gene__icontains=text) | Q(variant_type__icontains=text) | Q(chromosome__icontains=text)
		)
	paginator = Paginator(results, 10)
	
	page_number = 1
	if "page" in request.GET:
		page_number = request.GET["page"]
	
	page_obj = paginator.get_page(page_number)
	context["page_obj"] =  page_obj
	context["q"] = text


	return render(request, "variant/search.html", context)

def advanced_search(request):
	fields = [field.name for field in Main._meta.get_fields()]
	fields.insert(4, "base_position")
	context = {"fields": fields,
				 "params":{**dict(request.GET.items())}}
	if not "q1" in request.GET or request.GET["q1"] == "":
		return render(request, "variant/advanced_search.html", context)
	text = request.GET["q1"]
	if request.GET["f1"] == "base_position":
		text += ":"
	lookup = "%s__icontains" % ("chromosome" if request.GET["f1"] == "base_position" else request.GET["f1"])
	query = Q(**{lookup: text})
	querys = list(request.GET.keys())[2:]
	page_number = 1
	if "page" in querys[-1]:
		querys.pop()
		page_number = request.GET["page"]
	for i in range(0, len(querys), 3):
		lookup = "%s__icontains" % ("chromosome" if request.GET[querys[i+1]] == "base_position" else request.GET[querys[i+1]]) 
		text = request.GET[querys[i+2]]
		if request.GET[querys[i+1]] == "base_position":
			text += ":"
		qObj = Q(**{lookup: text})
		operator = request.GET[querys[i]]
		query.add(~qObj if operator == "NOT" else qObj, Q.OR if operator == "OR" else Q.AND)	
	results = Main.objects.filter(query)
	paginator = Paginator(results, 10)				
	page_obj = paginator.get_page(page_number)
	context["page_obj"] =  page_obj
	
	return render(request, "variant/advanced_search.html", context)

def detail(request, gene, variant):
	gene = gene.capitalize()
	z = ContentType.objects.get(model=gene)
	model = apps.get_model(z.app_label, gene)
	variant = model.objects.get(variant_id=variant)
	variant_dict = model_to_dict(variant)
	variant_fields = list(variant_dict.keys())
	return render(request, "variant/detail.html", {"variant":variant, "variant_dict":variant_dict, "variant_fields":variant_fields})
	


