from problem import Problem
import random


def forward_selection(problem: Problem) -> tuple[tuple, float]:
    # Create local alias
    accuracy_map = problem.set_accuracy_map
    while len(problem.features_remaining):
        # Generate new subset
        problem.new_subsets("Forward")

        # Set accuracies
        for subset in problem.set_accuracy_map:
            problem.set_accuracy_map[subset] = round(random.uniform(0, 100), 1)

        # Get the best subset and the chosen feature
        best_subset = max(accuracy_map, key=accuracy_map.get)
        for chosen_feature in problem.features_remaining:
            if chosen_feature in best_subset:
                break

        # Select the feature
        problem.select_feature(best_subset, chosen_feature, "Forward")

    # Get the best set and check if the accuracy decreased
    chosen_set = max(problem.chosen_sets, key=lambda chosen_set: chosen_set[1])
    if problem.chosen_sets.index(chosen_set) < len(problem.chosen_sets) - 1:
        print("(Warning, Accuracy has decreased!)")

    return chosen_set
