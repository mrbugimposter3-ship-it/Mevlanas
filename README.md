# KnowBoran Hifz (حفظ)

A fast-paced, fully offline Quran memorization app for Android, with a green theme and an Arabic-first interface.

**Use it in any browser (iPhone, iPad, Android, Surface, desktop):** https://mrbugimposter3-ship-it.github.io/Mevlanas/. To install it as an app, use Add to Home Screen; text works offline after the first load.

## Features
- Complete Quran: 114 surahs, 6,236 ayat, in Uthmani script (right-to-left, Amiri font).
- English transliteration under each ayah. No English translation: meaning comes from a short Arabic explanation (al-Tafsir al-Muyassar) per ayah.
- Home screen starts with Juz 25–30. The full Quran can be browsed by juz or surah.
- Drills: hide/reveal, fill in the missing word, next-ayah recall, and a 60-second timed round.
- XP, streaks, days used and memorized ayat are saved on the device (localStorage).
- Per-ayah recitation by Mishary Rashid Alafasy, streamed (not bundled), with repeat-N and auto-play-next. Text works offline; audio needs internet.

## Install
Download `releases/KnowBoran-Hifz-v1.4.apk` and sideload it. Android 7.0+ is required; it is debug-signed.

## Build
- `python3 prepare_data.py` downloads the text and regenerates `app/assets/www/quran.js`.
- `./build.sh` is a Gradle-free build that needs JDK 17 and an Android SDK with `platforms;android-34` and `build-tools;34.0.0`.
- `build.sh` also copies the web app to `docs/` (GitHub Pages, PWA with manifest and service worker).
- The app itself is `app/assets/www/index.html` wrapped in a minimal WebView (`app/src`).

## Sources and licenses
- **Urdu translation of the infaq ayat** (shown only when the اردو toggle is on): Fateh Muhammad Jalandhry, Al Quran Cloud edition `ur.jalandhry`.
- **Quran text:** Tanzil Quran Text (Uthmani), via the Al Quran Cloud API (`quran-uthmani`). Copyright (C) 2007-2026 Tanzil Project, CC BY 3.0. It is used verbatim without changes to the text. Per Tanzil's terms: "This copy of the Quran text is carefully produced, highly verified and continuously monitored by a group of specialists in Tanzil Project." Source: https://tanzil.net. The only processing is splitting the Basmala off ayah 1 for display, and removing an invisible byte-order mark.
- **Transliteration:** Al Quran Cloud edition `en.transliteration` (from Tanzil).
- **Tafsir:** al-Tafsir al-Muyassar (King Fahd Complex), Al Quran Cloud edition `ar.muyassar`.
- **Audio:** Mishary Alafasy recitation, streamed from `cdn.islamic.network` (Islamic Network / Al Quran Cloud; recordings originally from EveryAyah.com). No audio is redistributed in this repo.
- **Font:** Amiri by Khaled Hosny, SIL Open Font License 1.1 (https://github.com/aliftype/amiri).
- **App code and icon:** original work.

## الإنفاق في سبيل الله · Spending in the way of Allah

> مَّثَلُ ٱلَّذِينَ يُنفِقُونَ أَمْوَٰلَهُمْ فِى سَبِيلِ ٱللَّهِ كَمَثَلِ حَبَّةٍ أَنۢبَتَتْ سَبْعَ سَنَابِلَ فِى كُلِّ سُنۢبُلَةٍۢ مِّا۟ئَةُ حَبَّةٍۢ ۗ وَٱللَّهُ يُضَٰعِفُ لِمَن يَشَآءُ ۗ وَٱللَّهُ وَٰسِعٌ عَلِيمٌ ﴿٢٦١﴾
>
> — سُورَةُ البَقَرَةِ 2:261

> ءَامِنُوا۟ بِٱللَّهِ وَرَسُولِهِۦ وَأَنفِقُوا۟ مِمَّا جَعَلَكُم مُّسْتَخْلَفِينَ فِيهِ ۖ فَٱلَّذِينَ ءَامَنُوا۟ مِنكُمْ وَأَنفَقُوا۟ لَهُمْ أَجْرٌۭ كَبِيرٌۭ ﴿٧﴾
>
> — سُورَةُ الحَدِيدِ 57:7

The app shows a rotating card of ayat on zakat and charity (2:43, 2:245, 2:261, 2:267, 2:274, 9:41, 9:60, 57:7, 61:10–11, 64:16). Text: Tanzil Uthmani via [Al Quran Cloud](https://alquran.cloud) (`quran-uthmani`), used verbatim; generated into `infaq.js`, not typed by hand.

## Tools we use · أدوات نستخدمها

[Postiz](https://postiz.pro/mr-bug) for scheduling social posts. This is a **referral link** (we may earn a commission). It is a tool recommendation, not a charity.
