package com.example.schne.testapp;

public class Post {

    private String title;
    private String description;
    private String[] dates;
    private String[] times;
    private String location;
    private int credibility = 0;
    private String[] tags;
    private User author;

    public String getTitle() {
        return title;
    }

    public String getDescription() {
        return description;
    }

    public String getLocation() {
        return location;
    }

    public int getCredibility() {
        return credibility;
    }

    public String[] getTags() {
        return tags;
    }

    public User getAuthor() {
        return author;
    }

    Post(User postAuthor) {
        author = postAuthor;
    }


    /**
     * Increases the credibility of the post by a desired amount
     * Also recalculates the author's total credibility
     * @param increaseAmount amount to increase (if their user still exists)
     */
    public void upCredibility(int increaseAmount) {
        credibility += increaseAmount;
        if (author != null) {
            author.incrementCredibility(increaseAmount);
        }
    }

    /**
     * Increases the credibility of the post by one
     * ALso recalcualtes the author's total credibility (if their user still exists)
     */
    public void upCredibilityByOne() {
        credibility++;
        if (author != null) {
            author.incrementCredibilityByOne();
        }
    }

    public void lowerCredibilityByOne() {
        credibility--;
        if (author != null) {
            author.lowerCredibilityByOne();
        }
    }
}
