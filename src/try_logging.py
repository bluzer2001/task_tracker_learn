import logging

logging.basicConfig(level=logging.DEBUG)


logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")


logging.debug(
    "Serialized notification: %s",
    data,
)

logging.info(
    "Task assigned to user"
)

logging.warning(
    "Blocked user attempted task assignment"
)

logging.error(
    "Failed to publish notification"
)

logging.critical(
    "Database unavailable"
)
