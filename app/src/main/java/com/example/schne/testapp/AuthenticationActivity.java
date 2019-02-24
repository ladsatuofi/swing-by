package com.example.schne.testapp;

import android.accounts.AbstractAccountAuthenticator;
import android.accounts.AccountAuthenticatorActivity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class AuthenticationActivity extends AccountAuthenticatorActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


    }

    public String getUsername() {
        return getIntent().getStringExtra("username");
    }

    public String getEmail() {
        return getIntent().getStringExtra("email");
    }




}
