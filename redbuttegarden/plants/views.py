import logging

from django.core.paginator import Paginator, InvalidPage
from django.http import JsonResponse, HttpResponseBadRequest
from rest_framework import generics, viewsets, status
from django.middleware.csrf import get_token
from django.shortcuts import render, get_object_or_404
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from wagtail.images.models import Image

from .models import Family, Genus, Species, Collection, Location, SpeciesImage
from .serializers import FamilySerializer, SpeciesSerializer, CollectionSerializer, GenusSerializer, \
    LocationSerializer

logger = logging.getLogger(__name__)


class FamilyViewSet(viewsets.ModelViewSet):
    """
    List, create, retrieve, update or delete families.
    """
    queryset = Family.objects.all()
    serializer_class = FamilySerializer


class GenusViewSet(viewsets.ModelViewSet):
    """
    List, create, retrieve, update or delete genera.
    """
    queryset = Genus.objects.all()
    serializer_class = GenusSerializer


class SpeciesViewSet(viewsets.ModelViewSet):
    serializer_class = SpeciesSerializer

    def get_queryset(self):
        """
        Overriding queryset to make it possible to query for species that need to
        have their image set.
        """
        queryset = Species.objects.all()
        genus = self.request.query_params.get('genus')
        species = self.request.query_params.get('species')
        cultivar = self.request.query_params.get('cultivar')
        vernacular_name = self.request.query_params.get('vernacular_name')

        # Attempt to filter down to a single species object if query parameters were given
        if genus is not None:
            queryset = queryset.filter(genus__name=genus,
                                       name=species,
                                       cultivar=cultivar,
                                       vernacular_name=vernacular_name)

            if not queryset:
                logger.info(f'Species matching query does not exist.\nGenus name: {genus}\n'
                            f'Species name: {species}\nCultivar: {cultivar}\nVernacular name: {vernacular_name}')
                return queryset
            elif queryset.count() > 1:
                logger.info(f'Multiple objects match this query.\nGenus name: {genus}\n'
                            f'Species name: {species}\nCultivar: {cultivar}\nVernacular name: {vernacular_name}')
                return queryset

        return queryset


class LocationViewSet(viewsets.ModelViewSet):
    """
    List, create, retrieve, update or delete locations.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class CollectionList(generics.ListCreateAPIView):
    """
    List 100 most recently created collections, or create new collections.
    """
    queryset = Collection.objects.all().order_by('-id')[:100]
    serializer_class = CollectionSerializer


class CollectionDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a living plant collection.
    """
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        if user.groups.filter(name='API').exists():
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'csrf_token': get_token(request),
            })
        return Response(status=status.HTTP_403_FORBIDDEN)


def set_image(request, pk):
    # Check if user has a valid API Token
    try:
        token = request.META['Authorization'].split(' ')[1]
    except KeyError:
        return JsonResponse({'status': 'failure'})
    if Token.objects.get(key=token).exists():
        species = Species.objects.get(pk=pk)
        uploaded_image = request.FILES.get('image')
        image, img_created = Image.objects.get_or_create(
            title='_'.join([species.genus.name,
                            species.name,
                            species.cultivar]),
            defaults={'file': uploaded_image}
        )
        species_image, species_img_created = SpeciesImage.objects.get_or_create(
            species=species,
            image=image,
            caption=''
        )

        return JsonResponse({'status': 'success',
                             'image_created': img_created,
                             'species_image_created': species_img_created})

    return JsonResponse({'status': 'failure'})


def plant_map_view(request):
    return render(request, 'plants/collection_map.html')


def collection_detail(request, collection_id):
    collection = get_object_or_404(Collection, pk=collection_id)
    return render(request, 'plants/collection_detail.html', {'collection': collection})


def species_detail(request, species_id):
    species = get_object_or_404(Species, pk=species_id)
    species_images = SpeciesImage.objects.filter(species=species)
    return render(request, 'plants/species_detail.html', {'species': species,
                                                          'images': species_images})

def collection_search(request):
    qs = Collection.objects.all()
    paginator = Paginator(qs, 10)
    if request.method == 'GET':
        if request.is_ajax():
            if request.GET.get('page_number'):
                # Paginate based on the page number in the GET request
                page_number = request.GET.get('page_number')
                try:
                    page_objects = paginator.page(page_number).object_list
                except InvalidPage:
                    return HttpResponseBadRequest(mimetype="json")
                # Serialize the paginated objects
                serializer = CollectionSerializer(page_objects, many=True)
                return JsonResponse(serializer.data, safe=False)
    collections = paginator.page(1).object_list
    context = {'collections': collections}
    return render(request, 'plants/collection_search.html', context)
