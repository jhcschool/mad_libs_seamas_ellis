# Seamas and Ellis worked together
# Here is our madlib template:

# Today I went to the zoo. I saw a(n) ___________(adjective) _____________(Noun) jumping up and down in its tree.
# He _____________(verb, past tense) __________(adverb) through the large tunnel that led to its _______(adjective)
# __________(noun). I got some peanuts and passed them through the cage to a gigantic gray _______(noun)
# towering above my head. Feeding that animal made me hungry. I went to get a __________(adjective) scoop
# of ice cream. It filled my stomach. Afterwards I had to __________(verb) __________ (adverb) to catch our bus.
# When I got home I __________(verb, past tense) my mom for a __________(adjective) day at the zoo.
contains_digits = False

verb_1 = ""
noun_1 = ""

vlist = [verb_1, noun_1]
slist = ["verb_1:", "noun_1:"]

verb_1 = input("Verb in the past tense: ")
noun_1 = input("Noun: ")



answer_1 = f"When I {verb_1} down my street, I saw a {noun_1} that reminded me I had to do my homework."
print(answer_1)