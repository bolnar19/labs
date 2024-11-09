# importing the module 
from pytube import YouTube 

# Function Takes YouTube Object as Argument.
def video_info(yt):
    print("Author : ",yt.author)
    print("Title : ",yt.title)
    print("Total Length : ",yt.length," Seconds")
    print("Total Views : ",yt.views)
    print("Is Age Restricted : ",yt.age_restricted)
    #print("Video Rating ",round(yt.rating))
    print("Thumbnail Url : ",yt.thumbnail_url)
    print(dir(yt))
    
link = "https://www.youtube.com/watch?v=uztCqjxrkjQ&list=PLV0-i_rHNhfayEhTnncgEVAASKaxO8KuZ&index=1&pp=gAQBiAQB"
yt = YouTube(link) # Create Youtube Object..

# call the function
video_info(yt)
