import os

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames
    of the image files. These pet image labels are used to check the accuracy
    of the labels that are returned by the classifier function, since the
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    results_dic = {}
    for file in os.listdir(image_dir):
        if file[0]!= ".":  # Avoid hidden files such as .DS_STORE
            if file in results_dic.keys():  # Skip duplicates
                print(f"WARNING: duplicate files exist: {file}")
                continue
            else:  # Enter unique values to the dictionary
                filename = str(file).replace("_"," ").lower().strip()
                corrected = ""
                for letter in filename:
                    if letter == " ":
                        corrected += letter
                    elif letter.isalpha():
                        corrected += letter
                results_dic[str(file)] = [corrected[:-4]]

    return results_dic
