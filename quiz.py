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