import leaf_sick
import model_generate
import pandas as pd

def extract_data():
    total_mean = leaf_sick.get_total_rgb()/len(leaf_sick.get_mean_array())
    print("THIS IS THE TOTAL MEAN OF IT ALL: ", total_mean)
    global df
    df = pd.DataFrame(leaf_sick.get_dict())
    print(df)

folder_path1 = '/Users/gabrielsirvent/Documents/leaf_sick/Tomato_healthy'
folder_path2 = '/Users/gabrielsirvent/Documents/leaf_sick/Tomato_Late_blight'
leaf_sick.load(folder_path1)
print("")
print("")
leaf_sick.load(folder_path2)
extract_data()
model_generate.generate_model(df)
print("finish")




