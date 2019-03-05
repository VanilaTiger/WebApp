#Flask1!!!
#flaskemailcognibe@gmail.com

#działajacy

import smtplib, ssl

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "flaskemailcognibe@gmail.com"
password = "Flask1!!!"

# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender_email, password)
    # TODO: Send email here
    server.sendmail(sender_email, "madar89@gmail.com", "Python email")
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit()