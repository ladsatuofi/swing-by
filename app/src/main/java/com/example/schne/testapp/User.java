package com.example.schne.testapp;

import java.util.ArrayList;
import java.util.List;

public class User {

    private String username;
    private String email;

    //id might be obsolete, do not use
    private int id;


    private int credibility = 0;
    private List<Post> posts = new ArrayList<>();

    public String getUsername() {
        return username;
    }

    public int getCredibility() {
        return credibility;
    }

    public List<Post> getPosts() {
        return posts;
    }

    public String getEmail() {
        return email;
    }

    /**
     * Verifies that the email contains '@illinois.edu'
     * @return true if the email is found to be valid
     */
    public boolean verifyEmail() {
        for (int i = 0; i < email.length(); i++) {
            if (email.substring(i).equals("@illinois.edu")) {
                return true;
            }
        }

        return false;
    }

    public int getId() {
        return id;
    }

    User(String newUsername, String newEmail) {
        username = newUsername;
        email = newEmail;
    }

    public void setCredibilityByPosts() {
        if (posts.size() > 0) {
            for (Post post : posts) {
                credibility += post.getCredibility();
            }
        }
    }

    /**
     * Retrieves the total credibility of the user's posts
     * @return the total value of the user's credibility by posts
     */
    public int getCredibilityByPosts() {
        int postsCredibility = 0;
        if (posts.size() > 0) {
            for (Post post : posts) {
                postsCredibility += post.getCredibility();
            }
        }

        return postsCredibility;
    }

    public void incrementCredibility(int increaseAmount) {
        credibility += increaseAmount;
    }

    public void incrementCredibilityByOne() {
        credibility++;
    }

    public void lowerCredibilityByOne() {
        credibility--;
    }

    public Post createPost() {
        Post post = new Post(this);
        posts.add(post);
        return post;
    }


    @Override
    public int hashCode() {
        Integer idAsInt = (Integer) id;
        return idAsInt.hashCode() + username.hashCode();
    }

    @Override
    public boolean equals(Object other) {
        if (other == null) {
            return false;
        }

        if (other instanceof User) {
            User secondUser = (User) other;
            if (getEmail().equals(secondUser.getEmail()) && getUsername().equals(secondUser.getUsername())) {
                return true;
            }

            return false;
        }

        return false;
    }



}
