from django import template

register = template.Library()

import calendar

@register.filter
def month_name(month_number):
    return calendar.month_name[month_number]

@register.filter(name='times') 
def times(number):
    return range(number)