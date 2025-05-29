from django import template
from django.utils.timezone import now

register = template.Library()


@register.filter
def time_since_custom(value):
    delta = now() - value

    if delta.days >= 1:
        return f"{delta.days} day{'s' if delta.days != 1 else ''} ago"

    elif delta.seconds >= 3600:
        hours = delta.seconds // 3600
        return f"{hours} hour{'s' if hours != 1 else ''} ago"

    elif delta.seconds >= 60:
        minutes = delta.seconds // 60
        return f"{minutes} minute{'s' if minutes != 1 else ''} ago"
    else:
        return f"Just now"