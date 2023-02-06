def calculate_basic_statistics(data):
    nr_of_all_reviews = len(data.index)
    nr_of_all_clothes = len(set(data['Clothing ID']))
    return nr_of_all_reviews, nr_of_all_clothes




