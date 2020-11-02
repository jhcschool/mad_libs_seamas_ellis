# Seamas and Ellis worked together

# We found the template online @: https://irp-cdn.multiscreensite.com/ec2b0ab8/files/uploaded/Mad%20Libs.pdf
# Here is our 1st madlib template:

# Today I went to the zoo. I saw a(n) {adjective_1} {noun_1} jumping up and down in its tree.
# He {verb_past_tense_1} {adverb_1} through the large tunnel that led to its {adjective_2}
# {noun_2}. I got some peanuts and passed them through the cage to a gigantic gray {noun_3}
# towering above my head. Feeding that animal made me hungry. I went to get a {adjective_3} scoop
# of ice cream. It filled my stomach. Afterwards I had to {verb_1} {adverb_2} to catch our bus.
# When I got home I {verb_past_tense_2} my mom for a {adjective_4} day at the zoo.

# Here's the 2nd madlib:

# Found @: https://www.joyintheworks.com/wp-content/uploads/2015/04/Letter-from-Home-to-Camp-Picture.jpg
# Dear {proper_noun}, (1)
# How is camp? How is the {noun}? What is your counselor's name? How many {plural_noun} are in your cabin? (2)
# What does the {noun} taste like? Is it {adjective}? We are writing to let you know that things have been a little (2)
# {adjective} since you have left. The other night, we {past_tense_verb} a {noun}. We got up to {verb} what it was (4)
# and {exclamation}! You won't believe what we {verb_past_tense}. It was a {noun} {verb_ending_w/_ing} on your (4)
# {noun}! But don't worry, we {verb_past_tense} it right away and now everything is just {adjective} at home and all (3)
# set for your return.
# Love,
# Your family


# Attempt 1:

# Definitions of each word:

# adjective_1 = input("Enter an adjective: ").lower()
# noun_1 = input("Enter a noun: ").lower()
# verb_past_tense_1 = input("Enter a past tense verb: ").lower()
# adverb_1 = input("Enter an adverb: ").lower()
# adjective_2 = input("Enter an adjective: ").lower()
# noun_2 = input("Enter a noun: ").lower()
# noun_3 = input("Enter a noun: ").lower()
# adjective_3 = input("Enter an adjective: ").lower()
# verb_1 = input("Enter a verb: ").lower()
# adverb_2 = input("Enter an adverb: ").lower()
# verb_past_tense_2 = input("Enter a past tense verb: ").lower()
# adjective_4 = input("Enter an adjective: ").lower()
# The lower command was used for all inputted words since all of them do not require a capital letter.

# # Edge Cases:
# # line_1 = 'Today I went to the zoo. I saw a(n) {adjective_1} {noun_1} jumping up and down in its tree.'
# # line_2 = 'He {verb_past_tense_1} {adverb_1} through the large tunnel that led to its {adjective_2}'
# # line_3 = '{noun_2}. I got some peanuts and passed them through the cage to a gigantic gray {noun_3}'
# # line_4 = 'towering above my head. Feeding that animal made me hungry. I went to get a {adjective_3} scoop'
# # line_5 = 'of ice cream. It filled my stomach. Afterwards I had to {verb_1} {adverb_2} to catch our bus.'
# # line_6 = 'When I got home I {verb_past_tense_2} my mom for a {adjective_4} day at the zoo.'

# # Printed Statement:
#
# print("Here's the finishing result: ")
#
# print(f"Today I went to the zoo. I saw a(n) {adjective_1} {noun_1} jumping up and down in its tree.")
# print(f"He {verb_past_tense_1} {adverb_1} through the large tunnel that led to its {adjective_2}")
# print(f"{noun_2}. I got some peanuts and passed them through the cage to a gigantic gray {noun_3}")
# print(f"towering above my head. Feeding that animal made me hungry. I went to get a {adjective_3} scoop")
# print(f"of ice cream. It filled my stomach. Afterwards I had to {verb_1} {adverb_2} to catch our bus.")
# print(f"When I got home I {verb_past_tense_2} my mom for a {adjective_4} day at the zoo.")

# Attempt 2:

# After evaluation of the first attempt, we determined to take another approach in order to make the code better in various manners.
# We wanted to make our code work for various templates. The most efficient and DRY code would be the incorporation of lists and functions.

# Introduction of our game:
print("Welcome to the coolest Madlib out there.")
print("")
print("Presented by Seamas and Ellis")
print("")
print("There are two Madlibs available. Option one is about a zoo, and option two is about camp.")
print("")

# Now, we need the user to select which story they want.
# Similarly to what we did below, we looped the function in order to get a valid input from the user.
# Once the program knows which story was selected, then the proper list and function will be launched.


# We created a list for our templates
part_of_speech_list_zoo_story = ["adjective".lower().strip(), "noun".lower().strip(), "past tense verb".lower().strip(),
                                 "adverb".lower().strip(), "adjective".lower().strip(), "noun".lower().strip(),
                                 "noun".lower().strip(), "adjective".lower().strip(), "verb".lower().strip(),
                                 "adverb".lower().strip(), "past tense verb".lower().strip(),
                                 "adjective".lower().strip()]
part_of_speech_list_camp_story = ["proper noun".title().strip(), "noun".lower().strip(), "plural noun".lower().strip(),
                                  "adjective".lower().strip(), "past tense verb".lower().strip(), "adjective".lower().strip(),
                                  "past tense verb".lower().strip(), "noun".lower().strip(), "verb".lower().strip(),
                                  "exclamation".lower().strip(), "past tense verb".lower().strip(),
                                  "noun".lower().strip(), "verb ending in -ing".lower().strip(), "noun".lower().strip(),
                                  "past tense verb".lower().strip(), "adjective".lower().strip()]




# We put a .title on the proper noun since proper nouns need to have the first letter capitalized. None of the other variables in either madlib requires a title
# We .lowered everything else since nothing else needs capitalization.
# We also instated a .strip on everything since we wanted to remove the white spaces that may have been accidental.

# We will start with our first Madlib being the Zoo one.
def zoo_mad_lib():
    print(
        f"Today I went to the zoo. I saw a(n) {part_of_speech_list_zoo_story[0]} {part_of_speech_list_zoo_story[1]} jumping up and down in its tree.")
    print(
        f"He {part_of_speech_list_zoo_story[2]} {part_of_speech_list_zoo_story[3]} through the large tunnel that led to its {part_of_speech_list_zoo_story[4]}")
    print(
        f"{part_of_speech_list_zoo_story[5]}. I got some peanuts and passed them through the cage to a gigantic gray {part_of_speech_list_zoo_story[6]}")
    print(
        f"towering above my head. Feeding that animal made me hungry. I went to get a {part_of_speech_list_zoo_story[7]} scoop")
    print(
        f"of ice cream. It filled my stomach. Afterwards I had to {part_of_speech_list_zoo_story[8]} {part_of_speech_list_zoo_story[9]} to catch our bus.")
    print(
        f"When I got home I {part_of_speech_list_zoo_story[10]} my mom for a {part_of_speech_list_zoo_story[11]} day at the zoo.")


# Secondly, we will create the function for our second Madlib, the camping one.
def camp_mad_lib():
    print(f"Dear {part_of_speech_list_camp_story[0]},")
    print(
        f"How is camp? How is the {part_of_speech_list_camp_story[1]}? What is your counselor's name? How many {part_of_speech_list_camp_story[2]} are in your cabin?")
    print(
        f"What does the {part_of_speech_list_camp_story[3]} taste like? Is it {part_of_speech_list_camp_story[4]}? We are writing to let you know that things have been a little")
    print(
        f"{part_of_speech_list_camp_story[5]} since you have left. The other night, we {part_of_speech_list_camp_story[6]} a {part_of_speech_list_camp_story[7]}. We got up to {part_of_speech_list_camp_story[8]} what it was")
    print(
        f"and {part_of_speech_list_camp_story[9]}! You won't believe what we {part_of_speech_list_camp_story[10]}. It was a {part_of_speech_list_camp_story[11]} {part_of_speech_list_camp_story[12]} on your")
    print(
        f"{part_of_speech_list_camp_story[13]}! But don't worry, we {part_of_speech_list_camp_story[14]} it right away and now everything is just {part_of_speech_list_camp_story[15]} at home and all set for your return.")
    print("Love,")
    print("Your family")


# We need to make sure that our lists work properly. In order to do so, we must start our list at a = 0 and loop it so every user input increases one unit in the lists.
# Therefore, we created a definition (a function) to take the formatted parts of speech and change them into the user inputs.
def parts_of_speech_list_user_answers(list_of_parts_of_speech):
    a = 0
    # List starts at 0 like shown above in the lists.
    while a < len(list_of_parts_of_speech):
        # If the statement above is true, then 'a' or the list of values should be lower than the length or amount of the container or whole list of the parts of speech.
        word_inputted = input(f"{list_of_parts_of_speech[a]}?")
        if not word_inputted.lower().isalpha():
            print("Make sure you type an alphabetical value when prompted.")
        else:
            list_of_parts_of_speech[a] = word_inputted
            a += 1


madlib_selection = 0
# We need to start the story at option null or 0 then proceed let the user choose madlib "one" or "two"
while madlib_selection < 1:
    madlib_choice = input("Choose option 'one' or 'two': ")
    # Our first choice or the zoo madlib.
    if madlib_choice == "one":
        parts_of_speech_list_user_answers(part_of_speech_list_zoo_story)
        # Once the user inputs the values we need it to output or print.
        print(zoo_mad_lib())

    # Our second choice or the camp madlib.
    elif madlib_choice == "two":
        parts_of_speech_list_user_answers(part_of_speech_list_camp_story)
        # Once the user inputs the values we need it to output or print.
        print(camp_mad_lib())
    else:
        print("Choose option 'one' or 'two': ")