name = input("what's your name ?")

match name :
    case "harry"|"hermione"|"ron" :
        print("Gryffindor")

        #rather using this way we can make it concise
 #   case "hermione":
      #  print("Gryffindor")
   # case "ron":
      #  print("Gryffindor")

    case "draco":
        print("slytherin")
    case _:
        print("who")