from problem import Problem
import random

def backward_elimination(prob: Problem):
    while len(prob.features_remaining) > 1:
        #create new subsets
        prob.new_subsets("backward")

        # assign each subset an accuracy score 
        for subset in prob.set_accuracy_map:
            prob.set_accuracy_map[subset] = round(random.uniform(0,100),1)

        #Find the subset with highest accuracy score
        highest_score = 0
        best_subset = ()
        for subset in prob.set_accuracy_map:
            if prob.set_accuracy_map[subset] > highest_score:
                #print("found higher score\n")
                highest_score = prob.set_accuracy_map[subset]
                best_subset = subset
        
        #print("Subset to remove is: " + str(best_subset) + "\n")

        # Find feature to remove
        chosen_feature = 0
        for feature in prob.features_remaining:
            if not (feature in best_subset):
                chosen_feature = feature

        #print("Chosen feature to remove is: " + str(chosen_feature) + "\n")
        #Select feature
        prob.select_feature(best_subset, chosen_feature, "backward")
    
    #loop through chosen_features and find the subset with highest accuracy score
    final_highest_score = 0
    final_best_subset = ()
    for chosen in prob.chosen_sets:
        if(final_highest_score > chosen[1]):
            print("(Warning! Accuracy has decreased!)")
        if chosen[1] > final_highest_score:
            final_highest_score = chosen[1]
            final_best_subset = chosen[0]
    
    

    return (final_best_subset, final_highest_score)