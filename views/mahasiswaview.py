class MahasiswaView(object):
    def formMahasiswa(self):
        nim = int(input('nim :'))
        nama = input('nama mahasiswa :')
        alamat = input('alamat :')

        # //type dict
        dictmahasiswa = {
            'nim' : nim,
            'nama' : nama,
            'alamat' : alamat
        }
        return dictmahasiswa

    def tampilMahasiswa(self):
        print("[1]. View Profile\n[2]. Exit")
        option = input("\nYour Option: ")
        return option

    def mahasiswaPage(self, data):
        print("nim: " + str(data['nim']))
        print("nama: " + data['nama'])
        print("alamat: " + data['alamat'] + "\n")