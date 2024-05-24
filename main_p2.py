from nn_classifier import nn_classifier
from leave_one_out_validator import leave_one_out_validator

# intro
print("Welcome to group 27's NN-Classifier and Leave One Out Validator.\n")

# list of dataset files
file_list = {
    1: "small-test-dataset-1.txt",
    2: "large-test-dataset-2.txt",
}

# print the file choices and ask for the file number
print("\nType the number of the dataset file you want to run.\n"
        "\tsmall-test-dataset-1\n"
        "\tlarge-test-dataset-2\n")
file_name = int(input())

# ask the user for a list of features separated by commas
input_str = input("Enter a list of features separated by commas: ")

# split the input string by commas and convert each element to an integer
features_list = [int(feature) for feature in input_str.split(',')]

# read the dataset file, and return a dictionary with the class labels as keys and the instance's features as values
def read_file(file_name, features_list):
    data_map = {}
    min_values = [float('inf') * len(features_list)]
    max_values = [float('-inf') * len(features_list)]

    # find the min and max values for each feature
    with open(file_name, 'r') as file:
        for line in file:
            # split the line by spaces and get the features
            instance = line.strip().split()
            for i, feature in enumerate(features_list):
                feature_value = float(instance[feature])
                min_values[i] = min(min_values[i], feature_value)
                max_values[i] = max(max_values[i], feature_value)
                
    # read and normalize the data
    with open(file_name, 'r') as file:
        instance_index = 0
        for line in file:
            # split the line by spaces and get the features
            instance = line.strip().split()
            # get the class label from the first element in the list
            class_label = int(instance[0])
            # create a tuple with the class label
            instance_tuple = (class_label,)
            # get the features from the rest of the elements in the list
            for i, feature in enumerate(features_list):
                feature_value = float(instance[feature])
                # normalize the feature value
                normalized_value = (feature_value - min_values[i]) / (max_values[i] - min_values[i])
                # add the normalized value to the tuple
                instance_tuple += (normalized_value,)
            # add the tuple to the data map
            data_map[instance_index] = instance_tuple
            # increment the instance index
            instance_index += 1
    # {instance_index: [class_lable, feature1, feature2, ...]}
    return data_map

# get the data map from the file
data_map = read_file(file_list[file_name])

# perform leave one out validation
result = leave_one_out_validator(data_map)
print("Accuracy: " + str(result) + "%" + "using features: " + str(features_list))


    # leave_one_out_validator(data_map):
        # correct_predictions = 0
        # for instance_index in data_map:
            # train_set = data_map.copy()
            # train_set.pop(instance_index)
            # test_instance = data_map[instance_index]
            # prediction = nn_classifier(test_instance, train_set)
            # if prediction == test_instance[0]:
                # correct_predictions += 1
        # return correct_predictions / len(data_map)

    # nn_classifier(test_instance, train_set):
        # min_distance = float('inf')
        # for train_instance in train_set:
            # distance = euclidean_distance(test_instance, train_instance)
            # if distance < min_distance:
                # min_distance = distance
                # prediction = train_instance[0]
        # return prediction
    
    # euclidean_distance(test_instance, train_instance):
        # distance = 0
        # for i in range(1, len(test_instance)):
            # distance += (test_instance[i] - train_instance[i]) ** 2
        # return distance ** 0.5