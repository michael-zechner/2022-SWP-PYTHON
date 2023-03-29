public class App {
    public static void main(String[] args) {
        Printer swPrinter = new SWPrinter();
        Printer colorPrinter = new ColorPrinter();

        PrinterProxy printerProxy = new PrinterProxy(swPrinter);
        printerProxy.print("This document is in SW!");
        printerProxy.switchTo(colorPrinter);
        printerProxy.print("This document is in color!");
    }
}

