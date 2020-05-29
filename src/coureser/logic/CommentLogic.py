from coureser.common.paginator import paginate
from coureser.models.Comment import Comment


class CommentLogic:
    @staticmethod
    def comment(text, user, pk):
        Comment.objects.create(
            text=text,
            author=user.profile,
            film_id=pk)

    @staticmethod
    def paginate(request, pk):
        comments = Comment.objects.filter(film__id=pk)
        comments, p = paginate(comments, request)
        return comments, p.num_pages
