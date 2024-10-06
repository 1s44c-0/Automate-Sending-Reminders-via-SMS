from twilio.rest import Client

def send_sms(to_number, message):
    # Twilio credentials
    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    from_number = 'your_twilio_number'

    client = Client(account_sid, auth_token)

    try:
        message = client.messages.create(
            body=message,
            from_=from_number,
            to=to_number
        )
        print(f"Message sent to {to_number}: SID {message.sid}")
    except Exception as e:
        print(f"Failed to send message: {e}")

if __name__ == "__main__":
    to_number = "+1234567890"
    message = "This is a reminder for your appointment tomorrow at 10 AM."
    send_sms(to_number, message)
  
