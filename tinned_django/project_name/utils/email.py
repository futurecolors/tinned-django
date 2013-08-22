# coding: utf-8
from django.conf import settings
from django.core.mail.backends.smtp import EmailBackend


class DebugSMTPEmailBackend(EmailBackend):
    """ Overrides SMTP backend to send all emails to 1 debug address
        instead of actual recipients
    """
    subject_template = u'[DEBUG: %(emails)s] %(subject)s'

    def _send(self, email_message):
        if getattr(settings, 'EMAIL_DEBUG', True):
            email_message.subject = self.subject_template % {
                'emails': ','.join(email_message.to),
                'subject': email_message.subject}
            email_message.to = settings.EMAIL_DEBUG_ADDRESSES

        super(DebugSMTPEmailBackend, self)._send(email_message)
