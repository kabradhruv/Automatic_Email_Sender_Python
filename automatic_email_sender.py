# importing modules
import smtplib
import json
from functions_defined import take_command, speak
from email.message import EmailMessage

# opening config.json file
with open("config.json", "r") as r1:
    parameters = json.load(r1)["parameters"]
with open("email_list.json", "r") as r2:
    contacts = json.load(r2)["contacts"]

# establishing connection with smtp and defining a function
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(parameters["email"], parameters["password"])


def send_mail(to_addr, subject, mes):
    email = EmailMessage()
    email['From'] = parameters["email"]
    email['To'] = to_addr
    email['Subject'] = subject
    email.set_content(mes)
    server.send_message(email)
    # server.sendmail(parameters['email'],to_addr,mes)


def get_email_info():
    print("Sir,To whom you want to send this mail")
    speak("Sir,To whom you want to send this mail")
    to_addr = take_command().lower()
    try:
        receiver = contacts[to_addr]
        print(f"Found your email in the contacts {receiver}")
        speak(f"Found your email in the contacts ", 200)
    except:
        if "@" in to_addr:
            print(f"Couldn't find email in your contacts so sending to {to_addr}")
            speak(f"Couldn't find email in your contacts so sending to {to_addr}", 200)
            receiver = to_addr
        else:
            speak(f"Couldn't find email in your contacts so please type manually", 200)
            receiver=input("Email::>")
    print(receiver)
    print("Sir,what is the subject of the email")
    speak("Sir,what is the subject of the email")
    subject = take_command().lower()
    print("Sir,What is the message you want to send")
    speak("Sir,What is the message you want to send")
    message = take_command().lower()
    try:
        send_mail(receiver, subject, message)
    except Exception as e:
        print(e)
    print("Sir,Do you want to send more email")
    speak("Sir,Do you want to send more email")
    yes_or_no = take_command()
    if 'yes' in yes_or_no:
        get_email_info()
    elif 'no' in yes_or_no:
        pass
    else:
        print("Invalid statement")


get_email_info()
