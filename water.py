import time
from plyer import notification
if(__name__=="__main__"):
    notification.notify(
        title = "Drink water now!!",
        message = '''Benefits of drinking water carrying nutrients and oxygen to your cells. flushing bacteria from your bladder.aiding digestion.preventing constipation.''',
        timeout = 10
    )
    time.sleep(60*60)