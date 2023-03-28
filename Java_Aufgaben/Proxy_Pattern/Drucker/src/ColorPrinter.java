class ColorPrinter implements Printer {
    @Override
    public void print(String document) {
        System.out.println("Printing color document: " + document);
    }
}