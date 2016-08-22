"""The me command."""


from .base import Base


class Me(Base):
    """ounce me"""

    use_imessage = False
    value_error = "Please enter a number from 1 - 10. "
    char_value_error = "Please enter a single letter from a - z."
    bad_scale = "( 1 being not bad at all - 10 being extremely bad )"
    tempted_scale = "( 1 being not tempted at all - 10 being extremely tempted )"
    worried_scale = "( 1 being not worried at all - 10 being extremely worried )"
    protocol_scale = "( 1 being you did not follow protocol at all - 10 you followed protocol perfectly )"

    def run(self):
        if self.options['--imessage']:
            self.use_imessage = True
        report = self.ask_questions()
        print report
        # TODO: Have the program send the text message to trusted friend.

    def ask_questions(self):
        how_bad = str(self.ask("How bad?", self.bad_scale))
        how_tempted = str(self.ask("How tempted?", self.tempted_scale))
        how_worried = str(self.ask("How worried?", self.worried_scale))
        protocol_kept = str(self.ask("Protocol kept?", self.protocol_scale))
        subject_letter = self.ask_subject()
        return how_bad + ":" + how_tempted + ":" + how_worried + ":" + protocol_kept + ":" + subject_letter

    def ask(self, question, scale):
        while True:
            s = raw_input(question + " ")
            try:
                val = int(s)
                if val > 0 and val < 11:
                    break
                else:
                    raise ValueError
            except ValueError:
                print self.value_error + scale
        return val

    def ask_subject(self):
        while True:
            subject = raw_input("Subject letter? ")
            try:
                ascii_val = ord(subject)
                if ascii_val > 96 and ascii_val < 123:
                    break
                elif ascii_val > 64 and ascii_val < 90:
                    break
                else:
                    raise ValueError
            except ValueError:
                print "Please enter a single letter from a - z."

        return subject

