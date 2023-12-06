# not used 
from django import template

register = template.Library()

@register.filter(name="add_space")
def add_space(value):
    if "AM" in value:
        return value.replace("AM", " AM")
    elif "PM" in value:
        return value.replace("PM", " PM")
    return value