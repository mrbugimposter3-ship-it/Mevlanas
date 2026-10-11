package com.knowboran.hifz;
import android.app.Activity;import android.os.Bundle;import android.webkit.*;
public class Main extends Activity{WebView w;
protected void onCreate(Bundle b){super.onCreate(b);getWindow().setStatusBarColor(0xff062a1f);w=new WebView(this);
WebSettings s=w.getSettings();s.setJavaScriptEnabled(true);s.setDomStorageEnabled(true);s.setAllowFileAccess(true);s.setMediaPlaybackRequiresUserGesture(false);
w.setWebViewClient(new WebViewClient());w.loadUrl("file:///android_asset/www/index.html");setContentView(w);}
public void onBackPressed(){w.evaluateJavascript("home()",null);}}
