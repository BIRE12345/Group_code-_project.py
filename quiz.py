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
