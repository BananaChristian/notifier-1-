from plyer import notification
import time

notification_message='Hello world'
notification_title='Banana here'

notification.notify(
    title=notification_title,
    message=notification_message,
    app_icon='bellIcon.ico',
    timeout=10
)

time.sleep(60*60*12)