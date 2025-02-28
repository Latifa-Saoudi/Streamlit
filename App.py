'''import streamlit as st 
st.title("this is a title")
st.write("hello gomycoders")

st.header("hello programmers")
st.subheader("Deploy your app")
st.success("Success")
st.info("Information")
st.warning("Warning")
st.error("Error")
exp = ZeroDivisionError("Trying to divide by Zero" )
st.exception(exp)
from PIL import Image
img = Image.open("D:\Streamlit\Streamlit.jpg")
st.image(img,width=200)
if st.checkbox("Show/Hide"):
	# affiche le texte si la case à cocher renvoie la valeur True

     st.text("Showing the widget")

     # le premier argument est le titre du bouton radio
# le deuxième argument est l'option du bouton radio

status = st.radio("Select Gender: ", ('Male', 'Female'))

# déclaration conditionnelle à imprimer
# mâle si le mâle est sélectionné sinon imprimer female
# afficher le résultat à l'aide de la fonction de réussite

if (status == 'Male'):

	st.success("Male")

else:

	st.success("Female")
# Le premier argument est le titre de la boîte de sélection.
# le deuxième argument prend les options :

hobby = st.selectbox("Hobbies: ",['Dancing', 'Reading', 'Sports'])
# imprimer le hobby sélectionné :
st.write("Your hobby is: ", hobby)
#boite multi_selection
hobbies = st.multiselect("Hobbies: ",['Dancing', 'Reading', 'Sports'])
#nombre de selection
st.write("You selected", len(hobbies), 'hobbies')
#button with no reason
st.button("Submit")
#Bouton a condition
if(st.button("About")):
	st.text("Welcome To Gomycode!!!")
#texte
name = st.text_input("Enter Your name", "Type Here ...")
#texte with condition
if(st.button('Submit1')):
	result = name.title()
	st.success(result)
# le premier argument prend le titre du slider
# le deuxième argument prend le début du slider
# le dernier argument prend le numéro de fin
level = st.slider("Select the level", 1, 5)
# imprimer le niveau
# format() est utilisé pour imprimer la valeur d'une variable à une position spécifique
st.text('Selected: {}'.format(level))'''

# import the streamlit library 

import streamlit as st 

# give a title to our app 

st.title('Welcome to BMI Calculator') 

# TAKE WEIGHT INPUT in kgs 

weight = st.number_input("Enter your weight (in kgs)") 

# TAKE HEIGHT INPUT 

# radio button to choose height format status = st.radio('Select your height format: ', ('cms', 'meters', 'feet'))
status= st.radio('select your height format:',('cms','meters','feet'))
if(status == 'cms'):
    height = st.number_input('Centimeters')
    try:
        bmi = weight / ((height/100)**2)
    except:
        st.text("Enter some value of height")

elif(status == 'meters'):
    # take height input in meters
    height = st.number_input('Meters')
    try:
        bmi = weight / (height ** 2)
    except:
        st.text("Enter some value of height")
else:
    height = st.number_input('Feet')
    # 1 meter = 3.28
    try:
        bmi = weight / (((height/3.28))**2)
    except:
        st.text("Enter some value of height")
if(st.button('Calculate BMI')):
    # print the BMI INDEX
    st.text("Your BMI Index is {}.".format(bmi))
    # give the interpretation of BMI index
    if(bmi < 16):
        st.error("You are Extremely Underweight")
    elif(bmi >= 16 and bmi < 18.5):
        st.warning("You are Underweight")
    elif(bmi >= 18.5 and bmi < 25):
        st.success("Healthy")
    elif(bmi >= 25 and bmi < 30):
        st.warning("Overweight")
    elif(bmi >= 30):
        st.error("Extremely Overweight")