from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return None


@register.filter
def int_to_k(value):
    try:
        value = float(value)
        if value >= 1000:
            return f"{value / 1000:.1f}k".rstrip('0').rstrip('.')
        return str(int(value)) 
    except (ValueError, TypeError):
        return value
