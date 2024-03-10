# TAIL
既存データの[IWSLT2017](https://wit3.fbk.eu/2017-01-d)の英日対訳コーパスに音声認識英語文、音声、画像を付与した５つ組データセットである  
音声認識は[Google Speech Recognition](https://github.com/Uberi/speech_recognition)で行った  
IWSLT英語文と音声認識文とIWSLT日本語文の３つ組データと音声と画像の取得方法を公開する

## データ数
| all.txt | original | error-correction |
| ------- | -------- | ---------------- |
| 220444  | 106,993  | 84,682           |


## データ説明
- all.txt  
`train/dev/test \t 動画ID \t WER \t IWSLT英語文 \t 音声認識文 \t IWSLT日本語文`  
の形式で記述されている
```
train	1-1	8.33	Thank you so much, Chris. And it's truly a great honor to have the opportunity to come to this stage twice; I'm extremely grateful.	thank you so much Chris and it's it's truly a great honor to have the opportunity to come to the stage twice I'm extremely grateful	どうもありがとう クリス このステージに立てる機会を 2度もいただけるというのは実に光栄なことで とてもうれしく思っています
train	1-2	17.50	I have been blown away by this conference, and I want to thank all of you for the many nice comments about what I had to say the other night. And I say that sincerely, Put yourselves in my position.	I have been blown away by this conference and I want to thank all of you for the the many nice comments about what I had to say the the other night and I say that sincerely partly because	このカンファレンスには圧倒されっぱなしです 皆さんから― 前回の講演に対していただいた温かいコメントにお礼を申し上げたい 心からそう思っています それというのも…ううっ…私には必要なものでしたから！ どうか私の立場で考えてみてください！
train	1-3	100.00	I flew on Air Force Two for eight years.	put yourself in my position	8年間私はエアフォースツーで飛んでいました
```

- original.txt / error-correction.txt  
`train/dev/test \t 動画ID \t IWSLT英語文 \t 音声認識文 \t IWSLT日本語文`  
の形式で記述されている
```
test	1382-1	Today I'm going to talk about unexpected discoveries.	today I'm going to talk about unexpected discoveries	本日お話するのは 思ってもなかった発見についてです
test	1382-2	Now I work in the solar technology industry.	I work in solar technology industry in	私は 太陽光発電の活用に携わっています
test	1382-3	And my small startup is looking to force ourselves into the environment by paying attention to ...	my small startup is looking to force ourselves into the environment by paying attention to	私が始めた小さなベンチャー企業で 目指しているのは 皆さんの周りの環境を クラウドソーシングの･･･
```

- url_list.txt  
`train/dev/test \t 動画ID \t 動画タイトル \t TEDのURL \t 動画のURL`  
の形式で記述されている
```
train	1	Al Gore: Averting the climate crisis	http://www.ted.com/talks/al_gore_on_averting_climate_crisis	https://py.tedcdn.com/consus/projects/00/21/03/001/products/2006-al-gore-001-fallback-cbf9bf8e82c87149b369004928eb3fb8-1200k.mp4
train	2	Amy Smith: Simple designs to save a life	http://www.ted.com/talks/amy_smith_shares_simple_lifesaving_design	https://py.tedcdn.com/consus/projects/00/18/61/002/products/2006-amy-smith-002-fallback-44001df5c6dc1bc6318fa8014c51e14d-1200k.mp4
train	3	Ashraf Ghani: How to rebuild a broken state	http://www.ted.com/talks/ashraf_ghani_on_rebuilding_broken_states	https://py.tedcdn.com/consus/projects/00/15/91/001/products/2005g-ashraf-ghani-001-fallback-88f6a7e532da540cb47bd54f88ec8cf6-1200k.mp4
```

- timestamp.txt  
`動画ID \t テキストID \t タイムスタンプ（head） \t 画像ID（head） \t タイムスタンプ（middle） \t 画像ID（middle） \t タイムスタンプ（tail） \t 画像ID（tail）`  
または  
`動画ID \t テキストID \t タイムスタンプ（tail） \t 画像ID（tail）`  
の形式で記述されている
```
1	1-1	00:0.000	1-1-head	00:5.620	1-1-middle	00:11.240	1-1-tail
1	1-2	00:11.240	1-2-head	00:20.000	1-2-middle	00:28.760	1-2-tail
1	1-3	00:28.760	1-3-head	00:32.680	1-3-middle	00:36.600	1-3-tail
```
```
1	1-105	15:54.354	1-105-tail
2	2-132	14:42.849	2-132-tail
3	3-155	18:22.035	3-155-tail
```


## データ作成
動画・音声・画像を以下の手順で取得できる

### 準備
```
mkdir video_directory
mkdir flac_full_directory
mkdir flac_cut_directory
mkdir image_directory
pip install requests
pip install opencv-python
```
また、ffmpeg (https://www.ffmpeg.org/download.html) のダウンロードが必要である。

### URLから動画を取得する
```
python3 get_movie.py "url_list.txt" "video_directory"
```

### 動画を音声に変換しタイムスタンプに基づいて音声を取り出す
```
python3 get_flac.py "timestamp.txt" "video_directory" "flac_full_directory" "flac_cut_directory"

```

### 動画からタイムスタンプに基づいて画像を取り出す
```
python3 get_image.py "timestamp.txt" "video_directory" "image_directory"

```

### テキストデータの抽出
```
python3 select_line.py "all.txt" output_file wer_1 wer_2 len_1 len_2

# original.txt : 0 <= WER <= 50, 0.8 <= len(asr)/len(iwslt) <= 1.2
# python3 select_line.py "all.txt" output_file 0 50 0.8 1.2
# error-correction.txt : 5 <= WER <= 50, 0.8 <= len(asr)/len(iwslt) <= 1.2
# python3 select_line.py "all.txt" output_file 5 50 0.8 1.2
```


## 文献情報
寺面杏優, 近藤里咲, 梶原智之, 二宮崇.  
講演動画の言語横断字幕生成のための英日マルチモーダル対訳コーパスの構築.  
言語処理学会第30回年次大会, pp.2002-2006, March 2024.   
https://www.anlp.jp/proceedings/annual_meeting/2024/pdf_dir/P7-11.pdf

## ライセンス
Creative Commons Attribution 4.0 International License (CC BY 4.0)
