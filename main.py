# greeting to user
def greeting():
    print(" Welcome to youtube video downloader\n Created by RAPHAEL MKHITARYAN")
    print(" loading...")


greeting()
# importing pytube library
from pytube import YouTube

# url of youtube video and what type of quality user needs to download
url = input(" youtube video url:")
quality = input(" choose quality:(1)360,(2)720,(3)1080 :")

# youtube video URL
yt1 = YouTube(url)
yt = yt1.streams.filter(progressive=False)
####
print("Please wait,video is downloading!")


# which quality needed
def see():
    if quality == "1":
        one = yt.get_by_itag(18)
        if one == None:
            one = yt.get_by_itag(134)
            one.download()
            if one == None:
                one = yt.get_by_itag(34)
                one.download()
                if one == None:
                    one = yt.get_by_itag(43)
                    one.download()
                    if one == None:
                        one = yt.get_by_itag(82)
                        one.download()
                        if one == None:
                            one = yt.get_by_itag(93)
                            one.download()
                            if one == None:
                                one = yt.get_by_itag(100)
                                one.download()
        one.download()
        # print(one)
    elif quality == "2":
        two = yt.get_by_itag(22)
        if two == None:
            two = yt.get_by_itag(136)
            two.download()
            if two == None:
                two = yt.get_by_itag(45)
                two.download()
                if two == None:
                    two = yt.get_by_itag(84)
                    two.download()
                    if two == None:
                        two = yt.get_by_itag(95)
                        two.download()
                        if two == None:
                            two = yt.get_by_itag(102)
                            two.download()
                            if two == None:
                                two = yt.get_by_itag(151)
                                two.download()
                                if two == None:
                                    two = yt.get_by_itag(300)
                                    two.download()

        two.download()
    elif quality == "3":
        three = yt.get_by_itag(137)
        three.download()
        if three == None:
            three = yt.get_by_itag(37)
            three.download()
            if three == None:
                three = yt.get_by_itag(46)
                three.download()
                if three == None:
                    three = yt.get_by_itag(85)
                    three.download()
                    if three == None:
                        three = yt.get_by_itag(96)
                        three.download()
        three.download()


print(see())

# itag = 18 - 360,itag = 22 -720,itag = 137 - 1080,


# not done yet,want to add features:only mp3,downloading playlists,
