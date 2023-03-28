class PrinterProxy implements Printer {
    private Printer printer;

    public PrinterProxy(Printer printer) {
        this.printer = printer;
    }

    @Override
    public void print(String document) {
        printer.print(document);
    }

    public void switchTo(Printer newPrinter) {
        this.printer = newPrinter;
    }
}