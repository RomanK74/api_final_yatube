from rest_framework import serializers, validators

from .models import Comment, Follow, Group, Post, User


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date')
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        model = Comment
        read_only_fields = ('post',)


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('title',)
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault())
    following = serializers.SlugRelatedField(
        read_only=False,
        queryset=User.objects.all(),
        slug_field='username',)

    class Meta:
        model = Follow
        fields = ('user', 'following',)
        validators = [
            validators.UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following',)
            )
        ]

    def validate(self, attrs):
        if self.context['request'].user == attrs['following']:
            raise serializers.ValidationError(
                'Вы не можете подписаться на самого себя'
            )
        return attrs
