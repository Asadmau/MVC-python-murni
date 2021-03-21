class Mahasiswa(object):
    def __init__(self, nim, nama, alamat):
        self.nim = nim
        self.nama = nama
        self.alamat = alamat
    def getNim(self):
        return self.nim
    def setNim(self, nim):
        self.nim = nim
    def getNama(self):
        return self.nama
    def setNama(self, nama):
        self.nama = nama
    def getAlamat(self):
        return self.alamat
    def setAlamat(self, alamat):
        self.alamat = alamat
    def getAll(self):
        data = {
            'nim' : self.getNim(),
            'nama' : self.getNama(),
            'alamat' : self.getAlamat()
        }
        return data
    def setAll(self, data):
        self.setNim(data['nim'])
        self.setNama(data['nama'])
        self.getAlamat(data['alamat'])