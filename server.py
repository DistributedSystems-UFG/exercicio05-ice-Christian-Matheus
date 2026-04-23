import sys, Ice
import Demo

class PrinterI(Demo.Printer):
    def printString(self, s, current=None):
        print(s)

    def printUpperCase(self, s, current=None):
        print(s.upper())

class LoggerI(Demo.Logger):
    def log(self, s, current=None):
        print('[LOG] ' + s)

    def logError(self, s, current=None):
        print('[ERROR] ' + s)

communicator = Ice.initialize(sys.argv)

adapter = communicator.createObjectAdapterWithEndpoints("SimpleAdapter", "default -p 11000")
adapter.add(PrinterI(), communicator.stringToIdentity("SimplePrinter"))
adapter.add(LoggerI(), communicator.stringToIdentity("SimpleLogger"))
adapter.activate()

communicator.waitForShutdown()