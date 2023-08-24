from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
# mime stand for "multipurpose internet mail extension"
# MIMEMultipart is a class of multipart module, which is submodule of mime and mime is submodule of email

# create an object of MIMEMultipart
message = MIMEMultipart()
message["from"] = "junaid Tariq"
message["to"] = "sweetjohn2111@gmail.com"
message["subject"] = "Mail from python"
message.attach(MIMEText("Body"))

# smtplib module has a class name SMTP
# smtp = smtplib.SM(host="smtp.gmail.com", port=587)
# smtp.close() #release this resource , the better is use with i.e.,

with smtplib.SM(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smpt.login("sweetjohn2111@gmail.com ")
