#Menggunakan Metode Center
Judul = "Survey Kebersihan Toilet Siswa SMAN 81 Jakarta"
a = Judul.center (50,'=')
print (a)

#Menggunakan Metode Endswith
str = "Apakah Keran Air Berfungsi?"
print("Apakah Keran Air Berfungsi?")
print (str.endswith("Berfungsi?"))

#Menggunakan Metode Replace dan Endswith
str = "Apakah Airnya Berwarna?"
b = str.replace ("Berwarna","Keruh")
print(b)
print(str.endswith("Berwarna?"))