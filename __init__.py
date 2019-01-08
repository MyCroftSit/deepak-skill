from mycroft import MycroftSkill, intent_file_handler


class Deepak(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('deepak.intent')
    def handle_deepak(self, message):
        self.speak_dialog('deepak')


def create_skill():
    return Deepak()

