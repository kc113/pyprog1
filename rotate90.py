
def rotate180CW():
  src = makePicture(pickAFile())
  canvas = makeEmptyPicture(getWidth(src),getHeight(src))
  targetX = 0
  height = getHeight(src)
  width = getWidth(src)
  for sourceX in range(0,getWidth(src)):
    targetY = 0
    for sourceY in range(0,getHeight(src)):
      color = getColor(getPixel(src,sourceX,sourceY))
      setColor(getPixel(canvas,width - targetX - 1,height - targetY - 1), color)
      targetY = targetY + 1
    targetX = targetX + 1
  show(canvas)   
  return canvas


  
  
   
  