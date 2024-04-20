from data import details
from winotify import Notification, audio


def show_notif():

    # loop through the dummy data
    for detail in details:
        notif = Notification(
            app_id= "Desk-Notif",
            title= detail["title"],
            msg= detail["content"],
            duration= "short",
            icon= r"C:\Users\Gideon\Downloads\facet3.jpg"
        )

        # set an audio for the notification
        notif.set_audio(audio.Reminder, loop=False)

        # a call-to-action which come with the notif. Do forget to follow me on github
        notif.add_actions(label="Check Repo", launch="https://www.github.com/giiiiid")

        # display the notif
        notif.show()

if __name__ == "__main__":
    show_notif()