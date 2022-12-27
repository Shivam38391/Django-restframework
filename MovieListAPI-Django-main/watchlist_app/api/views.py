from watchlist_app.models import Watchlist , StreamPlatform, Review
from watchlist_app.api.serializers import WatchlistSerializer , StreamPlateformSerializer , ReviewSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.exceptions import ValidationError
from watchlist_app.api.permissions import AdminReadOnly , ReviewUserOrReadOnly



class ReviewCreate(generics.CreateAPIView): #to perform list and create
    
    queryset = Review.objects.all() #default gueryset
    ############or################
    # def get_queryset(self):
    #     return Review.objects.all() #
    
    serializer_class = ReviewSerializer
    
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        movie  = Watchlist.objects.get(pk=pk)
        
        user = self.request.user
        review_query = Review.objects.filter(review_user=user, watchlist= movie)
        if review_query.exists():
            raise ValidationError('u have already review this movie')
        
        if movie.number_of_ratings == 0:
            movie.avg_rating = serializer.validated_data['rating']
            
        else:
            movie.avg_rating = (movie.avg_rating + serializer.validated_data['rating'])/2
            
        movie.number_of_ratings += 1
        movie.save()
            
        serializer.save(watchlist = movie, review_user= user)
    
    
#######################listof Reviews using concrete classes############################

class ReviewList(generics.ListAPIView): #to perform list and create
    
    # queryset = Review.objects.all() #default gueryset
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist = pk) #review list of whatchist with ok id
    
    
    
    #######################detail of Reviews using concrete classes############################

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView): #to perform list and create
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [ReviewUserOrReadOnly]




##############################DEtail reviews########################
# class ReviewDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)



#######################listof Reviews############################
# class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView): #to perform list and create
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)



######################streamlistview #####################
class StreamlistAV(APIView):
    
    def get(self, request):
        
        platform = StreamPlatform.objects.all()
        serializer = StreamPlateformSerializer(platform, many=True)
        return Response(serializer.data)
    
    
    def post(self, request):
        
        serializer = StreamPlateformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
            
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#################detail av #################

class StreamDetailAV(APIView):
    
    def get(self, request, pk):
        
        try:
            plateform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({"Error": "Movie does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StreamPlateformSerializer(plateform)
        return Response(serializer.data)
    
    
    def put(self, request, pk):
        
        plateform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlateformSerializer(plateform,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
            
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





###################watchlitview################
class WatchlistAV(APIView):
    
    def get(self, request):
        
        movie = Watchlist.objects.all()
        serializer = WatchlistSerializer(movie, many=True)
        return Response(serializer.data)
    
    
    def post(self, request):
        
        serializer = WatchlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
            
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
#################detail av #################
class WatchDetailAV(APIView):
    
    def get(self, request, pk):
        
        try:
            movies = Watchlist.objects.get(pk=pk)
        except Watchlist.DoesNotExist:
            return Response({"Error": "Movie does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = WatchlistSerializer(movies)
        return Response(serializer.data)
    
    
    def put(self, request, pk):
        
        movies = Watchlist.objects.get(pk=pk)
        serializer = WatchlistSerializer(movies,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
            
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        

# @api_view(['GET', 'POST'])
# def movie_list(request):
    
#     if request.method == 'GET' :
            
#         movie = Movie.objects.all()
#         serializer = Movieserializer(movie, many=True)
#         return Response(serializer.data)
    
#     if request.method == 'POST' :
        
#         serializer = Movieserializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
            
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


# @api_view(["GET", "PUT", "DELETE"])
# def movie_details(request, pk):
    
    
#     if request.method =='GET':  
#         try:
#             movies = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({"Error": "Movie does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
#         serializer = Movieserializer(movies)
#         return Response(serializer.data)
    
#     if request.method =="PUT":
#         movies = Movie.objects.get(pk=pk)
#         serializer = Movieserializer(movies,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
            
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        
#     if request.method == "DELETE":
#         movies = Movie.objects.get(pk=pk)
#         movies.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)