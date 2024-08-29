
def rss(a):
    agility, speed, strength = a
    if strength > 7:
        return "Javelin Throw"
    elif speed > 7:
        return "Football"
    elif agility > 7:
        return "Cricket"
    else:
        return "Chess"

def gdp(weight, height):
    
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        return f"Your BMI is {bmi} Eat more calories to gain weight."
    elif 18.5 <= bmi < 24.9:
        return f"Your BMI is {bmi} Maintain a balanced diet with moderate calorie intake."
    else:
        return f"Your BMI is {bmi} Reduce calorie intake and focus on a balanced diet to lose weight."


students = {
    "A": {
        "class": "10A",
        "height": 1.80,
        "weight": 75,
        "agility": 8,
        "speed": 6,
        "strength": 7
    },
    "B": {
        "class": "10B",
        "height": 1.65,
        "weight": 60,
        "agility": 5,
        "speed": 9,
        "strength": 5
    },
    "C": {
        "class": "10A",
        "height": 1.70,
        "weight": 65,
        "agility": 9,
        "speed": 6,
        "strength": 6
    },
    "D": {
        "class": "10C",
        "height": 1.85,
        "weight": 85,
        "agility": 6,
        "speed": 7,
        "strength": 9
    },
    "E": {
        "class": "10B",
        "height": 1.95,
        "weight": 55,
        "agility": 6,
        "speed": 4,
        "strength": 9
    },
    "F": {
        "class": "10A",
        "height": 1.95,
        "weight": 60,
        "agility": 9,
        "speed": 9,
        "strength": 9
    },
    "G": {
        "class": "10B",
        "height": 1.35,
        "weight": 90,
        "agility": 7,
        "speed": 8,
        "strength": 9
    }
}

print(students)

for stu, det in students.items():
    a = (det["agility"], det["speed"], det["strength"])
    rs = rss(a)
    dp = gdp(det["weight"], det["height"])
    
    print(f"Student: {stu}")
    print(f"Class: {det['class']}")
    print(f"Height: {det['height']} meters")
    print(f"Weight: {det['weight']} kg")
    print(f"Recommended Sport: {rs}")
    print(f"Diet Plan: {dp}")
    print("-" * 30)

