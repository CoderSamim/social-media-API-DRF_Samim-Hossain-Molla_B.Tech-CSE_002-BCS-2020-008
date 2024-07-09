
from rest_framework import serializers
from .models import User, Post, Follow, Like, Comment

class UserSerializer(serializers.ModelSerializer):

    posts_count = serializers.IntegerField(source='post_set.count', read_only=True)
    likes_count = serializers.IntegerField(source='like_set.count', read_only=True)
    comments_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    following_count = serializers.IntegerField(source='following.count', read_only=True)
    followers_count = serializers.IntegerField(source='followers.count', read_only=True)

    class Meta:
        model = User
        # fields = '__all__'
        fields = ['id', 'username', 'full_name', 'email', 'bio', 'picture', 'gender', 'posts_count', 'likes_count', 'comments_count', 'following_count', 'followers_count']

class PostSerializer(serializers.ModelSerializer):

    likes_count = serializers.IntegerField(source='like_set.count', read_only=True)
    comments_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    

    class Meta:
        model = Post
        fields = ['id', 'user', 'content', 'created_at', 'updated_on' 'likes_count', 'comments_count']
        
        

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

