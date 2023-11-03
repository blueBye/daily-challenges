import org.junit.*;

import java.util.*;

import static org.junit.Assert.*;

public class HashCollisionCheckerSampleTest {
    @Test
    public void testCountOfUniqueHashCodesEmptyHashSet() {
        assertEquals(0, HashCollisionChecker.countOfUniqueHashCodes(new HashSet<>()));
    }

    @Test
    public void testCountOfUniqueHashCodesNonEmptyHashSet() {
        HashSet<String> set = new HashSet<>();
        set.add("c#c#c#c#c#c#bBc#c#c#c#bBc#");
        set.add("c#c#c#c#c#c#bBc#c#c#c#c#aa");
        set.add("c#c#c#c#c#c#bBc#c#c#c#c#bB");
        assertEquals(1, HashCollisionChecker.countOfUniqueHashCodes(set));
    }

    @Test
    public void testCountOfUniqueHashCodesEmptyHashMap() {
        assertEquals(0, HashCollisionChecker.countOfUniqueHashCodes(new HashMap<>()));
    }

    @Test
    public void testCountOfUniqueHashCodesNonEmptyHashMap() {
        HashMap<String, Integer> map = new HashMap<>();
        map.put("c#c#c#c#c#c#bBc#c#c#c#bBc#", 5);
        map.put("c#c#c#c#c#c#bBc#c#c#c#c#aa", 5);
        map.put("c#c#c#c#c#c#bBc#c#c#c#c#bB", 5);
        map.put("c#c#c#c#c#c#c#aaaaaaaac#c#", 5);
        map.put("c#c#c#c#c#c#c#aaaaaabBaaax", 5);
        assertEquals(2, HashCollisionChecker.countOfUniqueHashCodes(map));
    }
}