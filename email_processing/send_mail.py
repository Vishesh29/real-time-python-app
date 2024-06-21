import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

def send_email(sender_email, sender_password, recipient_email, subject, plain_text_content=None, html_content=None):
    """
    Sends an email with optional plain text and HTML content.

    Parameters:
    sender_email (str): Sender's email address.
    sender_password (str): Sender's email account password.
    recipient_email (str): Recipient's email address.
    subject (str): Email subject.
    plain_text_content (str, optional): Plain text content of the email.
    html_content (str, optional): HTML content of the email.

    Raises:
    SMTPAuthenticationError: If authentication fails with the provided credentials.
    """

    try:
        email = EmailMessage()
        email['from'] = sender_email
        email['to'] = recipient_email
        email['subject'] = subject

        if plain_text_content:
            email.set_content(plain_text_content)

        if html_content:
            email.set_content(html_content, subtype='html')

        with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
            smtp.ehlo()  # Hello message
            smtp.starttls()  # Encryption
            smtp.login(sender_email, sender_password)
            smtp.send_message(email)
            print('Email sent successfully!')

    except smtplib.SMTPAuthenticationError as e:
        print(f"SMTP Authentication Error: {e}")
    except Exception as e:
        print(f"An error occurred while sending email: {e}")

if __name__ == "__main__":
    # Example usage:
    sender_email = 'xyz@gmail.com'
    sender_password = 'hellooldfriend'
    recipient_email = 'abc@gmail.com'
    subject = 'This is your time!!!'

    # Plain text email content
    plain_text_content = 'I am a Python developer.'

    # Dynamic HTML email content using Template
    html_content = Template(Path('index.html').read_text()).substitute(name='Tyson')

    # Send email with plain text content
    send_email(sender_email, sender_password, recipient_email, subject, plain_text_content=plain_text_content)

    # Send email with HTML content
    send_email(sender_email, sender_password, recipient_email, subject, html_content=html_content)
