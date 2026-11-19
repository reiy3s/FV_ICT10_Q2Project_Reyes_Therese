from pyscript import display, document





#Drill 2 main.py code

g7 = {"Mendoza, Cheree", "Ramos, Elise"}
g8 = {"Schwab, Princess", "Mendoza, Orange"}
g9 = {"Adlawan, Nico", "Musni, Julienne"}
g10 = {"Ledres, Zoey", "Reyes, Therese"}

members = list(g7 | g8 | g9 | g10) #combination magic

def show_members(): #show CURRENT members
    members_list = document.getElementById("members-list")
    members_list.innerHTML = ""
    for member in sorted(members):
        item = document.createElement("li")
        item.textContent = member
        members_list.appendChild(item)

show_members()

def add_member(e):
    name1 = document.getElementById("fn").value #get fn
    name2 = document.getElementById("ln").value #get ln

    full_name = f"{name2.strip()}, {name1.strip()}" #combination magic pt 2
    members.append(full_name) #add
    members.sort() #sort
    show_members() #show new list





#Skills Test main.py code

#Element Name, info, info, info
elements = {"HYDROGEN": ("H", "Hydrogen", 1, 1.00),
            "HELIUM": ("He", "Helium", 2, 4.00),
            "CARBON": ("C", "Carbon", 6, 12.01),
            "NITROGEN": ("N", "Nitrogen", 7, 14.01),
            "OXYGEN": ("O", "Oxygen", 8, 16.00),
            "FLUORINE": ("F", "Fluorine", 9, 19.00),
            "SULFUR": ("S", "Sulfur", 16, 32.07),
            "CHLORINE": ("Cl", "Chlorine", 17, 35.45),
            "ARGON": ("Ar", "Argon", 18, 39.95),
            "SELENIUM": ("Se", "Selenium", 34, 78.96),
            "BROMINE": ("Br", "Bromine", 35, 79.90),
            "KYRPTON": ("Kr", "Krypton", 36, 83.80),
            "IODINE": ("I", "Iodine", 53, 126.90),
            "XENON": ("Xe", "Xenon", 54, 131.29),
            "ASTATINE": ("At", "Astatine", 85, 210.00),
            "RANDON": ("Rn", "Radon", 86, 222.00),
            "TENNESSINE": ("Ts", "Tenessine", 118, 294.00),
            "OGANESSON": ("Og", "Oganesson", 118, 294.00)
            }

# Function to search for an element
def search_element(e):
    # get input value
    element1 = document.getElementById("element1").value #get info from dict
    result = elements.get(element1, ("Element not found", "N/A", "N/A", "N/A")) #fall back if not found
    #display the result
    document.getElementById("code").innerText = result[0]
    document.getElementById("name").innerText = result[1]
    document.getElementById("atomic_#").innerText = result[2]
    document.getElementById("atomic_m").innerText = result[3]





#SW1 main.py code

from pyscript import display, document #link to index...?

members = ["Zoey Ledres", "Cheree Mendoza", "Princess Schwab", "Therese Reyes", "Elise Ramos"] #im pretty sure this is the ganglang thats allowed

def get_IN(e):
    name1 = document.getElementById("fn").value
    name2 = document.getElementById("ln").value

    full_name = f"{name1.strip()} {name2.strip()}" #combines name
    is_member = full_name in members #true or false

    if is_member:
        display("Welcome to the Rainbow Catering Club!", target="output") #displays when a member
    else:
        display("Oops! Are you sure you're part of this club?", target="output") #displays when not a member (?)