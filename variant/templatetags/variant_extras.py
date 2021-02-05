from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='split')
def split(value, arg=" "):
	return value.split(arg)

@register.filter(name="split_on_new_line")
def split_on_new_line(value):
	return value.split("\n")

@register.filter(name='index')
def index(value, arg):
	return value[arg]

@register.filter(name='strip')
def strip(value):
	return value.strip()

@register.filter(name="get_flanks")
def get_flanks(value):
	if "None" in value:
		return "None"
	if "Flanks" in value:
		result = value.split("Flanks]")[1].strip()
	else:
		result = " ".join(value.split()[1:]).strip()

	html_result = "<br>".join(result.split("\n")[:2]) + "<br>"
	html_result += "<span style='color: red;'>" + result.split("\n")[2] + "</span><br>"
	html_result += "<br>".join(result.split("\n")[3:])

	return mark_safe(html_result)
	

@register.filter(name="get_genes")
def get_genes(value):
	return " ".join(x for x in value.split() if "IL" in x)

@register.filter(name="get_clinical")
def get_clinical(value):
	if "Not" in value:
		return value

	html_result = "Reported in "
	html_result += "<a href='" + value.split("|")[1] + "'> ClinVar </a>"
	return mark_safe(html_result)

@register.filter(name="replace")
def replace(value, args):
	return value.replace(args.split(",")[0], args.split(",")[1])

# @register.filter(name=get_table)
# 	html = <table>
# 	return 