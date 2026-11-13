
from pyscript import document

# Diseases and their information stored in a dictionary!! 
diseases = {
    "Dengue": [
        "Dengue virus",
        "Transmitted through the bite of an infected Aedes mosquito",
        "High fever, headache, muscle pain, nausea, and rash"
    ],

    "Malaria": [
        "Plasmodium parasite",
        "Transmitted through the bite of an infected Anopheles mosquito",
        "Fever, chills, sweating, headache, and fatigue"
    ],

    "Tuberculosis": [
        "Mycobacterium tuberculosis bacteria",
        "Spread through the air when an infected person coughs or sneezes",
        "Persistent cough, chest pain, fever, night sweats, and weight loss"
    ],

    "Influenza": [
        "Influenza virus",
        "Spread through respiratory droplets and contact with contaminated surfaces",
        "Fever, cough, sore throat, body aches, and fatigue"
    ],

    "Measles": [
        "Measles virus",
        "Spread through the air and respiratory droplets",
        "Fever, cough, runny nose, red eyes, and skin rash"
    ],

    "Chickenpox": [
        "Varicella-zoster virus",
        "Spread through respiratory particles and direct contact with blister fluid",
        "Itchy rash, fever, tiredness, and loss of appetite"
    ],

    "Cholera": [
        "Vibrio cholerae bacteria",
        "Spread through food or water contaminated with the bacteria",
        "Watery diarrhea, vomiting, and dehydration"
    ],

    "COVID-19": [
        "SARS-CoV-2 virus",
        "Spread mainly through respiratory particles",
        "Fever, cough, sore throat, fatigue, and loss of taste or smell"
    ],

    "Rabies": [
        "Rabies virus",
        "Usually transmitted through the bite or scratch of an infected animal",
        "Fever, headache, weakness, and neurological symptoms"
    ],

    "Polio": [
        "Poliovirus",
        "Spread mainly through the fecal-oral route, often through contaminated food or water",
        "Fever, fatigue, headache, and muscle weakness"
    ]
}
# LOWKEY WANT TO ADD MORE DISEASES BUT I DONT WANNA OVERLOAD THE DICTIONARY LOL and it will be so much work to add more diseases and their information.... I will just leave it as is for now BUT BUT if you need like a full disease one, I'll be able to finish it in a month or year lol since there are many rare diseases...

# Checks whether the entered disease exists in the dictionary
def disease_checker(e):

    document.getElementById('result').innerHTML = " "

    disease1 = document.getElementById('disease_name').value.strip().title()

    result = diseases.get(
        disease1,
        ("Disease not found", "--", "--")
    )

    document.getElementById('result').innerHTML = f"""
    <b> Disease Name: </b> {disease1}<br>
    <b> Causative Agent: </b> {result[0]}<br>
    <b> Mode of Transmission: </b> {result[1]}<br>
    <b> Common Symptoms: </b> {result[2]}
    """

