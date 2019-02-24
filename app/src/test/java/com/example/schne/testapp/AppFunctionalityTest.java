package com.example.schne.testapp;

import com.google.gson.Gson;

import org.junit.Before;
import org.junit.Test;

import java.io.IOException;
import java.nio.file.FileSystems;
import java.nio.file.Files;

import static org.junit.Assert.assertEquals;

public class AppFunctionalityTest {

    @Test
    public void fileJsonParseTest() {
        Tag[] tags;
        String fileJson = "";
        try {
            fileJson = new String(Files.readAllBytes(FileSystems.getDefault().getPath("sampledata", "tags.json")));
        } catch (IOException e) {

        }

        Gson gson = new Gson();
        tags = gson.fromJson(fileJson, Tag[].class);
        assertEquals("Computer Science", tags[0].getShortName());
    }


}
