import array

def bubble_sort(arr):
     for pass_nr in range(len(arr) - 1, 0, -1):
          for i in range(pass_nr):
               if arr[i] > arr[i+1]:
                    temp = arr[i]
                    arr[i] = arr[i + 1]
                    arr [i+1] = temp

music_Count = [12, 2, 3, 35, 37, 1, 5, 504, 30, 40]

bubble_sort(music_Count)

print (music_Count)