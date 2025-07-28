# Probability = (Number of favorable outcomes) / (Total outcomes)
red=2
total=5
p_red=red/total
print("P(red): ",p_red)

# AND Rule (both events happen): P(A and B) = P(A) × P(B) 
head=3
tail=2
total=5
p_head=head/total
p_tail=tail/total
and_prob=p_head*p_tail
print("AND Probability: ",and_prob)

# OR Rule (either event happens): P(A or B) = P(A) + P(B) - P(A and B)

or_prop=p_head+p_tail-and_prob
print("OR Probability: ",or_prop)

# Conditional Probability - Given that one event has occurred, what's the probability of another?: P(A | B) = P(A and B) / P(B)

cond_prop_head=and_prob/p_tail
print("P( Head | Tail ): ",cond_prop_head)


#Bayes' Theorem :

#             P(B|A) × P(A)
#   P(A|B) = ----------------
#                 P(B)

cond_prop_tail=(cond_prop_head*p_head)/p_tail

print("P( Tail | Head ): ",cond_prop_tail)