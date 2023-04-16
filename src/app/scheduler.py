"""Check standing debt items at recurent intervals."""
import os
import time
from apscheduler.schedulers.background import BackgroundScheduler
from app.state import db


def check_standing_items():
    """Check unpaid items."""
    standing_items = []
    for item in db["debt_items"]:
        if not item.paid:
            standing_items.append(item)
    return standing_items


def generate_invoice(item):
    """Generate invoice. Mock outside lib functionality."""
    print(f"{item.name}, id: {item.governmentId} " +
          f"owes {item.debtAmount} due {item.debtDueDate}")


def send_email(item):
    """Mock email service."""
    print(f"To: {item.email}. See attached invoice.")


def job():
    """Configure recurring job."""
    standing_items = check_standing_items()
    for item in standing_items:
        generate_invoice(item)
        send_email(item)


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(job, 'interval', hours=6)
    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        # This is here to simulate application activity
        # (which keeps the main thread alive).
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled
        # but should be done if possible
        scheduler.shutdown()
