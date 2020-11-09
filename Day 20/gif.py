from moviepy.editor import*

clip = VideoFileClip("funny_cat.mp4")

#clip = clip.subclip(0,3)

clip.write_gif("mygif.gif")