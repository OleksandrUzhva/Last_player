from django.db import models
from shared.django import TimestampMixin
from django.db.models import Q
from users.models import User
from users.enums import Positions



class GameManagers(models.Manager):
    def filter_by_participent(self, user: User):
        return self.model.filter(Q(junior=user) | Q(senior=user))
    
class Games(TimestampMixin):
    creat_game = models.CharField(max_length=100)
    team = models.TextField(null=True)
    team_positions = models.CharField(choices=Positions.choices())

    support = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="support_game"
    )
    mid = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="mid_game"
    )
    tank = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="tank_game"
    )

    objects = GameManagers()