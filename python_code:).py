find the mistake(s)!!!!
*from microbit import*
*import music*
happiness = 100
pet = Image.RABBIT
while True:
  display.show(pet)
  if button_a.was_pressed():
    happiness = happiness + 1
    display.show(Image.HAPPY)
    sleep(500)
    display.scroll(int(happiness))
  if button_b.was_pressed():
    happiness = happiness - 1
    display.show(Image.SAD)
    sleep(500)
    display.scroll(int(happiness))
  if happiness == 0:
    display.show(Image.ANGRY)
    sleep(1000)
    music.play(music.WAWAWAWA)
    display.clear()
    
