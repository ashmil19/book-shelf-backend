from djchoices import DjangoChoices, ChoiceItem


class StatusChoice(DjangoChoices):
    TO_READ = ChoiceItem('TR')
    CURRENTLY_READING = ChoiceItem('CR')
    FINISHED_READING = ChoiceItem('FR')