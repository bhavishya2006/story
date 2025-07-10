from twilio.rest import Client
import env

class NotificationManager:

    def __init__(self):
        self.client = Client(env.TWILIO_SID, env.TWILIO_AUTH_TOKEN)

    def send_sms(self, message_body):
        message = self.client.messages.create(
            from_=env.TWILIO_VIRTUAL_NUMBER,
            body=message_body,
            to=env.TWILIO_VERIFIED_NUMBER
        )
        print(f"SMS sent with SID: {message.sid}")

    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_=f'whatsapp:{+18884780051}',
            body=message_body,
            to=f'whatsapp:{+19453355090}'
        )
        print(f"WhatsApp sent with SID: {message.sid}")
