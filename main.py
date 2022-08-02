from pytube import YouTube
import os
while True:
    def download_video(url):
        yt = YouTube(url)
        videos = yt.streams.all()
        video = list(enumerate(videos))
        for i in video:
            print(i)

        print("İndirmek istediğiniz formatı giriniz: ")
        download_format = int(input("Format numarasını giriniz: "))
        videos[download_format].download()
        print("İndirme Başarılı!")

    if __name__ == "__main__":
        print("Video urlsi girin: ")
        url = input()
        download_video(url)
