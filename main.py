import mysql.connector
from mysql.connector import Error

# Membuat koneksi ke database MySQL.
def create_connection(): 
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # Replace with your MySQL username
            password='',  # Replace with your MySQL password
            database='db_health'  # Replace with your MySQL database name
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

# Meminta pengguna untuk memasukkan bilangan bulat/integer.
def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Masukkan tidak sesuai, harap masukkan angka.")

# Menambahkan data pasien baru ke database.
def add_data(data): 
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute('''
                INSERT INTO pasien (
                    tanggal_periksa, nama_lengkap, jenis_kelamin, tempat_tanggal_lahir, 
                    alamat, no_hp, pekerjaan, poli, alergi_obat, keluhan
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ''', (
                data['tanggal_periksa'], data['nama_lengkap'], data['jenis_kelamin'], 
                data['tempat_tanggal_lahir'], data['alamat'], data['no_hp'], 
                data['pekerjaan'], data['poli'], data['alergi_obat'], data['keluhan']
            ))
            connection.commit()
            print("Data berhasil ditambahkan.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            connection.close()

# Mengambil semua data pasien dari database.
def get_all_data():
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM pasien")
            results = cursor.fetchall()
            for row in results:
                print(row)
        except Error as e:
            print(f"Error: {e}")
        finally:
            connection.close()

# Mengambil/menampilkan data pasien berdasarkan ID.
def get_data_by_id(id_pasien):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM pasien WHERE id_pasien = %s", (id_pasien,))
            result = cursor.fetchone()
            if result:
                print(result)
            else:
                print("Data tidak ditemukan.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            connection.close()

# Memperbarui data pasien berdasarkan ID.
def update_data(id_pasien, updated_data):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute('''
                UPDATE pasien SET
                    tanggal_periksa = %s,
                    nama_lengkap = %s,
                    jenis_kelamin = %s,
                    tempat_tanggal_lahir = %s,
                    alamat = %s,
                    no_hp = %s,
                    pekerjaan = %s,
                    poli = %s,
                    alergi_obat = %s,
                    keluhan = %s
                WHERE id_pasien = %s
            ''', (
                updated_data['tanggal_periksa'], updated_data['nama_lengkap'], 
                updated_data['jenis_kelamin'], updated_data['tempat_tanggal_lahir'], 
                updated_data['alamat'], updated_data['no_hp'], updated_data['pekerjaan'], 
                updated_data['poli'], updated_data['alergi_obat'], updated_data['keluhan'], id_pasien
            ))
            connection.commit()
            print("Data berhasil diperbarui.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            connection.close()

# Menghapus data pasien berdasarkan ID.
def delete_data(id_pasien):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM pasien WHERE id_pasien = %s", (id_pasien,))
            connection.commit()
            print("Data berhasil dihapus.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            connection.close()

# Program utama.
def main_menu():
    while True:
        print("\nMenu:")
        print("1. Tambahkan Data Pasien")
        print("2. Tampilkan Semua Data Pasien")
        print("3. Tampilkan Data Pasien Berdasarkan ID")
        print("4. Perbarui Data Pasien")
        print("5. Hapus Data Pasien")
        print("6. Keluar")
        choice = input("Masukkan pilihan Anda: ")

        if choice == "1":
            print("\nMasukkan angka [0] untuk kembali ke menu utama.")
            tanggal_periksa = input("Tanggal Periksa (YYYY-MM-DD): ")
            if tanggal_periksa == "0":
                print("Kembali ke menu utama.")
                continue
            nama_lengkap = input("Nama Lengkap: ")
            if nama_lengkap == "0":
                print("Kembali ke menu utama.")
                continue
            jenis_kelamin = input("Jenis Kelamin (L/P): ")
            if jenis_kelamin == "0":
                print("Kembali ke menu utama.")
                continue
            tempat_tanggal_lahir = input("Tempat Tanggal Lahir: ")
            if tempat_tanggal_lahir == "0":
                print("Kembali ke menu utama.")
                continue
            alamat = input("Alamat: ")
            if alamat == "0":
                print("Kembali ke menu utama.")
                continue
            no_hp = input("No HP: ")
            if no_hp == "0":
                print("Kembali ke menu utama.")
                continue
            pekerjaan = input("Pekerjaan: ")
            if pekerjaan == "0":
                print("Kembali ke menu utama.")
                continue
            poli = input("Poli: ")
            if poli == "0":
                print("Kembali ke menu utama.")
                continue
            alergi_obat = input("Alergi Obat: ")
            if alergi_obat == "0":
                print("Kembali ke menu utama.")
                continue
            keluhan = input("Keluhan: ")
            if keluhan == "0":
                print("Kembali ke menu utama.")
                continue

            data = {
                "tanggal_periksa": tanggal_periksa,
                "nama_lengkap": nama_lengkap,
                "jenis_kelamin": jenis_kelamin,
                "tempat_tanggal_lahir": tempat_tanggal_lahir,
                "alamat": alamat,
                "no_hp": no_hp,
                "pekerjaan": pekerjaan,
                "poli": poli,
                "alergi_obat": alergi_obat,
                "keluhan": keluhan
            }
            add_data(data)
        elif choice == "2":
            get_all_data()
        elif choice == "3":
            print("\nMasukkan angka [0] untuk kembali ke menu utama.")
            id_input = input("Masukkan ID Pasien: ")
            if id_input == "0":
                print("Kembali ke menu utama.")
                continue
            id_pasien = int(id_input)
            get_data_by_id(id_pasien)
        elif choice == "4":
            print("\nMasukkan angka [0] untuk kembali ke menu utama.")
            id_input = input("Masukkan ID Pasien yang Ingin Diperbarui: ")
            if id_input == "0":
                print("Kembali ke menu utama.")
                continue
            id_pasien = int(id_input)
            updated_data = {
                "tanggal_periksa": input("Tanggal Periksa (YYYY-MM-DD): "),
                "nama_lengkap": input("Nama Lengkap: "),
                "jenis_kelamin": input("Jenis Kelamin (L/P): "),
                "tempat_tanggal_lahir": input("Tempat Tanggal Lahir: "),
                "alamat": input("Alamat: "),
                "no_hp": input("No HP: "),
                "pekerjaan": input("Pekerjaan: "),
                "poli": input("Poli: "),
                "alergi_obat": input("Alergi Obat: "),
                "keluhan": input("Keluhan: ")
            }
            update_data(id_pasien, updated_data)
        elif choice == "5":
            print("\nMasukkan angka [0] untuk kembali ke menu utama.")
            id_input = input("Masukkan ID Pasien yang Ingin Dihapus: ")
            if id_input == "0":
                print("Kembali ke menu utama.")
                continue
            id_pasien = int(id_input)
            delete_data(id_pasien)
        elif choice == "6":
            confirm = input("Apakah yakin akan keluar dari program? (y/n): ").lower()
            if confirm == "y":
                print("========== Keluar dari program. ==========")
                break
            else:
                print("Kembali ke menu utama.")
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main_menu()
