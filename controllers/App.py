from views.mahasiswaview import MahasiswaView
from models.mahasiswa import Mahasiswa

class App(object):
    def createMahasiswa(self):
        views = MahasiswaView()
        data = views.formMahasiswa()

        return data
    def viewsmahasiswa(self, data):
        views = MahasiswaView()
        views.mahasiswaPage(data)

        self.tampil(data)

    def tampil(self, data):
        view = MahasiswaView()

        option = view.tampilMahasiswa()
        if option == '1':
            self.viewsmahasiswa(data)
        elif option == '2':
            print('Stop runing')
        else:
            print("Error 404")
            self.tampil(data)

    def run(self):

        registerData = self.createMahasiswa()

        nim = registerData['nim']
        nama = registerData['nama']
        alamat = registerData['alamat']

        mahasiswa = Mahasiswa(nim, nama, alamat)

        DataMahasiswa = mahasiswa.getAll()

        self.tampil(DataMahasiswa)