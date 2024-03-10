# TAIL
書き起こし英語文（IWSLT2017）、翻訳日本語文（IWSLT2017）、音声認識英語文、音声、画像の５つ組みデータセットである。

動画・音声・画像を以下の手順で取得できる


## 準備
```
mkdir video_directory
mkdir flac_full_directory
mkdir flac_cut_directory
mkdir image_directory
pip install requests
pip install opencv-python
```
また、ffmpeg (https://www.ffmpeg.org/download.html) のダウンロードが必要である。

## URLから動画を取得する
```
python3 get_movie.py "url_list.txt" "video_directory"
```

## 動画を音声に変換しタイムスタンプに基づいて音声を取り出す
```
python3 get_flac.py "timestamp.txt" "video_directory" "flac_full_directory" "flac_cut_directory"

```

## 動画からタイムスタンプに基づいて画像を取り出す
```
python3 get_image.py "timestamp.txt" "video_directory" "image_directory"

```
