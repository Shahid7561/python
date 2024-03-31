import time
from plyer import notification

notification.notify(
    title = "Hourly Motivation",
    message = "We cannot solve problems with the kind of thinking we employed when we came up with them. — Albert Einstein",
    timeout = 5
)
time.sleep(60)