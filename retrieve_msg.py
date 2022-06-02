import sys
def extract(key,stegoimg):
    byte_str = ''
    rgbdata= []
    for i in range(len(key)):
        stego_val = int(stegoimg[i])
        key_val = int(key[i])

        if i <8:
            print(stego_val - key_val)
            
        byte_str += str(stego_val - key_val)

        if len(byte_str) == 8:
            if i < 64:
                print (byte_str)
            rgbdata.append(str(int(byte_str,2)))
            byte_str=''
    return rgbdata
    
def get_ppm_as_list(image_file_name):
    f = open(sys.path[0] + '/UPRB/images/'+ image_file_name, "r")
    content = f.read()
    list = content.split()
    f.close()
    return list

def main(): 
    stegoimage = get_ppm_as_list("stegoimage.ppm")
    keyimage = get_ppm_as_list("gato.ppm")

    msg_rgb = extract(keyimage[4:],stegoimage[4:])
    f = open("Steganography/UPRB/images/reveal.ppm", "a")

    for i in range(0,len(msg_rgb)): 
            f.write(msg_rgb[i] + " ")
    print("Reveal - Success!")

if __name__ == "__main__":
    main()
