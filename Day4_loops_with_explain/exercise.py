weight=float(input("Enter your weight >\n"))
weight_in = input("K(kg) or L(lb)\n")

if weight_in == "L" or weight_in == "l":
    in_kg= weight * 0.4545
    print(f"your weight in kilogram (kg) is {in_kg}")
if weight_in == 'k' or weight_in =='K':
    in_pound= weight * 2.2046
    print(f"your weight in pounds (lbs) is {in_pound}")
    
print("\n")
print("Now I have another method to do this problem")
weight=float(input("Enter your weight >\n"))
weight_in = input("K(kg) or L(lb)\n")

if weight_in.upper()=='L':
    in_kg= weight * 0.4545
    print(f"your weight in kilogram (kg) is {in_kg}")
if weight_in.upper()=='K':
    in_pound= weight * 2.2046
    print(f"your weight in pounds (lbs) is {in_pound}")
    
