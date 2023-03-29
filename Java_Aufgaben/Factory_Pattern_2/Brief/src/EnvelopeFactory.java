public class EnvelopeFactory {
    public static Envelope createEnvelope(String size, double weight) {
        switch (size) {
            case "A4":
                return new A4(weight);
            case "A5":
                return new A5(weight);
            case "A6":
                return new A6(weight);
            default:
                throw new IllegalArgumentException("Unknown envelope size: " + size);
        }
    }
}
