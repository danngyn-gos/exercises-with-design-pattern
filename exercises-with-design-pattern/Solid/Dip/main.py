from abc import ABC, abstractmethod


class Notifier(ABC):
    @abstractmethod
    def send(self, message: str) -> None:
        pass


class EmailService(Notifier):
    def send(self, message: str) -> None:
        print(f"[EmailService] Sending email with message: {message}")


class SmsService(Notifier):
    def send(self, message: str) -> None:
        print(f"[SmsService] Sending sms with message: {message}")


class SendNotification:

    def __init__(self, notifier: Notifier):
        self._notifier = notifier  

    def send_notification(self, message: str) -> None:
        self._notifier.send(message=message)


if __name__ == "__main__":
    email_service = EmailService()
    sms_service = SmsService()
    notification_system = SendNotification(notifier=sms_service)
    notification_system.send_notification("System update available.")