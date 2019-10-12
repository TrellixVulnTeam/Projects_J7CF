import smtplib
from datacollector import db
from flask import render_template, flash
from sqlalchemy.sql import func
from datacollector.model import UserData
from email.mime.text import MIMEText


def send_email(email, height, average, count):
    from_email = "python2143@gmail.com"
    from_passwd = "datacollector321"
    to_email = email

    subject = "Height data"
    message = "Hey there, your height is <strong> {} </strong> <br>" \
              "The average height is <strong> {} </strong> cm, counted from <strong> {} </strong> users".format(height, average, count)

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    wp = smtplib.SMTP('smtp.gmail.com', 587)
    wp.ehlo()
    wp.starttls()
    wp.login(from_email, from_passwd)
    wp.send_message(msg)


class Backend(object):

    def __init__(self, form):
        self.form = form
        self.user_data = UserData

    def add_entry(self):
        email = self.form.email_addr.data
        height = self.form.height.data
        average_height = 0
        count = self.user_data.query.count()

        if count != 0:
            average_height = round(db.session.query(func.avg(self.user_data.height)).scalar(), 2)

        data = UserData(email=email, height=height)

        try:
            db.session.add(data)
            db.session.commit()
            send_email(email, height, average_height, count)
            return render_template("success.html")
        except Exception:
            flash("This email is not available!", "danger")
            return render_template("home.html", form=self.form)
