from ..badge import AbstractBadge


class FirstManualBadge(AbstractBadge):

    title = "Interest club"
    meta = "First manual!"
    display = False

    def is_completed(self, user):
        if user.badges_firstmanualbadge.count() > 0:
            return True
        return False

