package org.openlmis.mobile.refui;

import org.junit.Test;
import org.openlmis.mobile.sanity.Sanity;

import static org.junit.Assert.*;

/**
 * Example local unit test, which will execute on the development machine (host).
 *
 * @see <a href="http://d.android.com/tools/testing">Testing documentation</a>
 */
public class ExampleUnitTest {
    @Test
    public void addition_isCorrect() throws Exception {
        assertEquals(4, 2 + 2);
    }

    @Test
    public void should_be_able_to_call_core() throws Exception {
        Sanity s = new Sanity(123);
        assertNotNull(s);
    }
}