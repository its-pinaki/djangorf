l = 'banibihar2:214,248;saheed2:784;rajmahal2:879'
area=l.split(";")
for i in area:
    main=i.split(":")
    print(main)
    for m in main:
            area= m.split(",")
            print(area[0])
