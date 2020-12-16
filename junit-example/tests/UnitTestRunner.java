import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;
import org.junit.Test;
import junit.framework.TestSuite;
import junit.framework.TestResult;
import junit.framework.TestFailure;
import java.util.Enumeration;
import java.util.logging.Logger;
import java.util.logging.Level;
import java.nio.file.Files;
import java.io.OutputStream;
import java.io.IOException;
import java.io.PrintStream;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;

public class UnitTestRunner {
    static JUnitCore junitCore;
    static Class<?> testClasses;

    public static PrintStream lgst;
    public static PrintStream oldPrintStream;
    public static PrintStream newSysOut;
    public static PrintStream tmpSysOut;

    public static void main(String[] args) throws IOException, ClassNotFoundException, InstantiationException, IllegalAccessException {

        Class tc = Class.forName(args[0]);
        String name = "" + tc.getName() + ".xml";

        // Setup logger and output files
        // Log file
        String lname = args[0] + ".log";
        OutputStream logOut = Files.newOutputStream(Paths.get(lname),
              StandardOpenOption.WRITE, StandardOpenOption.CREATE);
        lgst = new PrintStream(logOut);
        System.setOut(lgst);

        // xml file
        OutputStream outFile = Files.newOutputStream(Paths.get(name),
              StandardOpenOption.WRITE, StandardOpenOption.CREATE);
        newSysOut = new PrintStream(outFile);

        // tmp file
        OutputStream tmpFile = Files.newOutputStream(Paths.get("tmp.txt"),
              StandardOpenOption.WRITE, StandardOpenOption.CREATE);
        tmpSysOut = new PrintStream(tmpFile);

        System.out.println("Running Junit Test Suite: " + args[0]);

        // run tests
        junitCore = new JUnitCore();
        junitCore.addListener(new CustomExecutionListener());
        Result result = junitCore.run(tc);

        for (Failure failure : result.getFailures()) {
            System.out.println(failure.toString());
        }

        // Save the System.out instance
        oldPrintStream = System.out;

        // xml output
        try {
            System.setOut(newSysOut);
            System.out.println("<?xml version=\"1.0\" encoding=\"UTF-8\" ?>");
            int fail_cnt = result.getFailureCount();
            int ig_cnt = result.getIgnoreCount();
            int cnt = result.getRunCount();
            long tt = result.getRunTime();
            System.out.println("<testsuite errors=\"0\" skipped=\"" + ig_cnt +
                                "\" tests=\"" + cnt + "\" time=\"" + tt + "\" failures=\"" +
                                fail_cnt + "\" name=\"" + tc.getName() + "\">");

            Files.copy(Paths.get("tmp.txt"), outFile);

            System.out.println("</testsuite>");
        } catch (Exception ex) {
            Logger.getLogger(UnitTestRunner.class.getName()).log(Level.SEVERE, null, ex);
        } finally {
            System.setOut(oldPrintStream);
        }

        System.out.println("Successful: " + result.wasSuccessful() + " ran " + result.getRunCount() + " tests");
    }
}

