from rest_framework import viewsets
from .models import YourModel
from .serializers import YourModelSerializer
from .pagination import YourCustomPagination
from rest_framework import parsers,status

class YourModelViewSet(viewsets.ModelViewSet):
    queryset = YourModel.objects.all()
    serializer_class = YourModelSerializer
    pagination_class = YourCustomPagination  # Add your custom pagination class here if needed
    parser_classes = [parsers.FormParser,parsers.MultiPartParser]

