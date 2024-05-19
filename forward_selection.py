from problem import Problem
import random


def get_best_feature(problem: Problem) -> None:
    # Create local aliases
    accuracy_map = problem.set_accuracy_map

    # Set accuracies
    for subset in problem.set_accuracy_map:
        problem.set_accuracy_map[subset] = round(random.uniform(0, 100), 1)

    # Get the best accuracy
    best_subset = max(accuracy_map, key=accuracy_map.get)
    for chosen_feature in problem.features_remaining:
        if chosen_feature in best_subset:
            break

    # Select the feature
    problem.select_feature(best_subset, chosen_feature, "Forward")


def forward_selection(problem: Problem) -> tuple[tuple, float]:
    # Generate new subset
    problem.new_subsets("Forward")

    # Create local aliases
    accuracy_map = problem.set_accuracy_map

    while len(accuracy_map.keys()) > 1:
        get_best_feature(problem)
        problem.new_subsets("Forward")

    get_best_feature(problem)

    return max(problem.chosen_sets, key=lambda chosen_set: chosen_set[1])


if __name__ == "__main__":
    print(f"The selected feature is {forward_selection(Problem(4))}")
