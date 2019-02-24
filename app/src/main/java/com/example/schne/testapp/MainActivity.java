package com.example.schne.testapp;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button signIn = (Button) findViewById(R.id.signInButton);

        signIn.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                EditText username = findViewById(R.id.usernameField);
                EditText email = findViewById(R.id.emailField);
                Intent authenticateIntent = new Intent(MainActivity.this, ChangeTagsActivity.class);
                authenticateIntent.putExtra("username", username.getText().toString());
                authenticateIntent.putExtra("email", email.getText().toString());
                startActivity(authenticateIntent);
            }
        });
    }

}
