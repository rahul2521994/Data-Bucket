##Send an html email using SMTP service

from pyathenajdbc import connect
from pyathenajdbc.util import as_pandas
import pandas as pd
from tabulate import tabulate
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import os
from datetime import datetime,timedelta




SMTP_host = 'email-smtp.us-west-2.amazonaws.com'
SMTP_port = '587'
SMTP_username = 'xxxxxxxxxxxxxxxxxxxx'
SMTP_password = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
sender = 'raj.k.stats@gmail.com'
from_email = 'raj.k.stats@gmail.com'


emailBody = """
<html><body><p>Revenue Numbers</p>
{RequestsDaily}
<p>Request Block numbers:</p>
{RequestSummary}
</body></html>
"""

html = emailBody.format(RequestsDaily = RequestsDaily.to_html(),
                        RequestSummary = RequestSummary.to_html(index=False))

message = MIMEMultipart(
    "alternative", None, [MIMEText(html,'html')])

message['Subject'] = 'XXXX Report'+' '+str(year)+'-'+str(month)+'-'+str(day)
message['From'] = from_email
message['To'] = 'raj.k.stats@gamil.com'
server = smtplib.SMTP(SMTP_host)
server.ehlo()
server.starttls()
server.login(SMTP_username, SMTP_password)
server.sendmail(from_email, 'raj.k.stats@gmail.com', message.as_string())
server.quit()



