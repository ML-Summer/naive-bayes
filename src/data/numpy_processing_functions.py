
def select_rows(arr, indices):
    """
    :param arr: np.array([
    [1, 0, 0, 1],
    [1, 1, 0, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 0]
    ])
    :param indices:[0,2]
    :return:np.array([
    [1, 0, 0, 1],
    [1, 0, 1, 0]
    ])
    """
    return arr[indices]


def make_labels_dict(labels):
    """
    :param labels: [0, 1, 1, 0, 1]
    :return: {0: [0, 3], 1: [1, 2, 4]}
    """
    label_dict = {}
    for index, label in enumerate(labels):
        if label not in label_dict:
            label_dict[label] = []
        label_dict[label].append(index)
    return label_dict
