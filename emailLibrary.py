import smtplib
from email.mime.text import MIMEText


class EmailLibrary:
    def __init__(self, movie_name):
        self.movie_name = movie_name
        self.email_user = 'user_email_here'
        self.email_password = 'email_password_here'
        self.email_send = 'ujwal.baidar@gmail.com'
        self.smtpHost = 'smtp.gmail.com'
        self.smtpPort = 587

    def send_email(self):
        server = smtplib.SMTP(self.smtpHost, self.smtpPort)
        server.starttls()
        server.login(self.email_user, self.email_password)

        msg = MIMEText('Tickets are now available for' + self.movie_name + '. Book your seat now.')
        msg['Subject'] = 'Booking open at qfx'
        msg['From'] = self.email_user
        msg['To'] = self.email_send
        server.send_message(msg)
        server.quit()
