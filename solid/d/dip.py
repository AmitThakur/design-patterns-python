# class GmailClient:
#
#     def send_email(self, data):
#         pass
#
#
# class EmailService:
#     def __init__(self):
#         self.gmail_client = GmailClient()
#
#     def send_email(self, data):
#         self.gmail_client.send_email(data)
#
#
class EmailClient:

    def send_email(self, data):
        raise NotImplementedError("Not implemented")

class EmailService:

    def __init__(self, email_client):
        self.email_client = email_client

    def send_email(self, data):
        self.email_client.send_email(data)


class GmailClient(EmailClient):

    def send_email(self, data):
        print(f'Sending email using Gmail: {data}')


class OutlookClient(EmailClient):

    def send_email(self, data):
        print(f'Sending email using Outlook: {data}')


if __name__ == '__main__':
    gmail_client = GmailClient()
    email_service = EmailService(gmail_client)
    email_service.send_email("Hello from Amit")