#Write a function called convert_add 
#that takes a list of strings as an argument and converts 
#it to integers and sums the list. For 
#example [‘1’, ‘3’, ‘5’] should be
#converted to [1, 3, 5] and summed to 9
def convert_add(arr):
    new_list = [int(i) for i in arr]
    print(new_list)
arr = ["1", "3", "5"]
convert_add(arr)
