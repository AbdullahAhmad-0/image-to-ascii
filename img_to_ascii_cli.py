import numpy as np # pip install numpy
from PIL import Image # For installing pil pip install pillow

# you can find gray scale level values from: http://paulbourke.net/dataformats/asciiart/ link is in description
 
# 70 levels of gray
gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
 
# 10 levels of gray
gscale2 = '@%#*+=-:. '

def getAvg(img):
    im = np.array(img)
    w, h = im.shape
    return np.average(im.reshape(w * h))
    
def convertImgToAscii(fileName, cols, scale, moreLevels):
    global gscale1, gscale2
    
    # open image and convert it into grayscale
    image = Image.open(fileName).convert('L')
    
    W, H = image.size[0], image.size[1]
    print(f"Image Size {W} x {H}")
    
    # find with of tile
    w = W / cols
    
    # find tile height based on aspect ratio
    h = w / scale
    
    # find no of rows
    rows = int(H / h)
    
    print(f"Rows: {rows}, Cols: {cols}")
    print(f"tile dims: {w} x {h}")
    
    # check if image size is too small
    if cols > W or rows > H:
        print("Iamge Size Is Too Small for given cols")
        exit(0)
        
    # ascii image list of character string
    
    img = []
    
    # genrate list of dimension
    
    for j in range(rows):
        y1 = int(j * h)
        y2 = int((j + 1) * h)
        
        # correct last tile
        if j == rows - 1:
            y2 = H
        
        # append empty string for saving
        img.append("")
        
        for i in range(cols):
            # crop image
            x1 = int(i * w)
            x2 = int((i + 1) * w)
            
            # correct last tile
            if i == cols - 1:
                x2 = W
                
            # crop image to extract tile
            img_ = image.crop((x1, y1, x2, y2))
            
            # get average using numpy
            avg = int(getAvg(img_))
            
            # look ascii char
            if moreLevels == "t": gv = gscale1[int((avg * 69) / 255)]
            else: gv = gscale2[int((avg * 9) / 255)]
            
            img[j] += gv
        
    # return text image in list format
    return img
    

def main():
    imgFile = input("Enter Image Location (Required): ")
    outFile = input("Enter Output Location (Not Required): ")
    cols = input("Enter Cols That You Want (Not Required): ")
    scale = input("Enter Image Scale (Not Required): ")
    moreLevels = input("Enter More Levels t for True f for False (Not Required): ")
    
    if outFile == "":
        outFile = "Output.txt"
    if scale == "":
        scale = 0.43
    scale = float(scale)
    if cols == "":
        cols = 80  # its default value
    cols = int(cols)
    
    img_ = convertImgToAscii(imgFile, cols, scale, moreLevels)
    
    # open file
    f = open(outFile, "w")
    
    # write to file
    for row in img_:
        f.write(row + '\n') # \n for new line we can also use f.writelines(img_)
    f.close()
    
# call main
if __name__ == "__main__":
    main()
    