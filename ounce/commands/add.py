"""The add command."""


import os
from .base import Base


class Hello(Base):
    """Add contact to ounce"""

    def run(self):
        add_contact_command = ""
        os.system(add_contact_command)
