color = input("Enter color: ")

match color:
    case "red":
        print("STOP")
    case "yellow":
        print("SLOW DOWN")
    case "green":
        print("GO")
    case _:
        print("Invalid color")