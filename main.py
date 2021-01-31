from pynotifier import Notification


def desktop_notification(string_1, string_2):
    Notification(
    title=string_1,
    description=string_2,
	icon_path='mail_icon.ico',
	duration=5,
	urgency=Notification.URGENCY_CRITICAL
).send()

if __name__ == "__main__":

    #mtitle = input("Enter the Title of the Notice ")
    #mdescription = input("Enter the Description of the Notice ")
    mtitle = "This is title"
    mdescription = "This is the description od the Notification"

    desktop_notification(mtitle,mdescription)