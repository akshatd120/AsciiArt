from PIL import Image
import os

# ascii characters used to build the output text 12->Chars
ASCII_CHARS = [" ",".",":", "░", "▒", "▓","█"]

ASCII_CHARS_INV = ["█","▓","▒","░",":","."," "]
def main():
    img = Image.open(input("Enter complete file name: "))
    mode = input("Enter Mode (0,1): ")
    pix = img.load()
    for j in range(0,img.height):
        for i in range(0,img.width):
            avg = (sum(list(pix[i,j])))/4
            rgb = list(pix[i,j])
            avg = int(avg/36.43)
            if(mode == "1"):
                print(ASCII_CHARS[avg],end="")
            else:
                print(ASCII_CHARS_INV[avg],end="")   
        print("",end="\n")
main()

#Simple hello text inside an picture and this was the output

#         ░▓▒  ▒▓▒   ▒▓▓▓▓: ░▓▒     ░▓▒        ▒▓▓▓▓▓▒
#         ░▓▒  ▒▓▒   ▒▓░    ░▓▒     ░▓▒       ▒▓░. ▒▓▒
#         ░▓▒  ▒▓░   ▒▓▒    ░▓▒     ░▓▒       ▒▓░  ▒▓▒
#         ░▓▓▓▓▓▒    ▓▓▓    ░▓░     ░▓░       ▒▓░  ▒▓▒
#         ▒▓▒  ▒▓░   ▒▓░    ▒▓░     ▒▓░       ░▓░  ▒▓▒
#         ▒▓▒  ▒▓░   ▒▓░    ▒▓░     ▒▓░       ░▓▒  ▒▓▒
#         ▒▓▒  ▒▓░   ▒▓▓▓▓░ ▒▓▓▓▓▒  ▒▓▓▓▓     ░▓▓ ▒▓▓▒
#         ▒▓▒  ▒▓░   ▒▓▓▓▓░ ▒▓▓▓▓▒  ▒▓▓▓▓▒    ░▓▓▓▓▓▒
