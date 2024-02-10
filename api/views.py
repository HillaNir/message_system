from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.utils import timezone
from django.db.models import Q
from .serializers import *
from api.models import *


class MessageAll(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            # is_authenticated = request.user == user
            
            if request.query_params.get('is_read', None) == 'True':
                messages = Message.objects.filter(receiver=user, is_read=True)
            else:
                messages = Message.objects.filter(Q(sender=user) | Q(receiver=user))

            serializer = MessageSerializer(messages, many=True)
            return Response(serializer.data)

        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)



    

class MessageOne(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    
    def post(self,request):
        data = JSONParser().parse(request)
        sender = User.objects.get(username=data['sender']['username'])
        receiver = User.objects.get(username=data['receiver']['username'])
        message = Message.objects.create(
        sender=sender,
        receiver=receiver,
        message=data['message'],
        subject=data['subject']
        )
        message.save()
        return JsonResponse({'message': 'message created successfully'}, status=status.HTTP_201_CREATED)
    def put(self,request,message_id):
        try:
            message = Message.objects.get(id=message_id)
            data = JSONParser().parse(request)
            message.is_read = True
            message.save()
            return JsonResponse({'message':'message updated successfully'})
        except:
            return JsonResponse({'message':'message not found'}, status=status.HTTP_404_NOT_FOUND) 
    def delete(self, request, message_id):
        try:
            message = Message.objects.get(id=message_id)
            message.delete()
            return JsonResponse({'message':'message deleted successfully'})
        except:
            return JsonResponse({'message':'message not found'}, status=status.HTTP_404_NOT_FOUND) 
    


# class MessageAll(APIView):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]    
#     def get_all_messages(self, request, user_id):
#         try:
#             user = User.objects.get(id=user_id)
#             if user.is_authenticated():
#                 user = request.user
#                 messages = Message.objects.filter(Q(sender=user) | Q(receiver=user))
#                 serializer = MessageSerializer(messages, many=True)
#                 return Response(serializer.data)
#             else:
#                 return Response({'error': 'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)
#         except:
#             return JsonResponse({'message':'message not found'}, status=status.HTTP_404_NOT_FOUND)
#     def get_unread_messages(self, request, user_id):
#         try:
#             user = User.objects.get(id=user_id)
#             if user.is_authenticated():
#                 user = request.user
#                 messages = Message.objects.filter(receiver=user, is_read=False)
#                 serializer = MessageSerializer(messages, many=True)
#                 return Response(serializer.data)
#             else:
#                 return Response({'error': 'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)
#         except:
#             return JsonResponse({'message':'message not found'}, status=status.HTTP_404_NOT_FOUND)
    

# לבדוק שהפונקציות נכונות

# from rest_framework import generics
# from rest_framework.permissions import IsAuthenticated
# from .models import Message
# from .serializers import MessageSerializer

# class MessageList(generics.ListCreateAPIView):
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer
#     permission_classes = (IsAuthenticated,)  # Only authenticated users can access

# class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer
#     permission_classes = (IsAuthenticated,)
