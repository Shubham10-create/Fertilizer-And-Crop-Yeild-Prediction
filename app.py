from pyexpat import model
from xml.sax.handler import feature_string_interning
from django.forms import NumberInput
import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open("random_forest_classification_model.pkl", "rb"))
model1 = pickle.load(open("random_forest_regression_model.pkl", "rb"))

nav = st.sidebar.radio("What would you like to predict ?",options = ["Fertilizer Prediction","Crop Prediction"])


if nav == "Fertilizer Prediction":
    st.header("Fertilizer Prediction")
    st.image("fertlizer.jpg")
    st.write("Please select values, to get right fertilizer to used:")

    temperature = st.slider("Temperature", 25, 40)
    humidity = st.slider("Humidity", 50, 75)
    moisture = st.slider("Moisture", 25, 65)
    nitrogen = st.slider("Nitrogen",5,41)
    potassium = st.slider("Potassium",0,19)
    phosphorous = st.slider("Phosphorous",0,42)

    soil_type = st.selectbox("Soil Type", ["Sandy", "Loamy", "Black", "Red", "Clayey"])
    Soil_type_sandy, Soil_Type_Clayey, Soil_Type_Loamy, Soil_Type_Red = 0, 0, 0, 0

    if(soil_type == "Sandy"):
        Soil_type_sandy = 1
    elif(soil_type == 'Clayey'):
        Soil_Type_Clayey = 1    

    elif(soil_type == 'Loamy'):
        Soil_Type_Loamy = 1
    elif(soil_type == 'Red'):
        Soil_Type_Red = 1

    crop_type = st.selectbox("Crop Type",["Maize", "Sugarcane", "Cotton", "Tobacco", "Paddy","Barley",
         "Wheat", "Millets", "Oil seeds", "Pulses", "Ground Nuts"])

    Crop_type_Maize, Crop_type_Sugarcane, Crop_type_Cotton, Crop_type_Tobacco, Crop_type_Paddy, Crop_type_Wheat, Crop_type_Millets, Crop_Type_Ground_Nuts, Crop_type_Oil_seeds, Crop_type_Pulses = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

    if(crop_type == "Maize"):
        Crop_type_Maize = 1
    elif(crop_type == "Sugarcane"):
        Crop_type_Sugarcane = 1
    elif(crop_type == "Cotton"):
        Crop_type_Cotton = 1
    elif(crop_type == "Tobacco"):
        Crop_type_Tobacco = 1
    elif(crop_type == "Paddy"):
        Crop_type_Paddy = 1
    elif(crop_type == "Wheat"):
        Crop_type_Wheat = 1
    elif(crop_type == "Millets"):
        Crop_type_Millets = 1
    elif(crop_type == "Ground Nuts"):
        Crop_Type_Ground_Nuts = 1
    elif(crop_type == "Oil seeds"):
        Crop_type_Oil_seeds = 1
    elif(crop_type == "Pulses"):
        Crop_type_Pulses = 1

    data = {
        "Temperature":temperature,
        "Humidity":humidity,
        "Moisture":moisture,
        "Nitrogen":nitrogen,
        "Potassium":potassium,
        "Phosphorous":phosphorous,
        "Soil_Type_Clayey": Soil_Type_Clayey,
        "Soil_Type_Loamy": Soil_Type_Loamy,
        "Soil_Type_Red": Soil_Type_Red,
        'Soil_Type_Sandy': Soil_type_sandy,
        'Crop_Type_Cotton': Crop_type_Cotton,
        'Crop_Type_Ground_Nuts': Crop_Type_Ground_Nuts,
        'Crop_Type_Maize': Crop_type_Maize,
        'Crop_Type_Millets': Crop_type_Millets,
        'Crop_Type_Oil_seeds': Crop_type_Oil_seeds,
        'Crop_Type_Paddy': Crop_type_Paddy,
        'Crop_Type_Pulses': Crop_type_Pulses,
        'Crop_Type_Sugarcane': Crop_type_Sugarcane,
        'Crop_Type_Tobacco': Crop_type_Tobacco,
        'Crop_Type_Wheat' : Crop_type_Wheat
    }

    features = pd.DataFrame(data,index=[0])
                   
    expected_features = ['Temparature', 'Humidity ', 'Moisture', 'Nitrogen', 'Potassium',
           'Phosphorous', 'Soil_Type_Clayey', 'Soil_Type_Loamy', 'Soil_Type_Red',
           'Soil_Type_Sandy', 'Crop_Type_Cotton', 'Crop_Type_Ground_Nuts',
           'Crop_Type_Maize', 'Crop_Type_Millets', 'Crop_Type_Oil_seeds',
           'Crop_Type_Paddy', 'Crop_Type_Pulses', 'Crop_Type_Sugarcane',
           'Crop_Type_Tobacco', 'Crop_Type_Wheat']

#print(list(features.columns))
#assert list(features.columns) == expected_features

    if st.button('Predict'):
        prediction = model.predict(features)
        if(prediction == 0):
            st.write("The fertilizer preffered is Urea")
        elif(prediction == 1):
            st.write("The fertilizer preffered is DAP")
        elif(prediction == 2):
            st.write("The fertilizer preffered is 14-35-14")
        elif(prediction == 3):
            st.write("The fertilizer preffered is 28-28")
        elif(prediction == 4):
            st.write("The fertilizer preffered is 17-17-17")
        elif(prediction == 5):
            st.write("The fertilizer preffered is 20-20")
    else:
        st.write("The fertilizer preffered is 10-26-26")

else:
    st.header("Crop Yield Prediction")
    st.image("crop.jpg")
    st.write("Please insert values, to get right crop to used:")


    #area = st.text_input("Area", 0.2, 877029.0)
   # production = st.text_input("Production", 0.0,780162000.0)
    area = st.number_input('Area of land...',min_value=0.2,max_value=877029.0,format="%.2f")
    production = st.number_input('Production...',min_value=0.0,max_value=780162000.0,format="%.2f")



    season = st.selectbox("Season", ['Kharif', 'Whole Year', 'Autumn', 'Rabi'])
    season_Kharif, season_Whole_Year, season_Rabi = 0, 0, 0

    if(season == "Kharif"):
        season_Kharif = 1
    elif(season == 'Whole year'):
        season_Whole_year = 1
    elif(season == 'Rabi'):
        season_Rabi = 1
    
    crop = st.selectbox("Crop",['Arecanut','Arhar/Tur', "Bajra",'Banana','Beans & Mutter(Vegetable)','Bhindi','Black pepper',
    'Bottle Gourd','Brinjal','Cabbage','Cashewnut','Castor seed','Citrus Fruit','Coconut','Coriander','Cotton(lint)', 'Cowpea(Lobia)',
       'Cucumber', 'Dry chillies', 'Dry ginger', 'Garlic','Ginger', 'Gram', 'Grapes', 'Groundnut','Horse-gram', 'Jowar', 'Korra', 'Lemon',
       'Linseed', 'Maize', 'Mango', 'Masoor', 'Mesta','Moong(Green Gram)', 'Niger seed','Oilseeds total','Onion', 'Orange', 'Other  Rabi pulses',
       'Other Fresh Fruits', 'Other Kharif pulses','Other Vegetables', 'Papaya', 'Peas  (vegetable)','Pome Fruit', 'Pome Granet', 'Potato',
       'Pulses total', 'Ragi', 'Rapeseed &Mustard', 'Rice','Safflower', 'Samai', 'Sapota', 'Sesamum','Small millets', 'Soyabean', 'Sugarcane',
       'Sunflower', 'Sweet potato', 'Tapioca', 'Tobacco','Tomato', 'Turmeric', 'Urad', 'Varagu','Wheat', 'other fibres', 'other misc. pulses',
       'other oilseeds'])

    crop_Arhar_Tur, crop_Bajra, crop_Banana, crop_Beans_Mutter_Vegetable, crop_Bhindi, crop_Black_pepper, crop_Bottle_Gourd, crop_Brinjal, crop_Cabbage, crop_Cashewnut, crop_Castor_seed, crop_Citrus_Fruit, crop_Coconut, crop_Coriander, crop_Cotton_lint, crop_Cowpea_Lobia, crop_Cucumber, crop_Dry_chillies, crop_Dry_ginger, crop_Garlic, crop_Ginger, crop_Gram, crop_Grapes, crop_Groundnut, crop_Horse_gram, crop_Jowar, crop_Korra, crop_Lemon, crop_Linseed, crop_Maize, crop_Mango, crop_Masoor, crop_Mesta, crop_Moong_Green_Gram, crop_Niger_seed, crop_Oilseeds_total, crop_Onion, crop_Orange, crop_Other_Rabi_pulses, crop_Other_Fresh_Fruits, crop_Other_Kharif_pulses, crop_Other_Vegetables, crop_Papaya, crop_Peas_vegetable, crop_Pome_Fruit, crop_Pome_Granet, crop_Potato, crop_Pulses_total, crop_Ragi, crop_Rapeseed_Mustard, crop_Rice, crop_Safflower, crop_Samai, crop_Sapota, crop_Sesamum, crop_Small_millets, crop_Soyabean, crop_Sugarcane, crop_Sunflower, crop_Sweet_potato, crop_Tapioca, crop_Tobacco, crop_Tomato, crop_Turmeric, crop_Urad, crop_Varagu, crop_Wheat, crop_other_fibres, crop_other_misc_pulses, crop_other_oilseeds = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
   
    if(crop == "Arhar/Tur"):
        crop_Arhar_Tur = 1
    elif(crop == "Bajra"):
        crop_Bajra = 1
    elif(crop == "Banana"):
        crop_Banana = 1
    elif(crop == "Beans & Mutter(Vegetable)"):
        crop_Beans_Mutter_Vegetable = 1
    elif(crop == "Bhindi"):
        crop_Bhindi = 1
    elif(crop == "Bottle Gourd"):
        crop_Bottle_Gourd = 1
    elif(crop == "Brinjal"):
        crop_Brinjal = 1
    elif(crop == "Cabbage"):
        crop_Cabbage = 1
    elif(crop == "Cashewnut"):
        crop_Cashewnut = 1
    elif(crop == "Castor seed"):
        crop_Castor_seed = 1
    elif(crop == "Citrus Fruit"):
        crop_Citrus_Fruit = 1
    elif(crop == "Coconut"):
        crop_Coconut = 1
    elif(crop == "Coriander"):
        crop_Coriander = 1
    elif(crop == "Cotton(lint)"):
        crop_Cotton_lint = 1
    elif(crop == "Cowpea(Lobia)"):
        crop_Cowpea_Lobia = 1
    elif(crop == "Cucumber"):
        crop_Cucumber = 1
    elif(crop == "Dry chillies"):
        crop_Dry_chillies = 1
    elif(crop == "Dry ginger"):
        crop_Dry_ginger = 1
    elif(crop == "Garlic"):
        crop_Garlic = 1
    elif(crop == "Ginger"):
        crop_Ginger = 1
    elif(crop == "Gram"):
        crop_Gram = 1
    elif(crop == "Grapes"):
        crop_Grapes = 1
    elif(crop == "Groundnut"):
        crop_Groundnut = 1
    elif(crop == "Horse-gram"):
        crop_Horse_gram = 1
    elif(crop == "Jowar"):
        crop_Jowar = 1
    elif(crop == "Korra"):
        crop_Korra = 1
    elif(crop == "Lemon"):
        crop_Lemon = 1
    elif(crop == "Linseed"):
        crop_Linseed = 1
    elif(crop == "Maize"):
        crop_Maize = 1
    elif(crop == "Mango"):
        crop_Mango = 1
    elif(crop == "Masoor"):
        crop_Masoor = 1
    elif(crop == "Mesta"):
        crop_Mesta = 1
    elif(crop == "Moong(Green Gram)"):
        crop_Moong_Green_Gram = 1
    elif(crop == "Niger seed"):
        crop_Niger_seed = 1
    elif(crop == "Oilseeds total"):
        crop_Oilseeds_total = 1
    elif(crop == "Onion"):
        crop_Onion = 1
    elif(crop == "Orange"):
        crop_Orange = 1
    elif(crop == "Other  Rabi pulses"):
        crop_Other_Rabi_pulses = 1
    elif(crop == "Other Fresh Fruits"):
        crop_Other_Fresh_Fruits = 1
    elif(crop == "Other Kharif pulses"):
        crop_Other_Kharif_pulses = 1
    elif(crop == "Other Vegetables"):
        crop_Other_Vegetables = 1
    elif(crop == "Papaya"):
        crop_Papaya = 1
    elif(crop == "Peas  (vegetable)"):
        crop_Peas_vegetable = 1
    elif(crop == "Pome Fruit"):
        crop_Pome_Fruit = 1
    elif(crop == "Pome Granet"):
        crop_Pome_Granet = 1
    elif(crop == "Potato"):
        crop_Potato = 1
    elif(crop == "Pulses total"):
        crop_Pulses_total = 1
    elif(crop == "Ragi"):
        crop_Ragi = 1
    elif(crop == "Rapeseed &Mustard"):
        crop_Rapeseed_Mustard = 1
    elif(crop == "Rice"):
        crop_Rice = 1
    elif(crop == "Safflower"):
        crop_Safflower = 1
    elif(crop == "Samai"):
        crop_Samai = 1
    elif(crop == "Sapota"):
        crop_Sapota = 1
    elif(crop == "Sesamum"):
        crop_Sesamum = 1
    elif(crop == "Small millets"):
        crop_Small_millets = 1
    elif(crop == "Soyabean"):
        crop_Soyabean = 1
    elif(crop == "Sugarcane"):
        crop_Sugarcane = 1
    elif(crop == "Sunflower"):
        crop_Sunflower = 1
    elif(crop == "Sweet potato"):
        crop_Sweet_potato = 1
    elif(crop == "Tapioca"):
        crop_Tapioca = 1
    elif(crop == "Tobacco"):
        crop_Tobacco = 1
    elif(crop == "Tomato"):
        crop_Tomato = 1
    elif(crop == "Turmeric"):
        crop_Turmeric = 1
    elif(crop == "Urad"):
        crop_Urad = 1
    elif(crop == "Varagu"):
        crop_Varagu = 1
    elif(crop == "Wheat"):
        crop_Wheat = 1
    elif(crop == "other fibres"):
        crop_other_fibres = 1
    elif(crop == "other misc. pulses"):
        crop_other_misc_pulses = 1
    elif(crop == "other oilseeds"):
        crop_other_oilseeds = 1
    
    
    data = {
        "Area":area,
        "Production":production,
        "season_Kharif": season_Kharif,
        "season_Whole_Year": season_Whole_Year,
        "season_Rabi": season_Rabi,
        'crop_Arhar_Tur': crop_Arhar_Tur,
        'crop_Bajra': crop_Bajra,
        'crop_Banana': crop_Banana,
        'crop_Beans_Mutter_Vegetable': crop_Beans_Mutter_Vegetable, 
        'crop_Bhindi': crop_Bhindi,
        'crop_Black_pepper': crop_Black_pepper,
        'crop_Bottle_Gourd': crop_Bottle_Gourd,
        'crop_Brinjal': crop_Brinjal,
        'crop_Cabbage': crop_Cabbage,
        'crop_Cashewnut': crop_Cashewnut,
        'crop_Castor_seed': crop_Castor_seed,
        'crop_Citrus_Fruit': crop_Citrus_Fruit,
        'crop_Coconut': crop_Coconut,
        'crop_Coriander': crop_Coriander,
        'crop_Cotton_lint': crop_Cotton_lint,
        'crop_Cowpea_Lobia': crop_Cowpea_Lobia,
        'crop_Cucumber': crop_Cucumber,
        'crop_Dry_chillies': crop_Dry_chillies,
        'crop_Dry_ginger': crop_Dry_ginger,
        'crop_Garlic': crop_Garlic,
        'crop_Ginger': crop_Ginger,
        'crop_Gram': crop_Gram,
        'crop_Grapes': crop_Grapes,
        'crop_Groundnut': crop_Groundnut,
        'crop_Horse_gram': crop_Horse_gram,
        'crop_Jowar': crop_Jowar,
        'crop_Korra': crop_Korra,
        'crop_Lemon': crop_Lemon,
        'crop_Linseed': crop_Linseed,
        'crop_Maize': crop_Maize,
        'crop_Mango': crop_Mango,
        'crop_Masoor': crop_Masoor,
        'crop_Mesta': crop_Mesta,
        'crop_Moong_Green_Gram': crop_Moong_Green_Gram,
        'crop_Niger_seed':crop_Niger_seed,
        'crop_Oilseeds_total': crop_Oilseeds_total,
        'crop_Onion': crop_Onion,
        'crop_Orange': crop_Orange,
        'crop_Other_Rabi_pulses': crop_Other_Rabi_pulses,
        'crop_Other_Fresh_Fruits': crop_Other_Fresh_Fruits,
        'crop_Other_Kharif_pulses': crop_Other_Kharif_pulses,
        'crop_Other_Vegetables': crop_Other_Vegetables,
        'crop_Papaya': crop_Papaya,
        'crop_Peas_vegetable': crop_Peas_vegetable,
        'crop_Pome_Fruit': crop_Pome_Fruit,
        'crop_Pome_Granet': crop_Pome_Granet,
        'crop_Potato': crop_Potato,
        'crop_Pulses_total': crop_Pulses_total,
        'crop_Ragi': crop_Ragi,
        'crop_Rapeseed_Mustard': crop_Rapeseed_Mustard,
        'crop_Rice': crop_Rice,
        'crop_Safflower': crop_Safflower,
        'crop_Samai': crop_Samai,
        'crop_Sapota': crop_Sapota,
        'crop_Sesamum': crop_Sesamum,
        'crop_Small_millets': crop_Small_millets,
        'crop_Soyabean': crop_Soyabean,
        'crop_Sugarcane': crop_Sugarcane,
        'crop_Sunflower': crop_Sunflower,
        'crop_Sweet_potato': crop_Sweet_potato,
        'crop_Tapioca': crop_Tapioca,
        'crop_Tobacco': crop_Tobacco,
        'crop_Tomato': crop_Tomato,
        'crop_Turmeric': crop_Turmeric,
        'crop_Urad': crop_Urad,
        'crop_Varagu': crop_Varagu,
        'crop_Wheat': crop_Wheat,
        'crop_other_fibres': crop_other_fibres,
        'crop_other_misc_pulses': crop_other_misc_pulses,
        'crop_other_oilseeds': crop_other_oilseeds
    }

    features = pd.DataFrame(data,index=[0])
                   
    expected_features = ['Area', 'Producton','Season_Kharif', 'Season_Whole_Year', 'Season_Rabi','crop_Arhar_Tur', 'crop_Bajra', 'crop_Banana',
       'crop_Beans_Mutter_Vegetable', 'crop_Bhindi', 'crop_Black_pepper','crop_Bottle_Gourd', 'crop_Brinjal', 'crop_Cabbage', 'crop_Cashewnut',
       'crop_Castor_seed', 'crop_Citrus_Fruit', 'crop_Coconut','crop_Coriander', 'crop_Cotton_lint', 'crop_Cowpea_Lobia','crop_Cucumber', 'crop_Dry_chillies', 'crop_Dry_ginger', 'crop_Garlic',
       'crop_Ginger', 'crop_Gram', 'crop_Grapes', 'crop_Groundnut','crop_Horse_gram', 'crop_Jowar', 'crop_Korra', 'crop_Lemon','crop_Linseed', 'crop_Maize', 'crop_Mango', 'crop_Masoor', 'crop_Mesta',
       'crop_Moong_Green_Gram','crop_Niger_seed', 'crop_Oilseeds_total','crop_Onion', 'crop_Orange', 'crop_Other_Rabi_pulses','crop_Other_Fresh_Fruits', 'crop_Other_Kharif_pulses',
       'crop_Other_Vegetables', 'crop_Papaya', 'crop_Peas_vegetable','crop_Pome_Fruit', 'crop_Pome_Granet', 'crop_Potato','crop_Pulses_total', 'crop_Ragi', 'crop_Rapeseed_Mustard', 'crop_Rice',
       'crop_Safflower', 'crop_Samai', 'crop_Sapota', 'crop_Sesamum','crop_Small_millets', 'crop_Soyabean', 'crop_Sugarcane','crop_Sunflower', 'crop_Sweet_potato', 'crop_Tapioca', 'crop_Tobacco',
       'crop_Tomato', 'crop_Turmeric', 'crop_Urad', 'crop_Varagu','crop_Wheat', 'crop_other_fibres', 'crop_other_misc_pulses','crop_other_oilseeds']

#print(list(features.columns))
#assert list(features.columns) == expected_features

    if st.button('Predict'):
        prediction = model1.predict(features)
        st.write(f"Your yield is {prediction}")
       

#st.write(f"{prediction}")