#!/usr/bin/python3

"""
This programs uses logging module
"""
import logging as lg

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
lg.basicConfig(filename = "E:\\python\\lumberjack.log", level = lg.DEBUG, format = LOG_FORMAT, filemode = 'w')
logger = lg.getlogger()
logger.info("Our FIRST message.")
print("\nCode developed by Masino")
