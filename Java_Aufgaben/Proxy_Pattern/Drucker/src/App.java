public class App {
    public static void main(String[] args) {
        Printer bwPrinter = new BWPrinter();
        Printer colorPrinter = new ColorPrinter();

        PrinterProxy printerProxy = new PrinterProxy(bwPrinter);
        printerProxy.print("");
        printerProxy.switchTo(colorPrinter);
        printerProxy.print("");
    }
}

