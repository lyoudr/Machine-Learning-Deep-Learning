import json
import logging
from pythonjsonlogger import jsonlogger


class CustomJsonFormatter(jsonlogger.JsonFormatter):
    """Formats log lines in JSON."""
    def process_log_record(self, log_record):
        """Modifies fields in the log_record to match Cloud Logging's expectations."""
        log_record["severity"] = log_record["levelname"]
        log_record["timestampSeconds"] = int(log_record['created'])
        log_record["timestampNanos"] = int(
            (log_record['created'] % 1) * 1000 * 1000 * 1000
        )

        return log_record

    def configure_logger():
        """Configure python logger to format logs as JSON."""
        formatter = CustomJsonFormatter(
            '%(name)s|%(levelname)s|%(message)s|%(created)f'
            '|%(lineno)d|%(pathname)s', '%Y-%m-%dT%H:%M:%S'
        )
        root_logger = logging.getLogger()
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        root_logger.addHandler(handler)
        root_logger.setLevel(logging.WARNING)
    
    logging.warning("This is a warning log")