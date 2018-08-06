import logging
logging.basicConfig(level=logging.DEBUG,
	format="%(asctime)s-->%(levelname)s-->%(message)s",
	filename="log.txt")
logging.info("INFO message")
logging.error("ERROR message")
logging.warn("WARNING message")
logging.debug("DEBUG message")