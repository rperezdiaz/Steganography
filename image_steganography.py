import sys
import os

def extract(key, stego_img):
    bitstring = ''

    for i in range(4, len(key)):
        stego_value = int(stego_img[i])
        key_value = int(key[i])
        bitstring += str( stego_value - key_value )


    #separate into groups of 8
    n=8
    bytes = [(bitstring[i:i+n]) for i in range(0, len(bitstring), n)]

    for i in range(8):
        print (bytes[i])


    return bytes

def embed(carrier, msg):
    stego_img = []
    #add header of carrier ppm to stego_img 
    for i in range(4):
        stego_img.append(carrier[i])

    c_idx = 4
    for i in range(len(msg)):
        byte = msg[i][2:]
        while(len(byte)!= 8):
            byte = '0'+byte
        for bit in byte:
            c_value = int(carrier[c_idx])
            value = int(bit)
            stego_img.append(str(c_value + value))
            c_idx +=1
    for i in range(c_idx, len(carrier)):
        stego_img.append(carrier[i])

    return stego_img

def get_ppm_as_byte_list(image_file_name):
    f = open(sys.path[0] + '/UPRB/images/'+ image_file_name, "r")
    content = f.read()
    content = content.split() #remove white space

    byte_list = []
    for i in range(len(content)):
        binary = toBinary(content[i])

        for i in range(len(binary)):
            binary[i] = str(binary[i])
            while len(binary[i]) != 8:
                binary[i] = '0'+ binary[i]

        byte_list.extend(binary)
    
    f.close()
    return byte_list

def toBinary(a):
    l,m=[],[]
    for i in a:
        l.append(ord(i))
    for i in l:
        m.append(int(bin(i)[2:]))
    return m

def get_ppm_as_list(image_file_name):
    f = open(sys.path[0] + '/UPRB/images/'+ image_file_name, "r")
    content = f.read()

    arr = content.split()
    
    f.close()
    return arr

def reveal_image():
    stego_name = input("Enter Segoimage name (with extension): ")
    key_name = input("Enter key image name (with extension): ")

    stego = get_ppm_as_list(stego_name)
    key = get_ppm_as_list(key_name)

    reveal_img = extract(key, stego)

    f = open("Steganography/UPRB/images/reveal.ppm", "w")
    
    for i in range(len(reveal_img)):
        f.write(str(reveal_img[i])+" ")
    

def hide_image(): 
    carrier_name = input("Enter Carrier name (with extension): ")
    legit_name = input("Enter the name of image you want to hide (with extension): ")

    carrier_size = os.path.getsize(sys.path[0] + '/UPRB/images/' + carrier_name)
    legit_msg_size = os.path.getsize(sys.path[0] + '/UPRB/images/'+ legit_name)

    if(carrier_size > legit_msg_size):
        legit_msg = get_ppm_as_byte_list(legit_name)
        carrier = get_ppm_as_list(carrier_name)

        stego_img = embed(carrier,legit_msg)

        #write stegoimage file
        f = open("Steganography/UPRB/images/stegoimage.ppm", "w")
        for i in range(0,len(stego_img)): 
                f.write(stego_img[i] + " ")
                if i%12 == 0:
                    f.write("\n")
        print("Image successfully hidden!")
    else:
        print("ERROR: Carrier image must be at least 3 times larger than Legit image.")

def show_menu():
    ans = ""
    while ans != 0:
        print("\nWhat do you want to do?")
        print("1. Hide an Image\n2. Extract an Image\n0. EXIT")
        ans = int(input("Enter option number: "))
        if ans == 1:
            hide_image()
        elif ans == 2:
            reveal_image()
        elif ans != 0:
            print("\n\033[93m"+ str(ans), "is not a valid input\033[0m")
            print("\nWhat do you want to do?")
            print("1. Hide an Image\n2. Extract an Image\n0. EXIT")
            ans = int(input("Enter option number: "))

def main():
    show_menu()

if __name__ == "__main__":
    main()
