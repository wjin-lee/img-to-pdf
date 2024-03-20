from PIL import Image
import os

print("====================[IMG -> PDF]========================")
print("                    |  v0.0.2  |                        ")
print("========================================================")


def savePDF(image_pathlist, rotation=False, angle=0):
    anchor_image = Image.open(image_pathlist[0])
    parent_dir = os.path.dirname(image_pathlist.pop(0))
    parent_name = parent_dir.split('\\')[-1]


    if rotation:
        anchor_image = anchor_image.rotate(angle, Image.NEAREST, True)

    image_list = []
    for address in image_pathlist:
        img = Image.open(address)
        if rotation:
            img = img.rotate(angle, Image.NEAREST, True)

        image_list.append(img)

    anchor_image.save(f"{parent_dir}\\{parent_name}.pdf", "PDF" ,resolution=100.0, save_all=True, append_images=image_list)
    print(f"PDF output saved to {parent_dir} as {parent_name}.pdf")


while True:
    print('-------------------------------------------------------------')
    ans = input("Please input the target directory (or type 'help'): ")
    if os.path.isdir(ans):
        image_path_list = []
        print('----------------SCANNING----------------')
        for file in os.listdir(ans):
            if os.path.isfile(os.path.join(ans, file)) and (file[-3:] == 'png' or file[-3:] == 'jpg' or file[-4:] == 'jpeg'):
                image_path_list.append(os.path.join(ans, file))
                print(file)

        if len(image_path_list) > 0:
            while True:
                ans = input("Rotate? [ Y / N ]: ")
                if ans.lower() == 'y':
                    try:
                        angle = int(input("Angle (Counter-Clockwise): "))
                        savePDF(image_path_list, rotation=True, angle=angle)
                        break
                    except:
                        print('Invalid Input')


                elif ans.lower() =='n':
                    savePDF(image_path_list)
                    break
                else:
                    print('Invalid Input')



        else:
            print("Could not find any files with the extension 'png', 'jpg', 'jpeg'")


    elif ans.lower() == 'help':
        print("This application will combine a list of images in a directory to a single PDF file at the specified directory.")
        print('Note that ALL images within the directory with the extension of either PNG or JPG will be collated.')
        print('P.S. Angles are rounded to an integer.')

    else:
        print('Invalid Directory')


