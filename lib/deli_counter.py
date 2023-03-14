katz_deli = []

def line(katz_deli):
    if (len(katz_deli) == 0):
        print("The line is currently empty.")
    else:
        line_start = "The line is currently:"
        for person in katz_deli:
            line_start += (f" {katz_deli.index(person) + 1}. {person}")
        print(line_start)

def take_a_number(katz_deli, customer):
    katz_deli.append(customer)
    print(f"Welcome, {customer}. You are number {katz_deli.index(customer) + 1} in line.")

def now_serving(katz_deli):
    if (len(katz_deli) == 0):
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {katz_deli.pop(0)}.")
