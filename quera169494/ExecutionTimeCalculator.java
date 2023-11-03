import java.math.BigDecimal;
import java.math.RoundingMode;


public class ExecutionTimeCalculator {
    public static long functionToCall() {
        long returnValue = 0;
        for (long i = 1; i < 1000L * 1000 * 1000 * 10; i++) {
            returnValue += i;
        }
        return returnValue;
    }

    public static BigDecimal measureExecutionTime(Runnable function) {
        long startTime = System.nanoTime();
        function.run();
        long endTime = System.nanoTime();
        BigDecimal  duration = new BigDecimal((endTime - startTime)/1000_000_000.0).setScale(5, RoundingMode.HALF_UP);

        return duration;
    }

    public static void main(String[] args) {
        System.out.println(measureExecutionTime(ExecutionTimeCalculator::functionToCall));
    }
}
