import smtplib as s

ob = s.SMTP('smtp.gmail.com', 587)
ob.ehlo()
ob.starttls()
ob.login('keshavhlkesh@gmail.com','hchz zgxn qiaq gibk')
subject = "test pyhton"
body = "I Love Python"
message = "subject:{}\n\n{}".format(subject,body)
listadd = ["Shivalinge038@gmail.com", "keshavhlkesh870@gmail.com"]
ob.sendmail('keshavhlkesh@gmail.com',listadd,message)
print("send mail")
ob.quit()