public class A4 implements Envelope {

    private double weight;

    public A4(double weight) {
        this.weight = weight;
    }

    @Override
    public double getWeight() {
        return weight;
    }
    @Override
    public String getSize() {
        return "A4";
    }
}
