from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        verbose_name='Название',
        max_length=200,
        help_text='Название группы'
    )
    description = models.TextField(
        verbose_name='Описание'
    )

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(
        "Дата публикации", auto_now_add=True
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts"
    )
    group = models.ForeignKey(
        Group,
        verbose_name='Группа',
        blank=True,
        on_delete=models.SET_NULL,
        null=True, related_name='posts',
    )

    def __str__(self):
        return self.text[:15]


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    text = models.TextField()
    created = models.DateTimeField(
        "Дата добавления", auto_now_add=True, db_index=True
    )


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        null=False,
        related_name='follower'
    )
    following = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.SET_NULL,
        null=True,
        related_name='following',
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "following"],
                                    name="followed_author")
        ]
