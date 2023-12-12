# yt-dlpGUI
yt-dlpをGUI化しただけ

## 機能(ja)
- URL,キーワードでダウンロード
- mp4,mp3,wavでダウンロード可能
- 画質,音質を選択可能
- プレイリストでフォルダ分けが可能

## 保存先について
やる気の関係上、保存先は指定できません。(ソースをいじれば可能ですが…)  
保存先は`/Users/ユーザー名/Documents/yt-dlp`になります。  
おそらくデフォルトではWindowsではドキュメント、MacOSでは書類にyt-dlpというフォルダが作成されるはずです。

## インストール
Releases からzipファイルをダウンロードして,解凍.  
ターミナルでフォルダを開いて  
```
pip install -r requirements.txt
```
で依存関係をダウンロード
```
python app.py
```
で起動できます.  
別に `git clone` しても大丈夫ですよ. 更新も `git pull` でできるしね.
