import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(to_email, images):
    from_email = "no-reply@dungeonmasterpiece.com"
    from_password = "igmdwswlucsbvah"  # Replace this with your app-specific password
    subject = "Your Game Jam Assignment"
    body = f"Your inspiration challenge prompts are:\n\n"
    for image in images:
        body += f"Title: {image['title']}\nURL: {image['url']}\n\n"
    body += "Good luck on the game jam!"

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, from_password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        print(f"Email successfully sent to {to_email}")
    except smtplib.SMTPException as e:
        print(f"SMTP error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
