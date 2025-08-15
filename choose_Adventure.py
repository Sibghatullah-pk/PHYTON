name=input("type your name: ")
print(f"Hello {name}, welcome to the Adventure Game!")
print("In this game, you will make choices that will lead you on an adventure.")

print("You find yourself at a crossroads in a dense forest.")
print("Do you want to go left towards the mountains or right towards the river?")       

choice = input("Type 'left' or 'right': ").lower()

if choice == "left":
    print("You head towards the mountains and encounter a friendly bear.")
    print("The bear offers you a ride to the top of the mountain.")                     
    print("Do you accept the bear's offer? (yes/no)")       

    bear_choice = input().lower()
    if bear_choice == "yes":        

        print("You ride the bear to the top of the mountain and enjoy a beautiful view!")
        print("Congratulations, you completed the adventure!")  
    else:
        print("You politely decline the bear's offer and head back to the crossroads.")
        print("You can either go left again or try the right path this time.")  
        print("Do you want to go left again or right towards the river?")

        choice = input("Type 'left' or 'right': ").lower()  
        if choice == "right":
            print("You walk towards the river and find a boat.")
            print("Do you want to take the boat across the river? (yes/no)")
            boat_choice = input().lower()
            if boat_choice == "yes":
                print("You take the boat across the river and find a hidden treasure!")
                print("Congratulations, you completed the adventure!")
            else:
                print("You decide to stay on the riverbank and enjoy the scenery.")
                print("You can either go back to the crossroads or explore further along the river.")
                print("Do you want to go back to the crossroads or continue along the river? (crossroads/river)")
                next_choice = input().lower()
                if next_choice == "crossroads":
                    print("You return to the crossroads and can choose your path again.")
                else:
                    print("You continue along the river and discover a beautiful waterfall.")
                    print("You sit by the waterfall and enjoy the peaceful surroundings.")
                    print("Congratulations, you completed the adventure!")


        else:
            print("You walk back to the crossroads and can choose your path again.")
            print("Do you want to go left towards the mountains or right towards the river?")       
            choice = input("Type 'left' or 'right': ").lower()  
            if choice == "left":
                print("You head towards the mountains again and find a cave.")
                print("Do you want to explore the cave? (yes/no)")  
                cave_choice = input().lower()
                if cave_choice == "yes":
                    print("You explore the cave and find ancient drawings on the walls.")
                    print("You feel a sense of wonder and accomplishment.")

                    print("Congratulations, you completed the adventure!")
                else:
                    print("You decide not to enter the cave and head back to the crossroads.")
                    print("You can either go left again or try the right path this time.")
                    print("Do you want to go left again or right towards the river?")
                    choice = input("Type 'left' or 'right': ").lower()
                    if choice == "right":
                        print("You walk towards the river and find a boat.")
                        print("Do you want to take the boat across the river? (yes/no)")

                        boat_choice = input().lower()
                        if boat_choice == "yes":
                            print("You take the boat across the river and find a hidden treasure!")
                            print("Congratulations, you completed the adventure!")


                        else:
                            print("You decide to stay on the riverbank and enjoy the scenery.")
                            print("You can either go back to the crossroads or explore further along the river.")

                            print("Do you want to go back to the crossroads or continue along the river? (crossroads/river)")
                            next_choice = input().lower()

                            if next_choice == "crossroads":
                                print("You return to the crossroads and can choose your path again.")
                            else:

                                print("You continue along the river and discover a beautiful waterfall.")
                                print("You sit by the waterfall and enjoy the peaceful surroundings.")
                                print("Congratulations, you completed the adventure!")
            else:
                print("You walk back to the crossroads and can choose your path again.")
                print("Do you want to go left towards the mountains or right towards the river?")

                choice = input("Type 'left' or 'right': ").lower()

                if choice == "right":
                    print("You walk towards the river and find a boat.")
                    print("Do you want to take the boat across the river? (yes/no)")
                    boat_choice = input().lower()
                    if boat_choice == "yes":

                        print("You take the boat across the river and find a hidden treasure!")
                        print("Congratulations, you completed the adventure!")



                    else:
                        print("You decide to stay on the riverbank and enjoy the scenery.")

                        print("You can either go back to the crossroads or explore further along the river.")
                        print("Do you want to go back to the crossroads or continue along the river? (crossroads/river)")
                        next_choice = input().lower()

                        if next_choice == "crossroads":


                            print("You return to the crossroads and can choose your path again.")
                        else:
                            print("You continue along the river and discover a beautiful waterfall.")
                            print("You sit by the waterfall and enjoy the peaceful surroundings.")
                            print("Congratulations, you completed the adventure!")  
else:
    print("You chose to go right towards the river and find a boat.")
    print("Do you want to take the boat across the river? (yes/no)")
    boat_choice = input().lower()   
    if boat_choice == "yes":
        print("You take the boat across the river and find a hidden treasure!")

        print("Congratulations, you completed the adventure!")
    else:
        print("You decide to stay on the riverbank and enjoy the scenery.")
        print("You can either go back to the crossroads or explore further along the river.")
        print("Do you want to go back to the crossroads or continue along the river? (crossroads/river)")
        next_choice = input().lower()
        if next_choice == "crossroads":
            print("You return to the crossroads and can choose your path again.")
        else:
            print("You continue along the river and discover a beautiful waterfall.")
            print("You sit by the waterfall and enjoy the peaceful surroundings.")
            print("Congratulations, you completed the adventure!")
if choice == "left":
    print("You chose to go left towards the mountains and encounter a friendly bear.")
    print("The bear offers you a ride to the top of the mountain.")
    print("Do you accept the bear's offer? (yes/no)")
    bear_choice = input().lower()
    if bear_choice == "yes":
        
        print("You ride the bear to the top of the mountain and enjoy a beautiful view!")
        print("Congratulations, you completed the adventure!")
    else:
        print("You politely decline the bear's offer and head back to the crossroads.")
        print("You can either go left again or try the right path this time.")

        print("Do you want to go left again or right towards the river?")
        choice = input("Type 'left' or 'right': ").lower()
        if choice == "right":
            print("You walk towards the river and find a boat.")
            print("Do you want to take the boat across the river? (yes/no)")
            boat_choice = input().lower()
            if boat_choice == "yes":
                print("You take the boat across the river and find a hidden treasure!")
                print("Congratulations, you completed the adventure!")
            else:
                print("You decide to stay on the riverbank and enjoy the scenery.")
                print("You can either go back to the crossroads or explore further along the river.")
                print("Do you want to go back to the crossroads or continue along the river? (crossroads/river)")
                next_choice = input().lower()
                if next_choice == "crossroads":
                    print("You return to the crossroads and can choose your path again.")
                else:
                    print("You continue along the river and discover a beautiful waterfall.")
                    print("You sit by the waterfall and enjoy the peaceful surroundings.")
                    print("Congratulations, you completed the adventure!")
        else:   
            print("You walk back to the crossroads and can choose your path again.")
            print("Do you want to go left towards the mountains or right towards the river?")
            choice = input("Type 'left' or 'right': ").lower()

            if choice == "left":
                print("You head towards the mountains again and find a cave.")
                print("Do you want to explore the cave? (yes/no)")
                cave_choice = input().lower()
                if cave_choice == "yes":
                    print("You explore the cave and find ancient drawings on the walls.")
                    print("You feel a sense of wonder and accomplishment.")
                    print("Congratulations, you completed the adventure!")
                else:
                    print("you failed")
                    print("You decide not to enter the cave and head back to the crossroads.")


                