from django import template
from django.utils.safestring import mark_safe
from django.conf import settings
import os

register = template.Library()


@register.simple_tag
def heroicon(name, **attrs):
    icon_path = os.path.join(settings.BASE_DIR, 'theme', 'static', 'theme', 'icons', f'{name}.svg')

    try:
        with open(icon_path, encoding='utf-8') as f:
            svg = f.read()

            if attrs:
                start = svg.find('<svg')
                end = svg.find('>', start)
                tag = svg[start:end+1]

                extra_attrs = ' '.join(f'{key}="{value}"' for key, value in attrs.items())
                new_tag = tag[:-1] + ' ' + extra_attrs + '>'

                svg = svg.replace(tag, new_tag, 1)

            return mark_safe(svg)
    except FileNotFoundError:
        return f'<!-- Icon {name}.svg not found -->'


@register.filter(name="add_class")
def add_class(field, css_class):
    existing_classes = field.field.widget.attrs.get("class", "")
    all_classes = f"{existing_classes} {css_class}".strip()
    return field.as_widget(attrs={"class": all_classes})


@register.filter
def get_attr(obj, attr_name):
    return getattr(obj, attr_name)
