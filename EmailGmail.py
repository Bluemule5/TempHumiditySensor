import time
import math
import smtplib
import HTU21DF

def email_esi() :
    TO = 'daniel.colvett@gmail.com'
    SUBJECT = 'IT Room Temp/Humidity Alert'
    TEXT = 'Temperature in IT Room is currently'

    # Gmail Sign In
    gmail_sender = 'esiit200@gmail.com'
    gmail_passwd = 'TheOne200!'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_sender, gmail_passwd)

    BODY = '\r\n'.join(['To: %s' % TO,
                        'From: %s' % gmail_sender,
                        'Subject: %s' % SUBJECT,
                        '', TEXT])

    try:
        server.sendmail(gmail_sender, [TO], BODY)
        print ('email sent')
    except:
        print ('error sending mail')

    server.quit()

while True:
	print("sending reset...")
	HTU21DF.htu_reset
	temperature = HTU21DF.read_temperature()
	print("The temperature is %f F." % temperature)
	time.sleep(1)
	humidity = HTU21DF.read_humidity()
	print("The humidity is %F percent." % humidity)
	time.sleep(1)