def pickItems():
    cost = 0
    totalCost = []
    # Stock
    SSD = [['1', '250 GB', 69.99], ['2', '500 GB', 93.99], ['3', '4 TB', 219.99]]
    HDD = [['1', '500 GB', 106.33], ['2', '1 TB', 134.33]]
    CPU = [['1', 'Intel Core i7-11700K', 499.99], ['2', 'AMD Ryzen 7 5800X', 312.99]]
    MOTHERBOARD = [['1', 'MSI B550-A Pro', 197.46], ['2', 'MSI Z490-A PRO', 262.30]]
    RAM = [['1', '16 GB', 82.99], ['2', '32 GB', 174.99]]
    GRAPHICS_CARD = [['1', 'MSI GeForce RTX 3060 12GB', 539.99]]
    PSU = [['1', 'Corsair RM750', 164.99]]
    CASE = [['1', 'Full Tower (black)', 149.99], ['2', 'Full Tower (red)', 149.99]]

    # Pre-built
    PREBUILTS = [['1', 'Legion Tower Gen 7 with RTX 3080 Ti', 3699.99], ['2', 'SkyTech Prism II Gaming PC', 2839.99], ['3', 'ASUS ROG Strix G10CE Gaming PC', 1099.99]]

    # Order
    print('Welcome to my PC shop!\n')
    orderType = ()
    while orderType not in ['1' or '2' or '3']:
        orderType = input("Would you like to build a custom PC (1), or purchase a pre-built PC (2), or would you like to checkout (3)?")

    # Custom PC
    if orderType == '1':
        print("\nGreat! Lets start building your PC!")

        # CPU selection
        print("\nFirst, let's pick a CPU.")
        print("1 : Intel Core i7-11700K, $499.99")
        print("2 : AMD Ryzen 7 5800X, $312.99")
        cpuType = ()
        while cpuType != '1' or '2':
            cpuType = input("Choose the number that corresponds with the part you want: ")
            if cpuType == '1':
                cost += 499.99
                break
            elif cpuType == '2':
                cost += 312.99
                break

        # Motherboard selection
        print("\nNext, let's pick a compatible motherboard.")
        motherboardType = ()
        if cpuType == '1':
            print("2 : MSI Z490-A PRO, $262.30")
            while motherboardType != '2':
                motherboardType = input("Choose the number that corresponds with the part you want: ")
                if motherboardType == '2':
                    cost += 262.30
                    break
        elif cpuType == '2':
            print(" 1 : MSI B550-A Pro, $197.46")
            while motherboardType != '1':
                motherboardType = input("Choose the number that corresponds with the part you want: ")
                if motherboardType == '1':
                    cost += 197.46
                    break

        #  RAM selection
        print("\nNext, let's pick your RAM.")
        print("1 : 16 GB, $82.99")
        print("2 : 32 GB, $174.99")
        ramType = ()
        while ramType != '1' or '2':
            ramType = input("Choose the number that corresponds with the part you want: ")
            if ramType == '1':
                cost += 82.99
                break
            elif ramType == '2':
                cost += 174.99
                break

        # PSU selection
        print("\nNext, let's pick your PSU.")
        print("1 : Corsair RM750, $164.99")
        psuType = ()
        while psuType != '1':
            psuType = input("Choose the number that corresponds with the part you want: ")
            if psuType == '1':
                cost += 164.99
                break

        # Case selection
        print("\nNext, let's pick your case.")
        print("1 : Full Tower (black), $149.99")
        print("2 : Full Tower (red), $149.99")
        caseType = ()
        while caseType != '1' or '2':
            caseType = input("Choose the number that corresponds with the part you want: ")
            cost += 149.99
            break

        # SSD selection
        print("\nNext, let's pick an SSD (optional, but you must have at least one SSD or HDD).")
        print("1 : 250 GB, $69.99")
        print("2 : 500 GB, $93.99")
        print("3 : 4 TB, $219.99")
        ssdType = ()
        while ssdType != '1' or '2' or '3' or 'X' or 'x':
            ssdType = input("Choose the number that corresponds with the part you want (or X to not get an SSD): ")
            if ssdType == '1':
                cost += 69.99
                break
            elif ssdType == '2':
                cost += 93.99
                break
            elif ssdType == '3':
                cost += 219.99
                break
            elif ssdType == 'X' or 'x':
                break

        # HDD type
        print("\nNext, let's pick an HDD (optional, but you must have at least one SSD or HDD).")
        print("1 : 500 GB, $106.33")
        print("2 : 1 TB, $134.33")
        hhdType = ()
        if ssdType == '1' or '2' or '3':
            while hhdType != '1' or '2' or 'X' or 'x':
                hhdType = input("Choose the number that corresponds with the part you want (or X to not get an HDD): ")
                if hhdType == '1':
                    cost += 106.33
                    break
                elif hhdType == '2':
                    cost += 134.33
                    break
                elif hhdType == 'X' or 'x':
                    break
        else:
            while hhdType != '1' or '2':
                hhdType = input("Choose the number that corresponds with the part you want (since ou did not get an SSD, you must get an HDD): ")
                if hhdType == '1':
                    cost += 106.33
                    break
                elif hhdType == '2':
                    cost += 134.33
                    break

        # Graphics card type
        print("\nFinally, let's pick your graphics card (or X not to get a graphics card).")
        print("1 : MSI GeForce RTX 3060 12GB, $539.99")
        graphicsCardType = ()
        while graphicsCardType != '1':
            graphicsCardType = input("Choose the number that corresponds with the part you want: ")
            if graphicsCardType == '1':
                cost += 539.99
                break
            elif graphicsCardType == 'X' or 'x':
                break

        # Total
        print("\nYou have selected all of the required parts! Your total for this PC is $%.2f" % cost)
        print()
        totalCost.append(cost)
        orderType = ()
        cost = 0

    # Pre-built PC
    elif orderType == '2':
        print("\nGreat! Let's pick a pre-built PC!")
        print("1 : Legion Tower Gen 7 with RTX 3080 Ti, $3699.99")
        print("2 : SkyTech Prism II Gaming PC, $2839.99")
        print("3 : ASUS ROG Strix G10CE Gaming PC, $1099.99")
        preBuilt = ()
        while preBuilt != '1' or '2' or '3':
            preBuilt = input("Choose the number that corresponds with the part you want: ")
            if preBuilt == '1':
                cost += 3699.99
                break
            elif preBuilt == '2':
                cost += 2839.99
                break
            elif preBuilt == '3':
                cost += 1099.99
                break
        print("\nYour total price for this prebuilt is $%.2f" % cost)
        print()
        totalCost.append(cost)
        orderType = ()
        cost = 0

    # Checkout
    elif orderType == '3':
        print(totalCost)
pickItems()
