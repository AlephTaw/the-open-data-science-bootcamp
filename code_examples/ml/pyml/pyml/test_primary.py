import pytest
import sort2

@pytest.fixture(scope="module", params=[[[],[]], [[1,1,1,1],[1,1,1,1]], [[-1,-2,4,-3],[-3,-2,-1,4]], [[3,5,1],[1,3,5]]])
def arr_sample(request):
    yield request.param

def test_insertion_sort(arr_sample):
    assert sort2.insertion_sort(arr_sample[0]) == arr_sample[1]

def test_selection_sort(arr_sample):
    assert sort2.selection_sort(arr_sample[0]) == arr_sample[1]

def test_bubble_sort(arr_sample):
    assert sort2.selection_sort(arr_sample[0]) == arr_sample[1]

def test_merge_sort(arr_sample):
    print('hey')
    print(arr_sample[0])
    assert sort2.merge_sort(arr_sample[0]) == arr_sample[1]