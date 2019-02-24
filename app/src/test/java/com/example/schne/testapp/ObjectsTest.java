package com.example.schne.testapp;

import org.junit.Before;
import org.junit.Test;

import static junit.framework.TestCase.assertTrue;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;

public class ObjectsTest {

    private User creator;
    private Post userPost;

    @Before
    public void setUpUser() {
        creator = new User("user", "testemail@illinois.edu");
        userPost = creator.createPost();
    }

    @Test
    public void adjustUserPointsFromPostTest() {
        assertEquals(0, creator.getCredibility());
        assertEquals(0, userPost.getCredibility());
        userPost.upCredibilityByOne();
        assertEquals(1, userPost.getCredibility());
        assertEquals(1, creator.getPosts().get(0).getCredibility());
        assertEquals(1, userPost.getAuthor().getCredibility());
        assertEquals(1, creator.getCredibility());
        userPost.lowerCredibilityByOne();
        assertEquals(0, userPost.getCredibility());
        assertEquals(0, creator.getPosts().get(0).getCredibility());
        assertEquals(0, userPost.getAuthor().getCredibility());
        assertEquals(0, creator.getCredibility());
    }

    @Test
    public void equalPlayersTest() {
        User secondUser = new User("user2", "testemail2@illinois.edu");
        User thirdUser = new User("user", "testemail3@illinois.edu");
        assertFalse(creator.equals(secondUser));
        assertFalse(creator.equals(thirdUser));
        assertTrue(creator.equals(creator));
    }


}
