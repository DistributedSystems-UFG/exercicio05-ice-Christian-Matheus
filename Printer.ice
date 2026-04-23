module Demo
{
    interface Printer
    {
        void printString(string s);
        void printUpperCase(string s);
    }

    interface Logger
    {
        void log(string s);
        void logError(string s);
    }
}
