# Amir Abu Hani
from datetime import datetime

timestamp_log = datetime.now()
date_log = timestamp_log.strftime("%Y-%m-%d")


def factory_system_logs(include_timestamp=False, include_level=False, include_date=False, log_level=""):
    def log(msg, level=log_level):
        log_detail = ""
        if include_timestamp:
            log_detail += f"{timestamp_log}"
        if include_date:
            log_detail += f"{date_log}"
        if include_level:
            log_detail += level
        msg += log_detail
        print(msg)

    return log


just_message_log = factory_system_logs()
msg_timestamp_log = factory_system_logs(include_timestamp=True)
msg_timestamp_level_log = factory_system_logs(include_timestamp=True, include_level=True)
event_date_log = factory_system_logs(include_date=True)

just_message_log("Disk space is critically low")
msg_timestamp_log("User 'amir' is logging in at: ")
msg_timestamp_level_log("Network connection lost ", level=" ERROR")
event_date_log("Memory usage approaching maximum limit ")
