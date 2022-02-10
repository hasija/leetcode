arr= [1,3,5,8,10] 
start = 0
end = len(arr)-1
least = None
print (arr)
while(start<len(arr)):
	if not least:
		least = arr[0]
	tmp = arr[start]
	arr[start]=arr[end]
	arr[end]=arr[start]
	start+=1
	if start<len(arr):
		new_least = arr[start]
		arr[start]= least
		arr[end]= new_least
		least = new_least
	start+=1
	end-=1
	print (arr, least)
print (arr)