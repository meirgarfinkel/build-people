from django import template
from datetime import datetime, timezone

register = template.Library()


@register.inclusion_tag("build_people/partials/comments_list.html", takes_context=True)
def render_comments_list(context):
    """Renders the comments section for a given recognition."""
    return {"recognition": context.get("recognition"), "user": context.get("user"), "request": context.get("request")}


@register.inclusion_tag("build_people/partials/recognitions_list.html", takes_context=True)
def render_recognitions_list(context):
    """Renders the recognitions list for the users company."""
    return {"recognitions": context.get("recognitions"), "user": context.get("user"), "request": context.get("request")}


@register.inclusion_tag("build_people/partials/recognition_form.html", takes_context=True)
def render_recognition_form(context):
    """Renders the recognition form."""
    return {"user": context.get("user"), "request": context.get("request")}


@register.inclusion_tag("build_people/partials/heart_button.html", takes_context=True)
def render_heart_button(context):
    return {"recognition": context.get("recognition"), "user": context.get("user"), "request": context.get("request")}


@register.filter
def days_since(value):
    """Custom filter to show only days from timesince, with 'Today' for same-day values."""
    if not value:
        return ""

    now = datetime.now(timezone.utc)
    diff = now - value

    if diff.days == 0:
        return "Today"
    elif diff.days == 1:
        return "Yesterday"
    
    return f"{diff.days} days ago"
