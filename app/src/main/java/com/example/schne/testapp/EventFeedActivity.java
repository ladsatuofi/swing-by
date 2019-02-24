package com.example.schne.testapp;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;

import java.util.ArrayList;

public class EventFeedActivity extends Activity {
    ArrayList<String> listItems=new ArrayList<String>();
    ArrayAdapter<String> adapter;
    int clickCounter = 0;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_events);

        Button settings = (Button) findViewById(R.id.settingsButton);
        Button createPost = (Button) findViewById(R.id.postButton);

        adapter = new ArrayAdapter<String>(this, android.R.layout.simple_list_item_1, listItems);
        setAdapter(adapter);
    }

    public void addItems(View v) {
        listItems.add("Clicked : " + clickCounter++);
        adapter.notifyDataSetChanged();
    }

    public void setAdapter(ArrayAdapter<String> adapter) {
        this.adapter = adapter;
    }
}
