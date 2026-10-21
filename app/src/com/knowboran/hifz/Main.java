package com.knowboran.hifz;
import android.app.Activity;import android.os.Bundle;import android.webkit.*;import android.content.Intent;import android.net.Uri;
public class Main extends Activity{WebView w;
protected void onCreate(Bundle b){super.onCreate(b);getWindow().setStatusBarColor(0xff062a1f);w=new WebView(this);
WebSettings s=w.getSettings();s.setJavaScriptEnabled(true);s.setDomStorageEnabled(true);s.setAllowFileAccess(true);s.setMediaPlaybackRequiresUserGesture(false);
w.setWebViewClient(new WebViewClient(){public boolean shouldOverrideUrlLoading(WebView v,WebResourceRequest r){Uri u=r.getUrl();String sc=u.getScheme();if("http".equals(sc)||"https".equals(sc)){try{startActivity(new Intent(Intent.ACTION_VIEW,u));}catch(Exception e){}return true;}return false;}});
w.getSettings().setSupportMultipleWindows(false);w.loadUrl("file:///android_asset/www/index.html");setContentView(w);}
public void onBackPressed(){w.evaluateJavascript("home()",null);}}
