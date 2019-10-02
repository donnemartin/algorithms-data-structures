#Like QuickSort, Merge Sort is a Divide and Conquer algorithm.
#It divides input array in two halves, calls itself for the two halves and then merges the two sorted halves.
#The merge() function is used for merging two halves.

from nose.tools import assert_equal, assert_raises


class TestMergeSort(object):

    def test_merge_sort(self):
        merge_sort = MergeSort()

        print('None input')
        assert_raises(TypeError, merge_sort.sort, None)

        print('Empty input')
        assert_equal(merge_sort.sort([]), [])

        print('One element')
        assert_equal(merge_sort.sort([5]), [5])

        print('Two or more elements')
        data = [5, 1, 7, 2, 6, -3, 5, 7, -1]
        assert_equal(merge_sort.sort(data), sorted(data))

        print('Success: test_merge_sort')


def main():
    test = TestMergeSort()
    test.test_merge_sort()


if __name__ == '__main__':
    main()
