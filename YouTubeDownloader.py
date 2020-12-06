import pytube
from time import sleep
from pytube.cli import on_progress

def video_download(link):
    print("="*50)
    vid = pytube.YouTube(link, on_progress_callback=on_progress)
    print("Name: "+(vid.title)+"\n"+"="*50)
    print("Available downloads:")
    for w in vid.streams.filter(progressive=True):
        print(w)
    reso=input("\n"+"="*50+"\nEnter resolution from above: ")   
    stream=vid.streams.get_by_resolution(reso)
    print("Size: "+str(round(stream.filesize/(1024*1024)))+" MB")
    print("Length:"+str(int((vid.length)/60))+" minutes "+str(int((vid.length)%60))+" seconds\n")
    print("Initiating download\n")
    sleep(5)
    print("============\nDownloading......\n")
    stream.download()
    print((vid.title)+"\nDOWNLOADED \n"+"="*50)

def audio_download(link):
    print("="*50)
    vid = pytube.YouTube(link, on_progress_callback=on_progress)
    print("Name: "+(vid.title)+"\n"+"="*50)
    stream=vid.streams.get_audio_only()
    print("Size: "+str(round(stream.filesize/(1024*1024)))+" MB")
    print("Length:"+str(int((vid.length)/60))+" minutes "+str(int((vid.length)%60))+" seconds\n")
    print("Initiating download\n")  
    sleep(5)
    print("============\nDownloading......\n")
    stream.download()
    print((vid.title)+"\nDOWNLOADED \n"+"="*50)


def playlist_download(link):
     print("="*50)
     p= pytube.Playlist(link)
     print("Playlist Name: "+(p.title)+"\n"+"="*50)
     t=input("To Download videos enter 1 \nTo Download audios enter 2\n")
     if(t=="2"):
         for audio in p.videos:
                print("\n Name: "+(audio.title)+"\n")
                stream=audio.streams.get_audio_only()
                print("Size: "+str(round(stream.filesize/(1024*1024)))+" MB")
                print("Length:"+str(int((audio.length)/60))+" minutes "+str(int((audio.length)%60))+" seconds\n")
                print("Initiating download\n")
                sleep(5)
                print("============ \nDownloading......\n\n")
                stream.download()
                print((audio.title)+"\nDOWNLOADED \n"+"="*50)
     elif(t=="1"):
         for video in p.videos:
                print("\n Name: "+(video.title)+"\n")
                print("Available downloads:")
                for w in video.streams.filter(progressive=True):
                    print(w)
                reso=input("\n"+"="*50+"\nEnter resolution from above: ")   
                stream=video.streams.get_by_resolution(reso)
                print("Size: "+str(round(stream.filesize/(1024*1024)))+" MB")
                print("Length:"+str(int((video.length)/60))+" minutes "+str(int((video.length)%60))+" seconds\n")
                print("Initiating download\n")
                sleep(5)
                print("============ \nDownloading......\n\n")
                stream.download()
                print((video.title)+"\nDOWNLOADED \n"+"="*50)
        

print("="*50)
print("1) Download video")
print("2) Download audio")
print("3) Download playlist")
print("4) Download using custom links file //paste video links sperated by newline in links text file in the same directory")

choice=input("\nEnter choice: ")

if(choice=="1"):
    link=input("\nEnter youtube video link: ")
    video_download(link)

elif(choice=="2"):
    link=input("\nEnter youtube video link: ")
    audio_download(link)
    
elif(choice=="3"):
    link=input("\nEnter youtube playlist link: ")
    playlist_download(link)
    
elif(choice=="4"):
    typ=input("\nChoose Video=1 or audio=2 :\t")
    links=open('links.txt','r')
    
    if(typ=="1"):
        for link in links:
            video_download(link)
        links.close()
    elif(typ=="2"):
        for link in links:
            audio_download(link)
        links.close()

print("="*50)
    
