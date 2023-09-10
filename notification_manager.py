from twilio.rest import Client

TWILIO_SID = "AC580299038c278284515a830ce3997232"
TWILIO_AUTH_TOKEN = "453d9e312a74ccd75ea33c1e10792cae"
TWILIO_VIRTUAL_NUMBER = +13342125509
TWILIO_VERIFIED_NUMBER = +919027763867


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)