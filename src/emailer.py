"""
    Functionality for broadcast email messages to a list of subscribers
"""
import os
import smtplib, ssl
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

HOST_ADDRESS_KEY = "HOST_ADDR"
HOST_PASSWORD_KEY = "HOST_PWD"
RETRY_TIME = 3  # how many times to resend if fail


class Emailer:

    def __init__(self, server: str = "smtp.gmail.com", port: int = 465):
        # fetch hosting email address and password from env for safety
        self.host_addr = os.getenv(HOST_ADDRESS_KEY)
        self.host_pwd = os.getenv(HOST_PASSWORD_KEY)
        assert (self.host_addr is not None) and (self.host_pwd is not None), f"Please set the environment variable {HOST_ADDRESS_KEY} and {HOST_PASSWORD_KEY}"
        self.subscribers = set()  # in emails
        self.server = server  # SMTP server
        self.port = port  # for SSL
        self.context = ssl.create_default_context()
        self.retry = RETRY_TIME

    def add_subscriber(self, new_email: str) -> None:
        self.subscribers.add(new_email)

    """
    Broadcast emails to all subscribers for up to retry times
    return True if all emails are sent out successfully
    or False if at least one email fails for retry times
    """
    def broadcast_email(self, email: str) -> bool:
        with smtplib.SMTP_SSL(self.server, self.port, context=self.context) as server:
            server.login(self.host_addr, self.host_pwd)
            to_send = list(self.subscribers)
            for _ in range(self.retry):
                failures = server.sendmail(self.host_addr, to_send, email)
                if (not failures):
                    return True
                # log the fail reason
                for email, tuple in failures.items():
                    logging.error(
                        f"Failure to send email to {email} for SMTP error code {tuple[0]} and reason {tuple[1]}")
                to_send = list(failures.keys())
            return False