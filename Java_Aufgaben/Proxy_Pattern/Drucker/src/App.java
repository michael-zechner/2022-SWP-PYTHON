public class App {
    public static void main(String[] args) {
        Printer swPrinter = new SWPrinter();
        Printer colorPrinter = new ColorPrinter();

        PrinterProxy printerProxy = new PrinterProxy(swPrinter);

        printerProxy.switchTo(colorPrinter);
        printerProxy.print("This document is in color!");
    }
}

