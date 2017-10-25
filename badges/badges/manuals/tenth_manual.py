from ..badge import AbstractBadge


class TenthManualBadge(AbstractBadge):
    title = "Teacher career"
    meta = "Your first anniversary!"
    display = True

    def is_completed(self, user):
        if user.badges_tenthmanualbadge.count() > 0:
            return True
        return False
