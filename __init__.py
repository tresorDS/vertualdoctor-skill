from mycroft import MycroftSkill, intent_file_handler


class Vertualdoctor(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('vertualdoctor.intent')
    def handle_vertualdoctor(self, message):
        self.speak_dialog('vertualdoctor')


def create_skill():
    return Vertualdoctor()

