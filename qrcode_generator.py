import qrcode

def qr_code_generator(filepath):
    
    try:
        with open(filepath, "r") as file:
            file_lines=file.readlines()

        if len(file_lines)<2:
            print("File lines cannot be less than 2")
            return
        
        text=file_lines[0].strip()
        filename=file_lines[1].strip()

        image_make=qrcode.make(text)
        image_make.save(filename)
        print("QR Code saved successfully")

    except FileNotFoundError:
        print(f"{filepath} file not found")

qr_code_generator("Qr_code.txt")

        
