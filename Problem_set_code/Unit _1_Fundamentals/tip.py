def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars_to_float(dollars) * percent_to_float(percent)
    print(f"Leave ${tip:.2f}")

#bloody broken init
def dollars_to_float(d):
    return float( d[1:] )

def percent_to_float(p):
    return float(p[:len(p)-1])/100



if __name__ == "__main__":
    print(dollars_to_float("$100.00"))
    main()
