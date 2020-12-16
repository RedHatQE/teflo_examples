import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertThat;
import static org.hamcrest.CoreMatchers.*;
import org.junit.Test;

public class SampleTest {

    @Test
    public void testMessage() {
        Sample sample = new Sample();
        String message = sample.message();
        assertEquals("Hello World!", message);
    }

    @Test
    public void testMessageNotEqual() {
        Sample sample = new Sample();
        String message = sample.message();
        assertThat("Hello World.", not(equalTo(message)));
    }
}
