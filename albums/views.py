from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Album
from artists.models import Artist
from albums.serializers import AlbumSerializer
from rest_framework import status
from django.http import JsonResponse


def Routes_album(request):
    routes = [
        'showalbums/'
    ]
    return JsonResponse(routes, safe=False)


@api_view(['POST'])
def showalbums(request):
    try:
        ar = request.data.get('artists')
        theartist = Artist.objects.get(artists=ar)
        rr = Album.objects.filter(
            artist_ids=theartist).select_related('artist_ids')
        rr_ser = AlbumSerializer(rr, many=True)
        return Response(rr_ser.data)
    except Artist.DoesNotExist:
        return Response({'error': 'Artist not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# def showalbums(request):
#     ar = request.data.get('artists')
#     theartist = Artist.objects.get(artists=ar)
#     rr = Album.objects.filter(
#         artist_ids=theartist).select_related('artist_ids')
#     rr_ser = AlbumSerializer(rr, many=True)
#     return Response(rr_ser.data)