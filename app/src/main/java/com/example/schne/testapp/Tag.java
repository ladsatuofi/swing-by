package com.example.schne.testapp;

public class Tag {

    private String shortName;
    private String longName;

    Tag(String newShortName, String newLongName) {
        shortName = newShortName;
        longName = newLongName;
    }

    public String getShortName() {
        return shortName;
    }

    public String getLongName() {
        return longName;
    }


}
