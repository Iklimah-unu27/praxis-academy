assert sum([1, 2, 3]) == 6, "Should be 6"
#tidal ada output karena jawabannya sudah benar yaitu 6

print("------------------------------------------------------------------------")

#assert sum([1, 2, 3]) == 8, "Should be 6"
# assert sum([1, 2, 3]) == 8, "Should be 6"
# AssertionError: Should be 6
# outputnya keluar tulisan eror karena jawaban tidak sesuai atau tidak benar

print("------------------------------------------------------------------------")
def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

if __name__ == "__main__":
    test_sum()
    print("Everything passed")



#https://realpython.com/python-testing/