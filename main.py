# Seamas and Ellis worked together
# We found the template online @: https://irp-cdn.multiscreensite.com/ec2b0ab8/files/uploaded/Mad%20Libs.pdf
# Here is our madlib template:

# Today I went to the zoo. I saw a(n) {adjective_1} {noun_1} jumping up and down in its tree.
# He {verb_past_tense_1} {adverb_1} through the large tunnel that led to its {adjective_2}
# {noun_2}. I got some peanuts and passed them through the cage to a gigantic gray {noun_3}
# towering above my head. Feeding that animal made me hungry. I went to get a {adjective_3} scoop
# of ice cream. It filled my stomach. Afterwards I had to {verb_1} {adverb_2} to catch our bus.
# When I got home I {verb_past_tense_2} my mom for a {adjective_4} day at the zoo.


# Attempt 1:

# Definitions of each word:

adjective_1 = input("Enter an adjective: ").lower()
noun_1 = input("Enter a noun: ").lower()
verb_past_tense_1 = input("Enter a past tense verb: ").lower()
adverb_1 = input("Enter an adverb: ").lower()
adjective_2 = input("Enter an adjective: ").lower()
noun_2 = input("Enter a noun: ").lower()
noun_3 = input("Enter a noun: ").lower()
adjective_3 = input("Enter an adjective: ").lower()
verb_1 = input("Enter a verb: ").lower()
adverb_2 = input("Enter an adverb: ").lower()
verb_past_tense_2 = input("Enter a past tense verb: ").lower()
adjective_4 = input("Enter an adjective: ").lower()
#The lower command was used for all inputted words since all of them do not require a capital letter.

# Edge Cases:
# line_1 = 'Today I went to the zoo. I saw a(n) {adjective_1} {noun_1} jumping up and down in its tree.'
# line_2 = 'He {verb_past_tense_1} {adverb_1} through the large tunnel that led to its {adjective_2}'
# line_3 = '{noun_2}. I got some peanuts and passed them through the cage to a gigantic gray {noun_3}'
# line_4 = 'towering above my head. Feeding that animal made me hungry. I went to get a {adjective_3} scoop'
# line_5 = 'of ice cream. It filled my stomach. Afterwards I had to {verb_1} {adverb_2} to catch our bus.'
# line_6 = 'When I got home I {verb_past_tense_2} my mom for a {adjective_4} day at the zoo.'


# Printed Statement:

print(f"Today I went to the zoo. I saw a(n) {adjective_1} {noun_1} jumping up and down in its tree.")
print(f"He {verb_past_tense_1} {adverb_1} through the large tunnel that led to its {adjective_2}")
print(f"{noun_2}. I got some peanuts and passed them through the cage to a gigantic gray {noun_3}")
print(f"towering above my head. Feeding that animal made me hungry. I went to get a {adjective_3} scoop")
print(f"of ice cream. It filled my stomach. Afterwards I had to {verb_1} {adverb_2} to catch our bus.")
print(f"When I got home I {verb_past_tense_2} my mom for a {adjective_4} day at the zoo.")

# Attempt 2:

