         ___        ______     ____ _                 _  ___  
        / \ \      / / ___|   / ___| | ___  _   _  __| |/ _ \ 
       / _ \ \ /\ / /\___ \  | |   | |/ _ \| | | |/ _` | (_) |
      / ___ \ V  V /  ___) | | |___| | (_) | |_| | (_| |\__, |
     /_/   \_\_/\_/  |____/   \____|_|\___/ \__,_|\__,_|  /_/ 
 ----------------------------------------------------------------- 


Halo! Selamat datang di AWS Cloud9!

Untuk memulai, buatlah beberapa file, coba gunakan terminal,
atau kunjungi https://docs.aws.amazon.com/console/cloud9/ untuk dokumentasi resmi.

Selamat ngoding! 🚀

# Deskripsi
Kode latihan python untuk kelas IDJAK127


# Cara mengintegrasikan AWS Cloud9 dengan GitHub

<img width="733" height="433" alt="Pasted Graphic 1" src="https://github.com/user-attachments/assets/2d5f90cd-3e3a-4ec0-8349-f13e1126be29" />

1. Buat folder .ssh di folder root.
   ```
   mkdir .ssh
   ```
   
2. Hasilkan pasangan SSH key dengan nama "github". Kamu bisa mengganti namanya sesuai kebutuhan.
   ```
   ssh-keygen -t ed25519 -C "youremail@gmail.com" -f /home/ec2-user/environment/.ssh/github
   ```

3. Daftarkan public key yang dihasilkan (github.pub) ke GitHub.
   <img width="946" height="520" alt="image" src="https://github.com/user-attachments/assets/51f623f6-a07f-4225-926f-8b28a2219da6" />

   > **_Login ke akun GitHub kamu melalui github.com -> Profile (pojok kanan atas) -> Settings -> SSH and GPG Keys -> New SSH key:_**
   > **_Salin semua isi file .ssh/github.pub -> tempelkan pada field SSH key (lihat gambar di atas).:_**

   
4. Buat koneksi SSH dengan path key khusus. (Langkah ini perlu diulang setiap kali mesin Cloud9 dijalankan kembali)
   ```
   eval "$(ssh-agent -s)"
   ssh-add .ssh/github
   ```

5. Validasi koneksi SSH & pastikan key berhasil dimuat.
   ```
   ssh git@github.com
   ```
   Hasil yang diharapkan:
   ```
   Hi yourgithubusername! You've successfully authenticated, but GitHub does not provide shell access.
   ```
   **Jika autentikasi gagal, ulangi langkah dari awal. **

6. Buat file **.gitignore** dan isi dengan kode berikut. Ingat: kita tidak boleh membagikan private key ke siapa pun. Menyimpan key di mesin lokal adalah keharusan!!
   ```
   .ssh/
   .c9/
   ```
   
7. Inisialisasi git lokal baru. Secara default, repository baru akan menempatkan kode di branch "master".
   ```
   git init
   ```

8. Daftarkan remote repository GitHub.
   Catatan: alamat SSH remote selalu diawali dengan **git@github.com:...**
   <img width="395" alt="image" src="https://github.com/user-attachments/assets/d8ce22ef-1030-4c42-b571-ceae79b89b1e" />
   ```
   git remote add origin [copied ssh remote address]
   ```


9. Buat dan checkout ke branch baru bernama "main". Ingat, branch default di GitHub adalah "main", jadi kita perlu menyesuaikan.
   ```
   git checkout -b main
   ```

10. Uji coba menarik kode dari GitHub.
   ```
   git pull origin main
   ```
   
   Jika muncul error "unrelated history", jalankan:
   ```
   git pull origin main --allow-unrelated-histories
   ```

   Jika muncul peringatan "You have divergent branches and need to specify how to reconcile them...", jalankan:
   ```
   git config pull.rebase false
   ```
   
11. Sinkronkan kode kamu dari git lokal ke GitHub (lakukan ini setiap kali ingin mengirim update baru).
   ```
   git add .
   git commit -m "Commit Message/Update notes"
   git push origin main --force
   ```

12. Cek kode yang sudah kamu unggah di GitHub. Selamat ngoding!


   
