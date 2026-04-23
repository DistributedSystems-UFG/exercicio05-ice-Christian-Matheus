import sys, Ice
import Demo

communicator = Ice.initialize(sys.argv)

base = communicator.stringToProxy("SimplePrinter:default -p 11000")
printer = Demo.PrinterPrx.checkedCast(base)
if not printer:
    raise RuntimeError("Invalid proxy")

printer.printString("Hello World!")
printer.printUpperCase("Hello World!")

base2 = communicator.stringToProxy("SimpleLogger:default -p 11000")
logger = Demo.LoggerPrx.checkedCast(base2)
if not logger:
    raise RuntimeError("Invalid proxy")

logger.log("Client connected successfully")
logger.logError("This is a test error message")

communicator.destroy()