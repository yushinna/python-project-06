from django import template

register = template.Library()


@register.filter()
def get_fields(obj):
    field_names = [f.name for f in obj._meta.fields]
    for field_name in field_names:
        if field_name not in [
            'id',
            'name',
            'image_filename',
            'image_caption',
            'category',
            'formula'
        ]:
            value = getattr(obj, field_name, None)
            if value != None:
                yield (field_name, value)
