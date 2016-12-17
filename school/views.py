from django.shortcuts import render
from django.template.defaultfilters import slugify
from .models import FeeCategory, Fee
from django.db.models import Count
# Create your views here.
import ipdb
def report(request):
	# fee_categories_slugify = [slugify(obj) for obj in FeeCategory.objects.all()]
	fee_categories = FeeCategory.objects.all()
	
	return render(request, 'pages/reports.html', {"fee_categories": fee_categories})



def fee(request):
	fee_type = request.GET.get('type').strip('/')
	records = Fee.objects.filter(fee_category__slug__iexact=fee_type)
	months = records.values('month').annotate(count=Count('month'))

	return render(request, 'pages/fee_reports.html', {"fees": records,"months":months})		
	# ipdb.set_trace()


