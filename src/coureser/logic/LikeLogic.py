from coureser.models.Film import Film
from coureser.models.Like import Like


class LikeLogic():
    @staticmethod
    def set_like(data, pk, user):
        Like.objects.like(data['value'], pk, user)
        Film.objects.count_rating(pk)

    @staticmethod
    def get_like_data(pk, user):
        if not user.is_authenticated:
            return {}

        like = Like.objects.filter(film_id=pk, author=user.profile).first()

        if like:
            like_data = {'value': like.value}
        else:
            like_data = {}

        return like_data
