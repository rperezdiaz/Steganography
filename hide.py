import sys

def embed_imgs(carrier, legit_msg):
    stego_img = []
    #add header of carrier ppm to stego_img 
    for i in range(4):
        stego_img.append(carrier[i])

    c_idx= 4
    for i in range(4, len(legit_msg)):
        value = int(legit_msg[i]) #el valor de RGB  -> '0b10101010'
        value ='{0:08b}'.format(value) #remove '0b'
        byte = list(value) # -> separando 10101010 -> [1,0,1,0,1,0,1,0]
        for bit in byte:
            carry_val = int(carrier[c_idx])
            bit_val = int(bit)
            stego_img.append(str(carry_val + bit_val))
            c_idx+=1

    #append remainder of carrier
    for i in range(c_idx, len(carrier)):
        stego_img.append(carrier[i])

    return stego_img

def get_ppm_as_list(image_file_name):
    f = open(sys.path[0] + '/UPRB/images/'+ image_file_name, "r")
    content = f.read()
    list = content.split()
    f.close()
    return list

def main(): 
    legit_msg = get_ppm_as_list("castillo.ppm")
    carrier = get_ppm_as_list("gato.ppm")

    f = open("Steganography/UPRB/images/stegoimage.ppm", "w")

    #save header of original image
    reveal = open("Steganography/UPRB/images/reveal.ppm", "w")
    for i in range(4):
        reveal.write(legit_msg[i]+" ")

    stego_img = embed_imgs(carrier,legit_msg)

    for i in range(0,len(stego_img)): 
            f.write(stego_img[i] + " ")

    print("Hide- Success!")

if __name__ == "__main__":
    main()
