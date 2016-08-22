"""The me command."""


from .base import Base


class Me(Base):
    """ounce me"""

    def run(self):
        print 'OUNCE!'
