# Import here
import datetime
from collections import defaultdict

from django.db.models import Avg, Sum, Count

from store.models import Employee, Product, Order


def young_employees(job: str):
    return Employee.objects.filter(age__lt=30, job=job)


def cheap_products():
    average_price = Product.objects.aggregate(Avg("price", default=0))
    return Product.objects.filter(price__lt=average_price['price__avg']).order_by('price').values_list('name', flat=True)


def products_sold_by_companies():
    return Product.objects.values('company__name').annotate(total_products=Sum('sold')).values_list('company__name', 'total_products')

def sum_of_income(start_date: str, end_date: str):
    return Order.objects.filter(time__gte=start_date, time__lte=end_date).aggregate(Sum('price'))['price__sum']
 

def good_customers():
    last_month = datetime.datetime.today() - datetime.timedelta(days=30)
    return Order.objects.filter(time__gt=last_month).values('customer').annotate(total_tx=Count('id')).filter(total_tx__gt=10).values_list('customer__name', 'customer__phone')


def nonprofitable_companies():
    return Product.objects.filter(sold__lt=100).values('company').annotate(total=Count('id')).filter(total__gte=4).values_list('company__name', flat=True)
