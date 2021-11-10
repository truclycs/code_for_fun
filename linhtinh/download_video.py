from __future__ import unicode_literals
import youtube_dl
import os
import argparse


def downloadYoutube(path, link):
    ydl_opts = {}
    os.chdir(path)
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([str(link)])


def findMaxInt(path):
    mylist = os.listdir(path)
    name = []
    for i in mylist:
        try:
            num = int(i.split('.')[0])
        except:
            name.append(i)
    for i, v in enumerate(name):
        newname = path + str(i + 36)+'.mp4'
        os.rename(path + v, newname)


def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-v', '--video', help='youtube video link')
    parser.add_argument('-f', '--save_folder', help='folder to save video')

    args = parser.parse_args()
    path = args.save_folder
    video_URL = args.video
    downloadYoutube(path, video_URL)
    # findMaxInt(path)


if __name__ == '__main__':
    main()
