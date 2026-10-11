#!/bin/bash
# Gradle-free build: needs JDK 17 (JAVA_HOME) and Android SDK (ANDROID_HOME) with platforms;android-34 and build-tools;34.0.0
set -e
cd "$(dirname "$0")/app"
JAVA_HOME=${JAVA_HOME:-$(ls -d /opt/jdk-17* | head -1)}; export PATH=$JAVA_HOME/bin:$PATH
SDK=${ANDROID_HOME:-/opt/android}; BT=$SDK/build-tools/34.0.0; AJ=$SDK/platforms/android-34/android.jar
KS=${KEYSTORE:-$HOME/.android/debug.keystore}
rm -rf out && mkdir -p out/cls
$BT/aapt2 compile --dir res -o out/res.zip
$BT/aapt2 link -I $AJ --manifest AndroidManifest.xml -A assets -o out/base.apk out/res.zip
javac -nowarn -source 8 -target 8 -cp $AJ -d out/cls src/com/knowboran/hifz/Main.java
$BT/d8 --lib $AJ --min-api 24 --output out out/cls/com/knowboran/hifz/*.class
cp out/base.apk out/u.apk
python3 -c "import zipfile;zipfile.ZipFile('out/u.apk','a').write('out/classes.dex','classes.dex')"
$BT/zipalign -f 4 out/u.apk out/a.apk
$BT/apksigner sign --ks "$KS" --ks-pass pass:android --out ../KnowBoran-Hifz.apk out/a.apk
$BT/apksigner verify ../KnowBoran-Hifz.apk && echo "Built ../KnowBoran-Hifz.apk"
