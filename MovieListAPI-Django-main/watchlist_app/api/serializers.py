from rest_framework import serializers
from watchlist_app.models import Watchlist , StreamPlatform , Review

# class Movieserializer(serializers.Serializer):
    
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
    
#     def create(self, validated_data):
#         # return super(Movieserializer, self).create(validated_data)
#         return Movie.objects.create(**validated_data)
    
#     def update(self,instance , validated_data):
        
#         instance.name = validated_data.get('name',instance.name)
#         instance.description = validated_data.get('description',instance.description)
#         instance.active = validated_data.get('active',instance.active)
#         instance.save()
#         return instance

class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only = True)
    
    class Meta:
        model = Review
        # fields = "__all__"
        exclude = ('watchlist',)


########################################################### watcjhlist serializer########################################################
class WatchlistSerializer(serializers.ModelSerializer):
    
    reviews = ReviewSerializer(many=True,read_only=True) #to show relationships with the help of related_name="reviews"
    
    
    class Meta:
        model = Watchlist
        fields = "__all__"

class StreamPlateformSerializer(serializers.ModelSerializer):
    
    watchlist = WatchlistSerializer(many=True,read_only=True) #to show relationships with the help of related_name="watchlist"
    
    class Meta:
        model = StreamPlatform
        fields = "__all__"

        
        
