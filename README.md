# TAIL
書き起こし英語文（IWSLT2017）、翻訳日本語文（IWSLT2017）、音声認識英語文、音声、画像の５つ組みデータセットである

動画・音声・画像を以下の手順で取得できる

## データ作成
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

## 文献情報
寺面杏優, 近藤里咲, 梶原智之, 二宮崇.  
講演動画の言語横断字幕生成のための英日マルチモーダル対訳コーパスの構築.  
言語処理学会第30回年次大会, pp.2002-2006, March 2024.   
https://www.anlp.jp/proceedings/annual_meeting/2024/pdf_dir/P7-11.pdf

## ライセンス
Creative Commons Attribution 4.0 International License (CC BY 4.0)
