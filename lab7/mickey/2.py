import pygame 

pygame.init()

screen =  pygame.display.set_mode((800, 600))

theNeighbourhood = [
    r"C:\Users\ASUS\Desktop\pp2\lab7\mickey\music\The Neighbourhood - Compass.mp3",
    r"C:\Users\ASUS\Desktop\pp2\lab7\mickey\music\The Neighbourhood - Softcore.mp3",
    r"C:\Users\ASUS\Desktop\pp2\lab7\mickey\music\The Neighbourhood - Reflections.mp3",
    r"C:\Users\ASUS\Desktop\pp2\lab7\mickey\music\The Neighbourhood - Void.mp3"
]

currentTrack = 0

pygame.mixer.music.load(theNeighbourhood[currentTrack])
pygame.mixer.music.play()

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_RIGHT:
                currentTrack = (currentTrack + 1) % len(theNeighbourhood)
                pygame.mixer.music.load(theNeighbourhood[currentTrack])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                currentTrack = (currentTrack - 1) % len(theNeighbourhood)
                pygame.mixer.music.load(theNeighbourhood[currentTrack])
                pygame.mixer.music.play()

pygame.quit()
