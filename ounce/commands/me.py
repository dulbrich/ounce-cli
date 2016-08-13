"""The me command."""


from .base import Base


class Me(Base):
    """Say hello, world!"""

    def run(self):
        print 'Hello, world!'
