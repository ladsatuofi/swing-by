package com.example.schne.testapp;

import java.util.ArrayList;
import java.util.List;

public class User {

    private String username;
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

    public int getId() {
        return id;
    }

    User(int newId, String newUsername) {
        id = newId;
        username = newUsername;
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



}
