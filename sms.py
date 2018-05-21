from twilio.rest import Client
import passwords
# Your Account Sid and Auth Token from twilio.com/console
account_sid = passwords.t_sid
auth_token = passwords.t_auth
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='This is the ship that made the Kessel Run in fourteen parsecs?',
         from_='+15859991090',
         to='+919087842840'
     )
print(message.sid)
