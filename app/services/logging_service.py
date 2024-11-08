import logging

class LoggingService:
    @staticmethod
    def log_event(event):
        logging.info(f"Event logged: {event}")

    @staticmethod
    def log_error(error):
        logging.error(f"Error logged: {error}")
