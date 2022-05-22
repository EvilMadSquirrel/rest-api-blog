from celery import shared_task


@shared_task(name="send_news")
def send_news():
    print("Task")
