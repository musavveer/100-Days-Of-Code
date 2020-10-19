# Desktop notifier

# importing time to schedule notification
import time
# Plyer is a Python library for accessing features of your computer
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Time to take a break",
            message = "All the research shows that people who do not take time off are less productive than those who take.",
            timeout = 10
        )
        # sends a notification after 1 hr
        time.sleep(60*60) 