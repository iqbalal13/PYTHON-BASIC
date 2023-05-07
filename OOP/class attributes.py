class siswa:
    jumlah_siswa = 0

    def __init__(self, nama: str, kelas: str):
        self.nama = nama
        self.kelas = kelas
        siswa.jumlah_siswa += 1

siswa1 = siswa("iqbal","1B")

jumlah_siswa = 70
print(siswa1.nama)