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

# Meminta input data dari pengguna
name = input("Masukkan nama Anda: ")
city = input("Masukkan kota Anda: ")
working_on = input("Apa yang sedang Anda kerjakan? ")
portfolio_link = input("Masukkan link portofolio Anda: ")
youtube_channel = input("Masukkan link channel Youtube Anda: ")
ebook_link = input("Masukkan link e-book Anda: ")
email = input("Masukkan alamat email Anda: ")

# Daftar untuk menyimpan URL gambar
languages_tools_urls = []

# Loop untuk meminta input URL gambar dari pengguna
while True:
    url = input("Masukkan URL gambar (atau ketik 'exit' untuk selesai): ")
    if url.lower() == 'exit':
        break
    languages_tools_urls.append(url)

# Menghasilkan tag <img> untuk setiap URL gambar dalam daftar
languages_tools = "\n".join(f'<img style="margin-right: 10px; margin-bottom: 10px;" height="50" src="{url}">' for url in languages_tools_urls)

github_stats_link = "https://github-readme-stats.vercel.app/api?username=maulayyacyber&show_icons=true&hide_border=true"

# Memanggil fungsi untuk menghasilkan konten README
generated_readme = generate_readme(name, city, working_on, portfolio_link, youtube_channel, ebook_link, email, languages_tools, github_stats_link)

# Menyimpan konten README ke dalam file README.md
with open('README.md', 'w') as readme_file:
    readme_file.write(generated_readme)

print("README.md telah berhasil dibuat atau diperbarui.")

