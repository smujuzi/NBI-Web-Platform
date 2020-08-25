from import_export import resources
from .models import NBI


class NBIResource(resources.ModelResource):
    class Meta:
        model = NBI
