from simplybooksapi.models.author import Author
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def check_user(request):
    '''Checks to see if User has Associated Gamer

    Method arguments:
      request -- The full HTTP request object
    '''
    uid = request.data['uid']

    author = Author.objects.filter(uid=uid).first()

    if author is not None:
        data = {
            'id': author.id,
            'uid': author.uid,
            'bio': author.bio
        }
        return Response(data)
    else:
        data = { 'valid': False }
        return Response(data)


@api_view(['POST'])
def register_user(request):
    '''Handles the creation of a new gamer for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    author = author.objects.create(
        bio=request.data['bio'],
        uid=request.data['uid']
    )

    data = {
        'id': author.id,
        'uid': author.uid,
        'bio': author.bio
    }
    return Response(data)
