# Biology Quiz Program - 25 Questions
# Prepared By: Birhan
# Intro
name = input("Enter your name: ")
print(f"\nWelcome, {name}! ")
print("This is your 25-question Biology quiz. Each question carries equal marks.\n")

# Questions, options, and correct answers
questions = [
    ("The basic unit of life is:", ["Tissue", "Cell", "Organ", "Molecule"], "b"),
    ("Which part of the cell controls activities?", ["Cytoplasm", "Nucleus", "Cell wall", "Vacuole"], "b"),
    ("Photosynthesis occurs in:", ["Mitochondria", "Chloroplast", "Ribosome", "Nucleus"], "b"),
    ("Which molecule carries genetic information?", ["RNA", "DNA", "Protein", "Lipid"], "b"),
    ("The largest organ in the human body is:", ["Heart", "Skin", "Liver", "Lung"], "b"),
    ("Which blood cells fight infections?", ["Red blood cells", "White blood cells", "Platelets", "Plasma"], "b"),
    ("The functional unit of the kidney is:", ["Alveolus", "Nephron", "Villus", "Axon"], "b"),
    ("The powerhouse of the cell is:", ["Ribosome", "Mitochondrion", "Lysosome", "Golgi body"], "b"),
    ("Which vitamin is produced in the skin by sunlight?", ["Vitamin A", "Vitamin D", "Vitamin C", "Vitamin K"], "b"),
    ("Which gas is absorbed during photosynthesis?", ["Oxygen", "Carbon dioxide", "Nitrogen", "Hydrogen"], "b"),
    ("The smallest blood vessels are:", ["Arteries", "Veins", "Capillaries", "Venules"], "c"),
    ("The study of fungi is called:", ["Botany", "Mycology", "Zoology", "Bacteriology"], "b"),
    ("Which organ stores bile?", ["Liver", "Gallbladder", "Pancreas", "Stomach"], "b"),
    ("Red color of blood is due to:", ["Chlorophyll", "Hemoglobin", "Plasma", "Myosin"], "b"),
    ("The structural unit of proteins is:", ["Fatty acids", "Amino acids", "Nucleotides", "Glucose"], "b"),
    ("Which organ produces insulin?", ["Liver", "Pancreas", "Kidney", "Spleen"], "b"),
    ("Which part of the brain controls balance?", ["Cerebrum", "Cerebellum", "Medulla", "Pons"], "b"),
    ("The lens of the eye focuses light on the:", ["Cornea", "Retina", "Iris", "Pupil"], "b"),
    ("Which blood group is a universal donor?", ["AB+", "O–", "O+", "AB–"], "b"),
    ("In humans, fertilization occurs in the:", ["Uterus", "Fallopian tube", "Ovary", "Vagina"], "b"),
    ("The green pigment in plants is:", ["Xanthophyll", "Chlorophyll", "Carotene", "Anthocyanin"], "b"),
    ("Which part of the ear helps in balance?", ["Cochlea", "Semicircular canals", "Eardrum", "Ossicles"], "b"),
    ("Malaria is caused by:", ["Virus", "Bacteria", "Protozoa", "Fungus"], "c"),
    ("Which kingdom includes mushrooms?", ["Plantae", "Fungi", "Protista", "Animalia"], "b"),
    ("Which is the longest bone in the human body?", ["Humerus", "Femur", "Tibia", "Fibula"], "b")
]

# Quiz loop
score = 0
for i, (question, options, correct) in enumerate(questions, start=1):
    print(f"\n{i}. {question}")
    for opt_index, option in zip("abcd", options):
        print(f"   {opt_index}) {option}")
    answer = input("Your answer (a/b/c/d): ").lower().strip()

    if answer == correct:
        score += 1
        print("✅ Correct!")
    else:
        print(f"❌ Wrong! Correct answer is '{correct}) {options[ord(correct)-97]}'")

# Final score
percentage = (score / len(questions)) * 100
print(f"\n{name}, your final score is: {score}/{len(questions)} ({percentage:.2f}%)")

if percentage == 100:
    print("🌟 Outstanding! You got a perfect score! 🌟")
elif percentage >= 80:
    print("💪 Great job! Keep it up!")
elif percentage >= 50:
    print("🙂 Not bad, but you can do better.")
else:
    print("📚 Keep studying, you'll improve!")


#Prepared By: Selamawit
#==============
 
# * Chemistry Quiz Program - 25 Questions *

# * Intro section: Get user's name and welcome them *
name = input("Enter your name: ")
print(f"\nWelcome, {name}! 😊")
print("This is your 25-question Chemistry quiz. Each question carries equal marks.\n")

# * Questions, options, and correct answers stored as a list of tuples *
# * Each tuple: (question text, list of options, correct answer as letter) *
questions = [
    ("What is the chemical symbol for water?", ["H2O", "O2", "CO2", "NaCl"], "a"),
    ("Atomic number represents:", ["Number of neutrons", "Number of protons", "Number of electrons", "Mass number"], "b"),
    ("Which gas is released when acids react with metals?", ["Oxygen", "Hydrogen", "Carbon dioxide", "Nitrogen"], "b"),
    ("The pH of a neutral solution is:", ["0", "7", "14", "1"], "b"),
    ("Which element is a noble gas?", ["Oxygen", "Nitrogen", "Neon", "Chlorine"], "c"),
    ("What is the chemical formula of table salt?", ["KCl", "NaCl", "CaCl2", "MgCl2"], "b"),
    ("Which is the lightest element?", ["Hydrogen", "Helium", "Carbon", "Oxygen"], "a"),
    ("Which type of bond involves sharing of electrons?", ["Ionic bond", "Covalent bond", "Metallic bond", "Hydrogen bond"], "b"),
    ("What is the main gas in the air we breathe?", ["Oxygen", "Nitrogen", "Carbon dioxide", "Hydrogen"], "b"),
    ("Which substance is acidic?", ["Lemon juice", "Soap", "Baking soda", "Milk of magnesia"], "a"),
    ("What is the chemical symbol for gold?", ["Ag", "Au", "Gd", "Go"], "b"),
    ("Which of these is an alkaline substance?", ["Vinegar", "Ammonia", "Lemon juice", "Sulfuric acid"], "b"),
    ("What is the mass number of an element?", ["Protons + Neutrons", "Protons + Electrons", "Neutrons only", "Electrons only"], "a"),
    ("Which element is required for hemoglobin?", ["Calcium", "Iron", "Magnesium", "Potassium"], "b"),
    ("Which gas causes global warming?", ["Nitrogen", "Oxygen", "Carbon dioxide", "Helium"], "c"),
    ("Which metal is liquid at room temperature?", ["Mercury", "Lead", "Aluminium", "Iron"], "a"),
    ("Avogadro’s number represents:", ["Number of molecules in 1 mole", "Atomic number", "Number of atoms in 1 g", "Number of ions in solution"], "a"),
    ("Which type of reaction absorbs heat?", ["Exothermic", "Endothermic", "Displacement", "Combustion"], "b"),
    ("What is the chemical formula of ammonia?", ["NH3", "H2O", "CH4", "HCl"], "a"),
    ("Which acid is present in vinegar?", ["Hydrochloric acid", "Sulfuric acid", "Acetic acid", "Nitric acid"], "c"),
    ("Which element has the highest electronegativity?", ["Oxygen", "Fluorine", "Chlorine", "Hydrogen"], "b"),
    ("Which type of bond is found in NaCl?", ["Covalent", "Ionic", "Metallic", "Hydrogen"], "b"),
    ("What is the main component of natural gas?", ["Methane", "Ethane", "Propane", "Butane"], "a"),
    ("Which is a transition metal?", ["Sodium", "Copper", "Potassium", "Calcium"], "b"),
    ("Which gas is produced in photosynthesis?", ["Oxygen", "Carbon dioxide", "Nitrogen", "Hydrogen"], "a")
]

# * Initialize the score variable *
score = 0

# * Loop through each question and ask the user *
for i, (question, options, correct) in enumerate(questions, start=1):
    print(f"\n{i}. {question}")  # * Display question number and text *
    for opt_index, option in zip("abcd", options):
        print(f"   {opt_index}) {option}")  # * Display options a-d *
    answer = input("Your answer (a/b/c/d): ").lower().strip()  # * Get user's answer and normalize it *

    # * Check if the answer is correct *
    if answer == correct:
        score += 1
        print("✅ Correct!")  # * Positive feedback *
    else:
        print(f"❌ Wrong! Correct answer is '{correct}) {options[ord(correct)-97]}'")  # * Show correct answer *

# * Calculate final score as percentage *
percentage = (score / len(questions)) * 100

# * Display final result *
print(f"\n{name}, your final score is: {score}/{len(questions)} ({percentage:.2f}%)")




# developed by mintesnot

# Multiple Choice Physics Quiz
print(" Welcome to the Physics Quiz! \n")

questions = [
    ("What is the speed of light in vacuum?", 
     {"A": "3 × 10^8 m/s", "B": "3 × 10^6 m/s", "C": "3 × 10^5 m/s", "D": "3 × 10^4 m/s"}, "A"),
    
    ("Who is known as the father of modern physics?", 
     {"A": "Newton", "B": "Einstein", "C": "Galileo", "D": "Bohr"}, "B"),
    
    ("What is the SI unit of force?", 
     {"A": "Joule", "B": "Pascal", "C": "Newton", "D": "Watt"}, "C"),
    
    ("Formula for kinetic energy?", 
     {"A": "mv", "B": "0.5mv^2", "C": "mgh", "D": "F×d"}, "B"),
    
    ("Acceleration due to gravity on Earth?", 
     {"A": "8.9 m/s^2", "B": "9.8 m/s^2", "C": "10 m/s^2", "D": "9.2 m/s^2"}, "B"),
    
    ("Which particle has a negative charge?", 
     {"A": "Proton", "B": "Neutron", "C": "Electron", "D": "Photon"}, "C"),
    
    ("SI unit of work?", 
     {"A": "Joule", "B": "Newton", "C": "Watt", "D": "Tesla"}, "A"),
    
    ("Law of action and reaction?", 
     {"A": "Newton's 1st", "B": "Newton's 2nd", "C": "Newton's 3rd", "D": "Hooke's Law"}, "C"),
    
    ("Unit of power?", 
     {"A": "Pascal", "B": "Joule", "C": "Watt", "D": "Volt"}, "C"),
    
    ("Which wave does not need a medium?", 
     {"A": "Sound", "B": "Water", "C": "Seismic", "D": "Electromagnetic"}, "D"),
    
    ("Boiling point of water (°C)?", 
     {"A": "0", "B": "50", "C": "100", "D": "200"}, "C"),
    
    ("Law relating current, voltage, and resistance?", 
     {"A": "Coulomb’s law", "B": "Ohm’s law", "C": "Faraday’s law", "D": "Newton’s law"}, "B"),
    
    ("SI unit of pressure?", 
     {"A": "Joule", "B": "Pascal", "C": "Watt", "D": "Newton"}, "B"),
    
    ("Device used to measure electric current?", 
     {"A": "Voltmeter", "B": "Barometer", "C": "Ammeter", "D": "Galvanometer"}, "C"),
    
    ("SI unit of frequency?", 
     {"A": "Hertz", "B": "Newton", "C": "Tesla", "D": "Joule"}, "A"),
    
    ("Who discovered gravitation?", 
     {"A": "Newton", "B": "Einstein", "C": "Tesla", "D": "Faraday"}, "A"),
    
    ("Formula for momentum?", 
     {"A": "KE=0.5mv^2", "B": "p=mv", "C": "F=ma", "D": "V=IR"}, "B"),
    
    ("Escape velocity of Earth?", 
     {"A": "9.8 km/s", "B": "11.2 km/s", "C": "8.9 km/s", "D": "12.5 km/s"}, "B"),
    
    ("Gas used in bulbs?", 
     {"A": "Oxygen", "B": "Nitrogen", "C": "Argon", "D": "Carbon dioxide"}, "C"),
    
    ("First law of thermodynamics is about?", 
     {"A": "Entropy", "B": "Energy conservation", "C": "Force", "D": "Work"}, "B"),
    
    ("Speed of sound in air?", 
     {"A": "343 m/s", "B": "300 m/s", "C": "500 m/s", "D": "1000 m/s"}, "A"),
    
    ("Charge of a proton?", 
     {"A": "Positive", "B": "Negative", "C": "Neutral", "D": "None"}, "A"),
    
    ("SI unit of electric charge?", 
     {"A": "Coulomb", "B": "Volt", "C": "Ohm", "D": "Tesla"}, "A"),
    
    ("Lens used in a magnifying glass?", 
     {"A": "Concave", "B": "Convex", "C": "Plane", "D": "Cylindrical"}, "B"),
    
    ("Which scientist proposed E=mc^2?", 
     {"A": "Newton", "B": "Einstein", "C": "Bohr", "D": "Galileo"}, "B")
]

score = 0

for i, (q, opts, correct) in enumerate(questions, 1):
    print(f"\nQ{i}: {q}")
    for key, value in opts.items():
        print(f"  {key}. {value}")
    ans = input("Your answer (A/B/C/D): ").strip().upper()
    
    if ans == correct:
        print(" Correct!")
        score += 1
    else:
        print(f" Incorrect! Correct answer: {correct}. {opts[correct]}")

print("\n Quiz Over!")
print(f"Your Score: {score}/{len(questions)}")
############## developed by julet
# * Mathematics Quiz Program - 25 Questions *
# * uesti: Get user's name and welcome them *
name = input("Enter your name: ")
print(f"\nWelcome, {name}! ")
print("This is yoon Mat")
# * Intro sectionur 25-qhematics quiz. Each question carries equal marks.\n")

# * Questions, options, and correct answers stored as a list of tuples *
# * Each tuple: (question text, list of options, correct answer as letter) *
questions = [
    ("What is 12 + 15?", ["25", "27", "28", "30"], "b"),
    ("What is 9 × 8?", ["72", "81", "64", "70"], "a"),
    ("What is the square of 11?", ["121", "111", "101", "131"], "a"),
    ("What is the square root of 144?", ["10", "11", "12", "13"], "c"),
    ("Solve for x: 2x + 5 = 15", ["4", "5", "6", "7"], "a"),
    ("The value of π (pi) is approximately:", ["3.14", "3.41", "3.24", "3.04"], "a"),
    ("What is 25 ÷ 5?", ["4", "5", "6", "7"], "b"),
    ("If angles of a triangle are 60°, 60°, and 60°, it is:", ["Scalene", "Isosceles", "Equilateral", "Right-angled"], "c"),
    ("The perimeter of a square with side 6 cm is:", ["24 cm", "36 cm", "18 cm", "30 cm"], "a"),
    ("The area of a rectangle with length 8 cm and width 5 cm is:", ["40 cm²", "45 cm²", "35 cm²", "50 cm²"], "a"),
    ("What is 15% of 200?", ["20", "25", "30", "35"], "c"),
    ("The sum of interior angles of a pentagon is:", ["360°", "540°", "720°", "450°"], "b"),
    ("If y = 3x + 2, find y when x = 4", ["10", "12", "14", "16"], "c"),
    ("Simplify: 5 + 2 × 3", ["21", "11", "16", "10"], "b"),
    ("The median of 3, 7, 9, 5, 11 is:", ["5", "7", "9", "6"], "b"),
    ("The mode of 2, 4, 4, 5, 6 is:", ["2", "4", "5", "6"], "b"),
    ("Convert 0.75 to a fraction:", ["3/4", "2/3", "1/2", "4/5"], "a"),
    ("If a = 5 and b = 3, find a² - b²", ["16", "25", "9", "8"], "a"),
    ("The radius of a circle with diameter 10 cm is:", ["10 cm", "5 cm", "7 cm", "8 cm"], "b"),
    ("The volume of a cube with side 4 cm is:", ["16 cm³", "64 cm³", "48 cm³", "32 cm³"], "b"),
    ("What is 7² + 24²?", ["625", "625", "625", "625"], "a"),  # Just ensuring correct option formatting
    ("If 2x = 10, then x = ?", ["4", "5", "6", "7"], "b"),
    ("The LCM of 6 and 8 is:", ["12", "24", "48", "18"], "b"),
    ("The HCF of 12 and 18 is:", ["4", "6", "8", "12"], "b"),
    ("If a triangle has sides 3 cm, 4 cm, 5 cm, its type is:", ["Equilateral", "Isosceles", "Right-angled", "Scalene"], "c")
]

# * Initialize the score variable *
score = 0

# * Loop through each question and ask the user *
for i, (question, options, correct) in enumerate(questions, start=1):
    print(f"\n{i}. {question}")  # * Display question number and text *
    for opt_index, option in zip("abcd", options):
        print(f"   {opt_index}) {option}")  # * Display options a-d *
    answer = input("Your answer (a/b/c/d): ").lower().strip()  # * Get user's answer and normalize it *

    # * Check if the answer is correct *
    if answer == correct:
        score += 1
        print("✅ Correct!")  # * Positive feedback *
    else:
        print(f"❌ Wrong! Correct answer is '{correct}) {options[ord(correct)-97]}'")  # * Show correct answer *

# * Calculate final score as percentage *
percentage = (score / len(questions)) * 100

# * Display final result *
print(f"\n{name}, your final score is: {score}/{len(questions)} ({percentage:.2f}%)")

# * Provide feedback based on performance *
if percentage == 100:
    print("🌟 Outstanding! You got a perfect score! 🌟")
elif percentage >= 80:
    print("💪 Great job! Keep it up!")
elif percentage >= 50:
    print("🙂 Not bad, but you can do better.")
else:
    print("📚 Keep studying, you'll improve!")