package com.example.schne.testapp;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.AutoCompleteTextView;
import android.widget.Button;

import com.google.gson.Gson;

import java.io.File;
import java.io.IOException;
import java.nio.file.FileSystems;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;

public class ChangeTagsActivity extends Activity {

    private List<String> shortTags = new ArrayList<>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_add_tags);
        String fileJson = "";
        try {
            fileJson = new String(Files.readAllBytes(FileSystems.getDefault().getPath("sampledata", "tags.json")));
        } catch (IOException e) {

        }

        Tag[] tagArray;
        Gson gson = new Gson();
        tagArray = gson.fromJson(fileJson, Tag[].class);
        for (Tag tag : tagArray) {
            shortTags.add(tag.getShortName());
        }

        AutoCompleteTextView searchForTags = (AutoCompleteTextView) findViewById(R.id.searchForTagsField);
        ArrayAdapter<String> adapter = new ArrayAdapter<String>(this, android.R.layout.simple_dropdown_item_1line, shortTags);
        searchForTags.setAdapter(adapter);

        Button addTag = (Button) findViewById(R.id.addTagButton);
        Button removeTag = (Button) findViewById(R.id.removeTagButton);

        addTag.setOnClickListener(new View.OnClickListener() {
            public void onClick (View v) {

            }
        });



    }

}
