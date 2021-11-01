def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range((len(arr) - 1)):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


salam = [45, 980, 446, 74, 12, 87]
print(bubbleSort(salam))


class BubbleSort:
    def __init__(self, array):
        self.array = array
        self.length = len(array)

    def __str__(self):
        return " ".join([str(x) for x in self.array])

    def bubbleSortRecursive(self, n=None):
        if n is None:
            n = self.length

        # Base case
        if n == 1:
            return

        for i in range(n - 1):
            if self.array[i] > self.array[i + 1]:
                self.array[i], self.array[i + 1] = self.array[i + 1], self.array[i]

        self.bubbleSortRecursive(n - 1)


# Driver Code
def main():
    array = [64, 34, 25, 12, 22, 11, 90]

    # Creating object for class
    sort = BubbleSort(array)

    # Sorting array
    sort.bubbleSortRecursive()
    print("Sorted array :\n", sort)


if __name__ == "__main__":
    main()

