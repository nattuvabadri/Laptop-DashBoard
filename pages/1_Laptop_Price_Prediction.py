import os
import streamlit as st
import numpy as np
import pandas as pd
import pickle
from PIL import Image
import plotly.express as px

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

encoder = pickle.load(open(r"C:\Users\Badri Nattuva\OneDrive\Desktop\Data_Science_Intern\Laptops DashBoard\resources\data\encoder.pkl", 'rb'))
scaler = pickle.load(open(r"C:\Users\Badri Nattuva\OneDrive\Desktop\Data_Science_Intern\Laptops DashBoard\resources\data\scaler.pkl", 'rb'))
model = pickle.load(open(r"C:\Users\Badri Nattuva\OneDrive\Desktop\Data_Science_Intern\Laptops DashBoard\resources\data\model_1.pkl", 'rb'))

st.title("Laptop Price Prediction")
st.subheader("Enter the Laptop Details")

image1 = Image.open(r"C:\Users\Badri Nattuva\OneDrive\Desktop\Data_Science_Intern\Laptops DashBoard\resources\images\Lap.jpg")
image2 = Image.open(r"C:\Users\Badri Nattuva\OneDrive\Desktop\Data_Science_Intern\Laptops DashBoard\resources\images\Acerlogo.jpg")
image3 = Image.open(r"C:\Users\Badri Nattuva\OneDrive\Desktop\Data_Science_Intern\Laptops DashBoard\resources\images\Applelogo.jpg")
image4 = Image.open(r"C:\Users\Badri Nattuva\OneDrive\Desktop\Data_Science_Intern\Laptops DashBoard\resources\images\Asuslogo.jpg")
image5 = Image.open(r"C:\Users\Badri Nattuva\OneDrive\Desktop\Data_Science_Intern\Laptops DashBoard\resources\images\Delllogo.jpg")
image6 = Image.open(r"C:\Users\Badri Nattuva\OneDrive\Desktop\Data_Science_Intern\Laptops DashBoard\resources\images\HPlogo.jpg")
image7 = Image.open(r"C:\Users\Badri Nattuva\OneDrive\Desktop\Data_Science_Intern\Laptops DashBoard\resources\images\Infinixlogo.jpg")
image8 = Image.open(r"C:\Users\Badri Nattuva\OneDrive\Desktop\Data_Science_Intern\Laptops DashBoard\resources\images\Lenovologo.jpg")
image9 = Image.open(r"C:\Users\Badri Nattuva\OneDrive\Desktop\Data_Science_Intern\Laptops DashBoard\resources\images\MSIlogo.jpg")
image10 = Image.open(r"C:\Users\Badri Nattuva\OneDrive\Desktop\Data_Science_Intern\Laptops DashBoard\resources\images\Realmelogo.jpg")
image11 = Image.open(r"C:\Users\Badri Nattuva\OneDrive\Desktop\Data_Science_Intern\Laptops DashBoard\resources\images\Redmilogo.jpg")
image12 = Image.open(r"C:\Users\Badri Nattuva\OneDrive\Desktop\Data_Science_Intern\Laptops DashBoard\resources\images\Acer.jpg")
image13 = Image.open(r"C:\Users\Badri Nattuva\OneDrive\Desktop\Data_Science_Intern\Laptops DashBoard\resources\images\Applelap.jpg")
image14 = Image.open(r"C:\Users\Badri Nattuva\OneDrive\Desktop\Data_Science_Intern\Laptops DashBoard\resources\images\Asus.jpg")
image15 = Image.open(r"C:\Users\Badri Nattuva\OneDrive\Desktop\Data_Science_Intern\Laptops DashBoard\resources\images\Dell.jpg")
image16 = Image.open(r"C:\Users\Badri Nattuva\OneDrive\Desktop\Data_Science_Intern\Laptops DashBoard\resources\images\HP.jpg")
image17 = Image.open(r"C:\Users\Badri Nattuva\OneDrive\Desktop\Data_Science_Intern\Laptops DashBoard\resources\images\Infinix.jpg")
image18 = Image.open(r"C:\Users\Badri Nattuva\OneDrive\Desktop\Data_Science_Intern\Laptops DashBoard\resources\images\Lenovo.jpg")
image19 = Image.open(r"C:\Users\Badri Nattuva\OneDrive\Desktop\Data_Science_Intern\Laptops DashBoard\resources\images\MSI.jpg")
image20 = Image.open(r"C:\Users\Badri Nattuva\OneDrive\Desktop\Data_Science_Intern\Laptops DashBoard\resources\images\Realme.jpg")
image21 = Image.open(r"C:\Users\Badri Nattuva\OneDrive\Desktop\Data_Science_Intern\Laptops DashBoard\resources\images\Redmi.jpg")
image22 = Image.open(r"C:\Users\Badri Nattuva\OneDrive\Desktop\Data_Science_Intern\Laptops DashBoard\resources\images\Intellogo.jpg")
image23 = Image.open(r"C:\Users\Badri Nattuva\OneDrive\Desktop\Data_Science_Intern\Laptops DashBoard\resources\images\AMDlogo.jpg")
image24 = Image.open(r"C:\Users\Badri Nattuva\OneDrive\Desktop\Data_Science_Intern\Laptops DashBoard\resources\images\Apple.jpg")
st.image(image1)

df = pd.read_csv(r"C:\Users\Badri Nattuva\OneDrive\Desktop\Data_Science_Intern\Laptops DashBoard\resources\data\Clean_Dataset.csv")
df.drop(labels=['Unnamed: 0', 'Price'], axis=1, inplace=True)
st.dataframe(df)

# Here we select Brand Name

Brand=st.selectbox("Brand",("acer", "APPLE", "ASUS", "DELL", "HP", "Infinix", "Lenovo", "MSI", "realme", "RedmiBook"))
if Brand == "acer":
	st.image(image2)
elif Brand == "APPLE":
	st.image(image3)
elif Brand == "ASUS":
	st.image(image4)
elif Brand == "DELL":
	st.image(image5)
elif Brand == "HP":
	st.image(image6)
elif Brand == "Infinix":
	st.image(image7)
elif Brand == "Lenovo":
	st.image(image8)
elif Brand == "MSI":
	st.image(image9)
elif Brand == "realme":
	st.image(image10)
elif Brand == "RedmiBook":
	st.image(image11)
        
# Here we select Processor Company

if Brand == "APPLE":
    p_c = st.selectbox("Processor Company", ("Apple",))
    st.image(image24)
else:
    p_c = st.selectbox("Processor Company", ("Intel", "AMD"))
    if p_c == "Intel":
        st.image(image22)
    elif p_c == "AMD":
        st.image(image23)
        
# Here we select Processor Type
	
if p_c == "Intel":
    processor = st.selectbox("Processor", ("Celeron", "Dual", "Pentium", "i3", "i5", "i7", "i9"))

    if processor == "Celeron":
        ram = st.select_slider("Ram (GB)", (0, 4, 8))
        if ram == 0:
            ram_type = "DDR4"
        else:
            ram_type = st.selectbox("Ram Type", ("DDR4", "LPDDR4", "LPDDR4X"))
    elif processor == "Pentium":
        ram = st.select_slider("Ram (GB)", (0, 8,))
        ram_type = "DDR4"
    else:
        ram = st.select_slider("Ram (GB)", (0, 4, 8, 16, 32))
        ram_type = st.selectbox("Ram Type", ("DDR4", "DDR5", "LPDDR4", "LPDDR4X", "LPDDR5", "Unified"))

elif p_c == "AMD":
    processor = st.selectbox("Processor", ("Athlon", "r3", "r5", "r7", "r9"))
    ram = st.select_slider("Ram (GB)", (0, 4, 8, 16, 32))
    ram_type = st.selectbox("Ram Type", ("DDR4", "DDR5", "LPDDR4", "LPDDR4X", "LPDDR5", "Unified"))

elif p_c == "Apple":
    processor = st.selectbox("Processor", ("M1", "M1P", "M2", "M1M"))
    ram = st.select_slider("Ram (GB)", (0, 4, 8, 16, 32))
    ram_type = st.selectbox("Ram Type", ("DDR4", "DDR5", "LPDDR4", "LPDDR4X", "LPDDR5", "Unified"))
    
# Here we Select Operating System

if p_c == "Intel" or p_c == "AMD":
    OS = st.selectbox("Operating System", ("DOS", "Chrome", "win10", "win11"))
elif p_c == "Apple":
    OS = st.selectbox("Operating System", ("MacOS",))

# Here we Select Type of Screen

touch_scr=st.selectbox("Touch Screen",("yes","no"))

# Here we Select Type of Storage in SSD

ssd=st.select_slider("SSD GB",(0, 128, 256, 512, 1020, 2040))

# Here we Select Type of Storage in HDD

hdd=st.select_slider("HDD GB",(0, 256, 1020))



X_test_num=pd.DataFrame({"Ram_1":ram,"SSD":ssd,"HDD":hdd},index=[0])
X_test_cat=pd.DataFrame({"processor_company":p_c,"Ram_type":ram_type,"Processor":processor,"Brand":Brand,"Operating_System":OS,"Touch_Screen":touch_scr},index=[0])


X_test_num_rescaled = pd.DataFrame(scaler.transform(X_test_num)) 
                                    

X_test_cat_ohe = pd.DataFrame(encoder.transform(X_test_cat)) 
                               

X_test_transformed = pd.concat([X_test_num_rescaled, X_test_cat_ohe], axis=1)

but = st.button("Predict Price")
if ram == 0 and ssd == 0 and hdd == 0:
    st.subheader("Invalid Values Please check and Enter valid Values.")
elif ram == 0 and ssd == 0:
     st.subheader("Invalid Values Please check the RAM and SDD Values and Enter valid Values.")
elif ram == 0 and hdd == 0:
     st.subheader("Invalid Values Please check the RAM and HDD Values and Enter valid Values.")
elif ssd == 0 and hdd == 0:
     st.subheader("Invalid Values Please check the SSD and HDD Values and Enter valid Values.")
else:
    # Perform calculations or show results based on valid values
    if but == True:
        pred = model.predict(X_test_transformed)
        st.subheader("The Price of the Laptop is ₹ {}".format(pred[0].round(2)))
        if Brand == "acer":
            st.image(image12)
        elif Brand == "APPLE":
            st.image(image13)
        elif Brand == "ASUS":
            st.image(image14)
        elif Brand == "DELL":
            st.image(image15)
        elif Brand == "HP":
            st.image(image16)
        elif Brand == "Infinix":
            st.image(image17)
        elif Brand == "Lenovo":
            st.image(image18)
        elif Brand == "MSI":
            st.image(image19)
        elif Brand == "realme":
            st.image(image20)
        elif Brand == "RedmiBook":
            st.image(image21)

