import sys

def toBinary(a):
  l,m=[],[]

  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(int(bin(i)[2:]))
  return m[0]

def embed_imgs(carrier, legit_msg):
    stego_img = []
    #add header of carrier ppm to stego_img 
    for i in range(4):
        stego_img.append(carrier[i])

    c_idx = 4
    l_idx = 0
    while(l_idx < len(legit_msg)):
        byte = toBinary(legit_msg[l_idx])
        bits = list(str(byte))
        for i in range (len(bits)):
            value = int(carrier[c_idx])
            bit = int(bits[i])
            stego_img.append( str( value + bit) ) 
            c_idx += 1
        l_idx += 1

    for i in range(c_idx, len(carrier)):
        stego_img.append(carrier[i])
    
    # print(stego_img)


    return stego_img

def get_ppm_as_list(image_file_name):
    f = open(sys.path[0] + '/UPRB/images/'+ image_file_name, "r")
    content = f.read()
    list = content.split()
    f.close()
    return list

def main(): 
    legit_msg = get_ppm_as_list("cotorra_boricua.ppm")
    carrier = get_ppm_as_list("gato.ppm")

    f = open("Steganography\stegoimage.ppm", "w")

    stego_img = embed_imgs(carrier,legit_msg)

    for i in range(0,len(stego_img)): 
            f.write(stego_img[i] + " ")

if __name__ == "__main__":
    main()
