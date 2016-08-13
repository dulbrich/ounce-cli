"""
ounce

Usage:
  ounce me [<phone> | <name> | <list-name> | <list-name> <name>] [-i | --imessage]
  ounce install
  ounce add [<list-name>] (<name> <phone>)
  ounce contacts [<list-name>]
  ounce remove [<name> | <list-name> <name>]
  ounce -h | --help
  ounce --version

Options:
  -h --help                         Show this screen.
  --version                         Show version.
  -i --imessage                     Send via imessage on mac

Examples:
  ounce me
  ounce me -i
  ounce add dave 888-777-6666
  ounce add spending dave 888-777-6666
  ounce me -i spending

Help:




  "An ounce of prevention is worth a pound of cure." -proverb




  COMPATIBILITIES:

  macOS
  Linux
  Anything that can run python and 'curl'




  LIMITATIONS:

  If you are not using the -i on a mac then unfortunately you are limited to only 75 text messages for a single day.
  This is because once makes use of the textbelt.com open source API for outgoing tests. If you are sending via imessage
  then you have unlimited making this an ideal tool for the mac at this time.




  HOW TO SEND TO DEFAULT CONTACTS LIST:

  ounce me

  Example:

      $ ounce me -i
      $ How bad? 5
      $ How tempted? 8
      $ How worried? 4
      $ Protocol Kept? 9
      $ Subject letter? p
      > "5:8:4:9:p" was sent via imessage to:
      > Mom
      > Dad
      > Bishop




  HOW TO ADD A CONTACT TO DEFAULT CONTACTS LIST:

  ounce add <name> <phone>

  Example:

      $ ounce add dave 888-777-6666
      > Added dave to default contact list




  HOW TO ADD A CONTACT TO SPECIFIC LIST:

  ounce add <list-name> <name> <phone>

  Example:

      $ ounce add spending dave 888-777-6666
      > Added date to your spending list




  HOW TO SEND TO CONTACT LIST:

  ounce me <list-name>

  Example:

      $ ounce me -i spending
      $ How bad? 5
      $ How tempted? 8
      $ How worried? 4
      $ Protocol Kept? 9
      $ Subject letter? p
      > "5:8:4:9:p" was sent via imessage to:
      > dave




  ABOUT:

  This tool was primarily intended to help those struggling with a pornography addiction. However, it can also be used
  to help anybody with any addiction. The idea behind ounce is that you get a sponsor or a trusted friend who will
  receive your ounce messages via text messages. These messages are discrete and do not call a lot of attention to
  themselves. Each message consists of several numbers that report an incident in which you found yourself face to face
  with a temptation for relapse into destructive habits.

  For example: Say you struggle with abstaining from viewing pornography. You have discussed this with your spouse and
  have agreed that any time you see something provocative you will report that you saw something immediately. The nice
  thing about ounce is that you don't have to describe what you saw with words, but instead you describe 4 things on a
  scale from 1 - 10:

  1) How bad
  2) How Tempted
  3) How Worried
  4) Protocol Kept

  HOW BAD. How bad was it? In the pornography example this would describe how illicit the material you saw was on a
  scale of 1 - 10.

  HOW TEMPTED. How tempted were you? In the pornography example this would describe how tempted you were on a scale of
  1 - 10 to keep looking at it or to start looking at more provocative material.

  HOW WORRIED. How worried are you? In the pornography example this would describe how worried you are on a scale of
  1 - 10 that this will illicit a relapse to destructive habits or actions.

  PROTOCOL KEPT: This describes how good you were on a scale of 1 - 10 responding with a predetermined action. In the
  pornography example this could be how fast you turned off your computer screen and sent the message or how fast you
  stopped viewing the provocative whatever-it-is and sent the message to report it.

  The last thing that ounce will report is the subject. This is usually predetermined by a letter. For example if you
  and your sponser were working on your pornography addiction, you might choose the letter "p".

  Example message:

  5:8:4:9:p

  5 means that the provocative material seen was moderately bad.

  8 means that you were badly tempted to keep looking at the provocative material.

  4 means that you are not very worried about relapsing

  9 means you almost immediately turned away from the material and stopped viewing it.

  p means that the subject matter was pornography.

  The wonderful thing about Ounce is that you can work on fostering all sorts of good habits. Have a hard time not
  overspending on clothing? Use the letter "c" for "clothes." Have a hard time with overeating? Use the letter "f" for
  "food." The other nice thing is that it can be kept confidential between you and your sponsor. Others who view the
  message won't necessarily know what you are talking about, and will see a simple messsage with only numbers and one
  letter. Once is a wonderful way to open a channel of communication of help.

  A note on trust. Obviously ounce is a system built on the honor system. One who uses it infrequently will not reap its
  benefits. For instance if you are working on a pornography addiction with your spouse, you may have damaged your
  trust with your spouse in the first place by being viewing pornography at all in the first place. They may feel hurt
  and you may feel remorse and want to earn that trust back. Ounce is a wonderful tool for doing that. If every time
  you see something bad you report it to your spouse, not only do they see that you are making the effort, but they
  immediately know when you are struggling and can start a conversation with you to help you when you need it. Sometimes
  all it takes is a simple phone call or a text message conversation to help you overcome the situation.

  For the addict this becomes extremely liberating because you suddenly don't have to face your addiction alone. You can
  rely on the strength of others and the more you use it the more honest you are being with yourself and others. For the
  person who may have been hurt by you in the past by your addiction Ounce is liberating too. With time you will no
  longer have to wonder if they are being honest with you. You can see they are honestly trying and seeking the help
  they need.

"""


from inspect import getmembers, isclass

from docopt import docopt

from . import __version__ as VERSION


def main():
    """Main CLI entrypoint."""
    import commands
    options = docopt(__doc__, version=VERSION)

    # Here we'll try to dynamically match the command the user is trying to run
    # with a pre-defined command class we've already created.
    for k, v in options.iteritems():
        if hasattr(commands, k) and v:
            module = getattr(commands, k)
            commands = getmembers(module, isclass)
            command = [command[1] for command in commands if command[0] != 'Base'][0]
            command = command(options)
            command.run()
