import logging

from digiformatter import logger as digilogger


def test_digiformathandler():
    logger = logging.getLogger("sizebot")
    dfhandler = digilogger.DigiFormatterHandler()
    logger.handlers = []
    logger.propogate = False
    logger.addHandler(dfhandler)
    logger.warning("AAAAA")
