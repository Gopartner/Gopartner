def generate_readme(name, city, working_on, portfolio_link, youtube_channel, ebook_link, email, languages_tools, github_stats_link):
    readme_content = f"""<h1 align="center">Hi 👋, I'm {name}</h1>
<h3 align="center">A Software Engineer 🚀 from {city}</h3>
                                                      <br>                                                  
- 🔭 I’m currently working on [{working_on}](https://santrikoding.com)
- 👨‍💻 Portfolio at [Here]({portfolio_link})
- 🎥 My Channel [Youtube]({youtube_channel})
- 📚 My E-book at [Here]({ebook_link})
- ✉️ How to reach me **{email}**
                                                      **Languages & Tools:**                                
<div style="display: flex; flex-wrap: wrap;">
{languages_tools}
</div>

![GitHub Stats]({github_stats_link})
                                                      ***********************************

#### Thank You-🙏🏼.
"""
    return readme_content

# Meminta input data dari pengguna jika tidak ada data sebelumnya atau jika pengguna memberikan input baru
def get_input(prompt, default):
    user_input = input(prompt)
    if user_input.strip():  # Cek apakah input tidak kosong
        return user_input
    else:
        return default

# Meminta data pengguna untuk informasi yang diperlukan
name = get_input("Masukkan nama Anda: ", "John Doe")
city = get_input("Masukkan kota Anda: ", "Unknown City")
working_on = get_input("Apa yang sedang Anda kerjakan? ", "Project X")
portfolio_link = get_input("Masukkan link portofolio Anda: ", "https://example.com/portfolio")
youtube_channel = get_input("Masukkan link channel Youtube Anda: ", "https://www.youtube.com/user/example")
ebook_link = get_input("Masukkan link e-book Anda: ", "https://example.com/ebook")
email = get_input("Masukkan alamat email Anda: ", "example@example.com")

# Daftar untuk menyimpan URL gambar
languages_tools_urls = []

# Loop untuk meminta input URL gambar dari pengguna
while True:
    url = input("Masukkan URL gambar (atau ketik 'exit' untuk selesai): ")
    if url.lower() == 'exit':
        break
    if url.strip():  # Cek apakah URL tidak kosong
        languages_tools_urls.append(url)

# Jika tidak ada URL baru, gunakan URL sebelumnya
if not languages_tools_urls:
    languages_tools_urls = ["https://example.com/image1.jpg", "https://example.com/image2.jpg"]

# Menghasilkan tag <img> untuk setiap URL gambar dalam daftar
languages_tools = "\n".join(f'<img style="margin-right: 10px; margin-bottom: 10px;" height="50" src="{url}">' for url in languages_tools_urls)


# Memanggil fungsi untuk menghasilkan konten README
generated_readme = generate_readme(name, city, working_on, portfolio_link, youtube_channel, ebook_link, email, languages_tools, github_stats_link)

# Menyimpan konten README ke dalam file README.md
with open('README.md', 'w') as readme_file:
    readme_file.write(generated_readme)

print("README.md telah berhasil dibuat atau diperbarui.")


