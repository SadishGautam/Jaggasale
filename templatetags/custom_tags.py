from django import template

register = template.Library()

@register.filter(name='propertyImages')
def filter_range(start, end):
  return range(start, end)
