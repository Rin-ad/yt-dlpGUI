import yt_dlp
import flet as ft
from flet import (
    Text,TextField,Page,
)
import time
from os.path import expanduser

home = expanduser("~")

#App Window
def main(page:Page):
    page.title = "yt-dlpGUI"
    page.padding = 24
    page.window_width = 550

    #Quality selection dropdown options
    sel_mp4 = [ft.dropdown.Option('Auto'),ft.dropdown.Option('1080p'),ft.dropdown.Option('720p')]
    sel_mp3 = [ft.dropdown.Option('Auto'),ft.dropdown.Option('320K'),ft.dropdown.Option('192K')]
    
    #Change quality settings dropdown choices when format selection dropdown changes.
    def formatdd_changed(e):
        if format_dd.value == "mp4":
            quality_dd.options = sel_mp4
            quality_dd.value = "Auto"
            quality_dd.update()
        elif format_dd.value == "mp3":
            quality_dd.options = sel_mp3
            quality_dd.value = "Auto"
            quality_dd.update()
        elif format_dd.value == "wav":
            quality_dd.options = [ft.dropdown.Option('Auto')]
            quality_dd.value = "Auto"
            quality_dd.update()
    
    #Called when a video is downloaded.
    def download_video(url,format,opt):
        dl_btn.disabled = True
        progress_text.value = "Downloading..."
        progress_text.update()
        dl_btn.update()
        #Update progress information
        def hook(d):
            info_dict = d.get('info_dict')
            movie_title = info_dict.get('title')
            playlist_title = info_dict.get('playlist_title')
            progress_title.value = movie_title
            progress_playlist.value = playlist_title
            progress_title.update()
            progress_playlist.update()
            if d['status'] == 'downloading':
                progress_ps = float(d['_percent_str'].replace('%', ''))
                progress_bar.visible = True
                percent_value_scaled = progress_ps * 0.01
                progress_bar.value = percent_value_scaled
                progress_text.value = f"Downloading... Progress:{progress_ps}%"
                progress_bar.update()
                progress_text.update()
        ydl_opts = {
            'progress_hooks': [hook],
            'format': format,
            'noprogress':True,
            'ignoreerrors':True,
            'color':'no_color',
            'writethumbnail': 'true',
            'default_search': 'ytsearch',
            'postprocessors':[{
                'key':'FFmpegMetadata',
                'add_metadata': True
            },
            {
                'key': 'EmbedThumbnail',
                'already_have_thumbnail': False,
            }],
            'outtmpl': f'{home}/Documents/yt-dlp/video/{opt}%(title)s.%(ext)s'
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        dl_btn.disabled = False
        progress_text.value = "No Task"
        progress_text.update()
        dl_btn.update()

    #Called when a audio is downloaded.
    def download_audio(url,format,audio,quality,opt):
        dl_btn.disabled = True
        progress_text.value = "Downloading..."
        progress_text.update()
        dl_btn.update()
        #Update progress information
        def hook(d):
            info_dict = d.get('info_dict')
            movie_title = info_dict.get('title')
            playlist_title = info_dict.get('playlist_title')
            progress_title.value = movie_title
            progress_playlist.value = playlist_title
            progress_title.update()
            progress_playlist.update()
            if d['status'] == 'downloading':
                progress_ps = float(d['_percent_str'].replace('%', ''))
                progress_bar.visible = True
                percent_value_scaled = progress_ps * 0.01
                progress_bar.value = percent_value_scaled
                progress_text.value = f"Downloading... Progress:{progress_ps}%"
                progress_bar.update()
                progress_text.update()
        ydl_opts = {
            'progress_hooks': [hook],
            'format': format,
            'noprogress': True,
            'color':'no_color',
            'outtmpl': f'{home}/Documents/yt-dlp/audio/{opt}%(title)s.%(ext)s',
            'postprocessors':[{
                'key':'FFmpegExtractAudio',
                'preferredcodec':audio,
                'preferredquality':quality
            },
            {
                'key':'FFmpegMetadata',
                'add_metadata': True
            }],
            'default_search': 'ytsearch'
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        dl_btn.disabled = False
        progress_text.value = "No Task"
        progress_text.update()
        dl_btn.update()

    #Called when the download button is pressed.
    def initialize_download(e):
        if url_input.value == "" or format_dd.value =="" or quality_dd.value == "":
            progress_text.value = "Please select an option."
            progress_text.update()
            time.sleep(3)
            progress_text.value = "No Task"
            progress_text.update()
            return
        if format_dd.value == "mp4":
            if quality_dd.value == "Auto" and playlist_sw.value == True:
                cmd = "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]"
                opt = "%(playlist_title)s/"
                download_video(url_input.value,cmd,opt)
            elif quality_dd.value == "Auto" and playlist_sw.value == False:
                cmd = "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]"
                opt = ""
                download_video(url_input.value,cmd,opt)
            elif quality_dd.value == "1080p" and playlist_sw.value == True:
                cmd = "bestvideo[ext=mp4][height=1080]+bestaudio[ext=m4a]/best[ext=mp4][height=1080]"
                opt = "%(playlist_title)s/"
                download_video(url_input.value,cmd,opt)
            elif quality_dd.value == "1080p" and playlist_sw.value == False:
                cmd = "bestvideo[ext=mp4][height=1080]+bestaudio[ext=m4a]/best[ext=mp4][height=1080]"
                opt = ""
                download_video(url_input.value,cmd,opt)
            elif quality_dd.value == "720p" and playlist_sw.value == True:
                cmd = "bestvideo[ext=mp4][height=720]+bestaudio[ext=m4a]/best[ext=mp4][height=720]"
                opt = "%(playlist_title)s/"
                download_video(url_input.value,cmd,opt)
            elif quality_dd.value == "720p" and playlist_sw.value == False:
                cmd = "bestvideo[ext=mp4][height=720]+bestaudio[ext=m4a]/best[ext=mp4][height=720]"
                opt = ""
                download_video(url_input.value,cmd,opt)
        elif format_dd.value == "mp3":
            if quality_dd.value == "Auto" and playlist_sw.value == True:
                cmd = "bestaudio"
                opt = "%(playlist_title)s/"
                download_audio(url_input.value,cmd,'mp3','',opt)
            elif quality_dd.value == "Auto" and playlist_sw.value == False:
                cmd = "bestaudio"
                opt = ""
                download_audio(url_input.value,cmd,'mp3','',opt)
            elif quality_dd.value == "320K" and playlist_sw.value == True:
                cmd = "bestaudio"
                opt = "%(playlist_title)s/"
                download_audio(url_input.value,cmd,'mp3','320',opt)
            elif quality_dd.value == "320K" and playlist_sw.value == False:
                cmd = "bestaudio"
                opt = ""
                download_audio(url_input.value,cmd,'mp3','320',opt)
            elif quality_dd.value == "192K" and playlist_sw.value == True:
                cmd = "bestaudio"
                opt = "%(playlist_title)s/"
                download_audio(url_input.value,cmd,'mp3','192',opt)
            elif quality_dd.value == "192K" and playlist_sw.value == False:
                cmd = "bestaudio"
                opt = ""
                download_audio(url_input.value,cmd,'mp3','192',opt)
        elif format_dd.value == "wav":
            if quality_dd.value == "Auto" and playlist_sw.value == True:
                cmd = "bestaudio"
                opt = "%(playlist_title)s/"
                download_audio(url_input.value,cmd,'wav','',opt)
            elif quality_dd.value == "Auto" and playlist_sw.value == False:
                cmd = "bestaudio"
                opt = ""
                download_audio(url_input.value,cmd,'wav','',opt)

    #define element
    text = Text("yt-dlpGUI",size=24,weight=ft.FontWeight.BOLD)
    url_input = TextField(hint_text="Enter video URL or keyword here",label="URL or Keyword")
    format_dd = ft.Dropdown(label="Format",options=[ft.dropdown.Option("mp4"),ft.dropdown.Option('mp3'),ft.dropdown.Option("wav")],on_change=formatdd_changed)
    quality_dd = ft.Dropdown(label="Quality")
    playlist_sw = ft.Switch(label="Sort into folders by playlist")
    dl_btn = ft.FilledButton("Download",icon=ft.icons.DOWNLOAD,on_click=initialize_download)
    progress_text = ft.Text(value="No Task")
    progress_bar = ft.ProgressBar(value=0)
    progress_title = ft.TextField(read_only=True,label="Downloading Title")
    progress_playlist = ft.TextField(read_only=True,label="Downloading Playlist")

    page.add(text,url_input,format_dd,quality_dd,playlist_sw,ft.Row([dl_btn,progress_text]),ft.Text("Progress:",size=16,weight=ft.FontWeight.BOLD),progress_title,progress_playlist,progress_bar)

#Run App
ft.app(main)
