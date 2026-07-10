name = input("Passenger Name: ")
has_passport = input("Does the passenger have a valid passport? (y/n): ") == "y"
on_nofly_list = input("Is the passenger on the no-fly list? (y/n): ") == "y"

if not has_passport or on_nofly_list:
    if not has_passport:
        reason = "Invalid passport"
    else:
        reason = "Passenger is on the no-fly list"

    print("\n=============================================")
    print("       AIRPORT CHECK-IN SUMMARY")
    print("=============================================")
    print(f"Passenger     : {name}")
    print("---------------------------------------------")
    print("BOARDING      : DENIED")
    print(f"Reason        : {reason}")
    print("=============================================")
else:
    is_loyalty = input("Is loyalty member? (y/n): ") == "y"
    flight_duration = float(input("Flight duration in hours: "))
    num_bags = int(input("Number of bags: "))

    OVERWEIGHT_RATE = 12
    bag1_fee = 0.0
    bag2_fee = 0.0
    bag1_weight = 0.0
    bag2_weight = 0.0
    refused_entry = False

    if num_bags >= 3:
        refused_entry = True
    elif num_bags == 2:
        bag1_weight = float(input("Weight of Bag 1 (kg): "))
        bag2_weight = float(input("Weight of Bag 2 (kg): "))

        if bag1_weight > 23:
            bag1_fee = (bag1_weight - 23) * OVERWEIGHT_RATE

        if bag2_weight > 23:
            bag2_fee = 35.0 + ((bag2_weight - 23) * OVERWEIGHT_RATE)
        else:
            bag2_fee = 35.0
    elif num_bags == 1:
        bag1_weight = float(input("Weight of Bag 1 (kg): "))
        if bag1_weight > 23:
            bag1_fee = (bag1_weight - 23) * OVERWEIGHT_RATE

    total_baggage_fee = bag1_fee + bag2_fee

    if is_loyalty:
        if flight_duration > 6:
            upgrade_display = "Free (Business Class)"
        else:
            upgrade_display = "$79.00"
    else:
        upgrade_display = "No upgrade available"

    loyalty_display = "Yes" if is_loyalty else "No"

    print("\n=============================================")
    print("       AIRPORT CHECK-IN SUMMARY")
    print("=============================================")
    print(f"Passenger     : {name}")
    print(f"Loyalty Member: {loyalty_display}")
    print("---------------------------------------------")
    print("BAGGAGE")

    if refused_entry:
        print("Baggage Status: REFUSED (Maximum 2 bags allowed)")
        total_baggage_fee = 0.0
    else:
        if num_bags >= 1:
            bag1_msg = f"${bag1_fee:.2f} overage" if bag1_fee > 0 else "Free"
            print(f"Bag 1         : {bag1_weight:.1f}kg       → {bag1_msg}")
        if num_bags == 2:
            bag2_msg = f"${bag2_fee:.2f} (35 + {bag2_fee - 35:.0f} overage)" if bag2_fee > 35 else "$35.00"
            print(f"Bag 2         : {bag2_weight:.1f}kg       → {bag2_msg}")
        if num_bags == 0:
            print("No bags checked in.")

    print(f"Total Baggage : ${total_baggage_fee:.2f}")
    print("---------------------------------------------")
    print("SEAT")
    print(f"Flight        : {flight_duration:.1f} hrs")
    print(f"Upgrade       : {upgrade_display}")
    print("---------------------------------------------")
    print("BOARDING      : APPROVED")
    print("=============================================")