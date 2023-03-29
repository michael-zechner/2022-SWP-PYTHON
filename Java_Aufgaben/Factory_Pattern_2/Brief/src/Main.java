public class Main {
    public static void main(String[] args) {
        // Erstelle einen A4-Briefumschlag mit einem Gewicht von 20 Gramm
        Envelope a4Envelope = EnvelopeFactory.createEnvelope("A4", 20.0);
        System.out.println("Briefumschlagsgröße: " + a4Envelope.getSize());
        System.out.println("Briefewicht: " + a4Envelope.getWeight() + " g");
    }
}
