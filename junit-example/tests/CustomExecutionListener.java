import org.junit.runner.Description;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;
import org.junit.runner.notification.RunListener;


public class CustomExecutionListener extends RunListener {

    static long start_time;
    static long end_time;
    static double difference;

    public void testRunStarted(Description description) throws Exception {
        System.out.println("Number of tests to execute: " + description.testCount());
        System.out.println();
    }

    public void testRunFinished(Result result) throws Exception {
        System.out.println("Number of tests executed: " + result.getRunCount());
        System.out.println("Time: " + result.getRunTime());
    }

    public void testStarted(Description description) throws Exception {
        start_time = System.nanoTime();
        System.out.println("   Starting: " + description.getMethodName());
    }

    public void testFinished(Description description) throws Exception {
        end_time = System.nanoTime();
        difference = (end_time - start_time) / 1000000;
        System.out.println("   Finished: " + description.getMethodName());
        System.out.println("   Time    : " + difference);
        System.out.println();
        System.setOut(UnitTestRunner.tmpSysOut);
        String tc = description.getTestClass().getName();
        System.out.println("     <testcase classname=\"" + tc + "\" name=\"" + description.getMethodName() + "\" time=\"" + difference + "\"/>");
        System.setOut(UnitTestRunner.lgst);
    }

    public void testFailure(Failure failure) throws Exception {
        System.out.println("   Failed: " + failure.getDescription().getMethodName());
    }

    public void testAssumptionFailure(Failure failure) {
        System.out.println("   Failed: " + failure.getDescription().getMethodName());
    }

    public void testIgnored(Description description) throws Exception {
        System.out.println("   Ignored: " + description.getMethodName());
    }
}


