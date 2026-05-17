# print ("LINEAR SEARCHING")
# def linear_search(arr,target): #membuat fungsi bernamalinear_search
#     for i in range(len(arr)):#periksa jika nilainya cocok dgn target
#         if arr[i] == target:
#             return i #hentikan pencarian,kembalikan indeksnya
#     return -1 # jika di cek semua tidak ada kembalikan -1
# data = [12,7,25,9,15]
# angka_dicari = 9 #target
# #panggil fungsi dan simpan hasilnya
# hasil = linear_search(data, angka_dicari)
# if hasil != -1:
#     print("angka", angka_dicari, "ada di indeks ke:", hasil)
# else:
#     print("angka tidak ditemukan")


# #binary search
# print("BINARY SEARCHING") 
# def binary_search(arr,target):
#     left = 0   # batas kiri
#     right = len(arr) -1  # batas kanan
#     #semua batas kiri dan kanan blm bersilang
#     while left <= right:
#         #cari indeks tengah
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return mid # ketemu! kembalikan indeks
#         elif target < arr[mid]:
#             right = mid -1 #target lebih kecil,geser batas kanan 
#         else:
#             left  = mid + 1 #target lebih besar,geser batas kiri
#     return -1 #
# data = [10,20,30,40,50]
# angka_dicari = 40 
# hasil = binary_search(data, angka_dicari)
# if hasil != -1:
#     print("angka", angka_dicari, "ada di indeks ke:", hasil)
# else:
#     print("angka tidak ditemukan")


# print("naive string matching")
# text = "DATA STRUKTUR DATA"
# pattern = "DATA"

# for i in range(len(text) - len(pattern) + 1):

#     if text[i:i+len(pattern)] == pattern:
#         print("ketemu di index", i)


#MP [Knuth-Morris-Pratt]
# print("Knuth-Morris-Pratt (KMP)")
# def lps(pattern):
#     hasil = [0, 0, 1, 2, 3, 0]
#     return hasil

# pattern = "ABABCABAB"
# print("pattern:", pattern)
# print("LPS :", lps(pattern))

# print("BUBBLE SORT")
# def bubble_sort(arr):

#     n = len(arr)
#     for i in range(n):
#         for j in range (n-i-1):
#             if arr[j] > arr [j+1]:
#                 arr [j], arr[j+1] = arr[j+1], arr [j]
#     return arr
# # data yang akan diurutkan
# data = [5, 3, 8, 1, 2]
# #panggil fungsi
# hasil = bubble_sort(data)
# #tampilkan hasil
# print ("Data sebelum sorting:", [5, 3, 8, 1, 2])
# print("Data setelah sorting:", hasil)

# print("SELECTION SORT")
# def selection_sort(arr):
#     for i in range(len(arr)):
#         min_index = i
#         for j in range (i+1, len(arr)): 
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr [i]
#     return arr
# data = [5, 3, 2, 4]
# hasil = selection_sort(data) 
# print("Hasil sorting:", hasil)

# print("INSERTION SORT")
# def insertion_sort(arr):
#     for i in range (1, len(arr)):
#         key = arr [i]
#         j = i - 1
#         while j >= 0 and arr[j] > key:
#             arr[j+1] = arr[j]
#             j -= 1
#         arr[j+1]=key
#     return arr
# data = [5, 3, 4]
# hasil = insertion_sort(data)
# print("Hasil sorting:", hasil)


# print("merge sort")
# def merge_sort(arr):
#         if len(arr) > 1:
#             mid = len(arr) // 2
#             left = arr[:mid]
#             right = arr[mid:]
#             merge_sort(left)
#             merge_sort(right)

#             i = j = k = 0
#             while i < len(left) and j < len(right):
#                 if left[i] < right[j]:
#                     arr[k] = left[i]
#                     i += 1
#                 else:
#                     arr[k] = right[j]
#                     j += 1
#                 k += 1
#             while i < len(left):
#                 arr[k] = left [i]
#                 i += 1
#                 k += 1
#             while j < len(right):
#                 arr[k] = right[j]
#                 j += 1
#                 k += 1
#         return arr
# data = [8, 4, 2, 6]
# hasil = merge_sort(data)
# print("Hasil sorting:", hasil)

# print("QUICK SORT")
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = []
#     middle = []
#     right = []
#     for x in arr:
#         if x < pivot:
#             left.append(x)
#         elif x > pivot:
#             right.append(x)
#         else:
#             middle.append(x)
#     return quick_sort(left) + middle + quick_sort(right)
# data = [10, 7, 8, 9]
# hasil = quick_sort(data)
# print("Hasil sorting:", hasil)

#LATIHAN 1
# print("LATIHAN 1")
# def linear_search(arr, target):
#     for i in range (len(arr)):
#         if arr[i] == target:
#             return i
#     return -1
# data= [4, 7, 1, 9]
# angka_dicari = 9 #target
# hasil = linear_search(data, angka_dicari)
# if hasil !=-1:
#     print("angka", angka_dicari, "ada di indeks ke:", hasil)
# else:
#     print("angka tidak ditemukan")


#("LATIHAN 2")
# print("LATIHAN 2")
# def binary_search(arr, target):
#     left = 0                #batas kiri
#     right = len(arr) -1     #batas kanan

#     #selama batas kiri dan kanan belum bersilang
#     while left <= right:
#         #cari indeks tengah
#         mid = (left + right) // 2
#         if arr [mid] == target:
#             return mid 
#         elif target < arr [mid]:
#             right = mid - 1
#         else:
#             left = mid + 1
#     return -1
# data = [2, 4, 6, 8, 10]
# angka_dicari = 8   #target
# hasil = binary_search(data, angka_dicari)
# if hasil != -1:
#     print("angka ", angka_dicari, "ada di indeks ke-", hasil)
# else:
#     print("angka tidak ditemukan")

#LATIHAN 3
# print("LATIHAN 3 SORTING")
# print("BUBBLE SORT")
# def bubble_sort(arr):

#     n = len(arr)
#     for i in range(n):
#         for j in range (n-i-1):
#             if arr[j] > arr [j+1]:
#                 arr [j], arr[j+1] = arr[j+1], arr [j]
#     return arr
# # data yang akan diurutkan
# data = [9, 3, 5, 1]
# #panggil fungsi
# hasil = bubble_sort(data)
# #tampilkan hasil
# print ("Data sebelum sorting:", [9, 3, 5, 1])
# print("Data setelah sorting:", hasil)

# print("LATIHAN 3 SORTING")  
# print("SELECTION SORT")
# def selection_sort(arr):
#     for i in range(len(arr)):
#         min_index = i
#         for j in range (i+1, len(arr)): 
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr [i]
#     return arr
# data = [9, 3, 5, 1]
# hasil = selection_sort(data) 
# print("Hasil sorting:", hasil)


# print("LATIHAN 3 SORTING")
# print("INSERTION SORT")
# def insertion_sort(arr):
#     for i in range (1, len(arr)):
#         key = arr [i]
#         j = i - 1
#         while j >= 0 and arr[j] > key:
#             arr[j+1] = arr[j]
#             j -= 1
#         arr[j+1]=key
#     return arr
# data = [9, 3, 5, 1]
# hasil = insertion_sort(data)
# print("Hasil sorting:", hasil)


# print("LATIHAN 3 SORTING")
# print("MERGE SORT")
# def merge_sort(arr):
#         if len(arr) > 1:
#             mid = len(arr) // 2
#             left = arr[:mid]
#             right = arr[mid:]
#             merge_sort(left)
#             merge_sort(right)

#             i = j = k = 0
#             while i < len(left) and j < len(right):
#                 if left[i] < right[j]:
#                     arr[k] = left[i]
#                     i += 1
#                 else:
#                     arr[k] = right[j]
#                     j += 1
#                 k += 1
#             while i < len(left):
#                 arr[k] = left [i]
#                 i += 1
#                 k += 1
#             while j < len(right):
#                 arr[k] = right[j]
#                 j += 1
#                 k += 1
#         return arr
# data = [9, 3, 5, 1]
# hasil = merge_sort(data)
# print("Hasil sorting:", hasil)


# print("LATIHAN 3 SORTING")
# print("QUICK SORT")
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = []
#     middle = []
#     right = []
#     for x in arr:
#         if x < pivot:
#             left.append(x)
#         elif x > pivot:
#             right.append(x)
#         else:
#             middle.append(x)
#     return quick_sort(left) + middle + quick_sort(right)
# data = [9, 3, 5, 1  ]
# hasil = quick_sort(data)
# print("Hasil sorting:", hasil)a


