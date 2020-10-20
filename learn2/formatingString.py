data = "Tulisan dummy ini adalah tulisan Testing Aja si ."


dataLower = data.lower()
dataUpper = data.upper()

print("{} data ini adalah normal".format(data))
print("{} data ini adalah lower".format(dataLower))
print("{} data ini adalah upper".format(dataUpper))

dataArray = data.split(' ')
print("Jumlah kata pada data dummy {}".format(len(dataArray)))