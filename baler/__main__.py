from .baler import main
import logging
logger = logging.getLogger(__name__)
import datetime

timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M")
logging.basicConfig(filename="baler.log"+timestamp, level=logging.INFO)
logger.debug("Made logger")
logger.debug("Starting baler")

main()
