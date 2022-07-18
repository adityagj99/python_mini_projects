# Auto send email using smtblib
import smtplib                                                          # SMTP library to use SMTP

def auto_email():
    recipient_name = input("Enter recipient name : ")                   # recipient user name
    recipient_email = input("Enter recipient email address: ")          # recipient email address

    sender_email = input("Enter sender's email: ")                      # Sender's email address
    sender_passwd = input("Enter sendr's password: ")                   # Sender"s password

    message = (f'''
    Hi {recipient_name},

    This is autogenerated email sent using python.

    Regards ''')
    
    s = smtplib.SMTP('smtp.gmail.com', 587)                             # SMTP client server and port declaration
    s.ehlo()                                                            # SMTP connection start
    s.starttls()                                                        # TLS(Transport Layer Security) established
    s.login(sender_email, sender_passwd)                                # Authentication
    s.sendmail(sender_email, recipient_email, message)                  # Email sending process
    print("Email sent")                                                 # Acknowledgement

auto_email()
