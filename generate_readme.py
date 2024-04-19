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

{languages_tools}

![GitHub Stats]({github_stats_link})

***********************************

#### Thank You-🙏🏼.
"""
    return readme_content

# Data untuk mengisi variabel dalam README
name = "Yudi Billy"
city = "SURABAYA"
working_on = "tukangsby.com"
portfolio_link = "https://github.com/maulayyacyber/portfolio/blob/master/README.md"
youtube_channel = "https://youtube.com/@Yudibilly?si=1NOrsSsfdV52loLv"
ebook_link = "https://santrikoding.com/ebook"
email = "yudibilly@gmail.com"

# Daftar bahasa dan tools (gunakan format Markdown untuk gambar)
languages_tools = """
<img height="50" src="https://santrikoding.com/storage/categories/11166a84-9aa9-4afc-9e30-b25d00dfc575.webp">
<img height="50" src="https://santrikoding.com/storage/categories/8c30b91e-fa6a-408c-b9c9-029fd6a0a887.webp">
<img height="50" src="https://santrikoding.com/storage/categories/f33b3b22-847a-44eb-b334-9695069dbbf9.webp">
<img height="50" src="https://santrikoding.com/storage/categories/10b6992b-1d4f-47e5-b2a5-e5e6e8595bc8.webp">
<img height="50" src="https://santrikoding.com/storage/categories/df6e5b68-ccbd-4c14-9eec-89789e546da3.webp">
<img height="50" src="https://santrikoding.com/storage/categories/0eb18343-130f-4fe8-b82b-36f0ac89595d.webp">
<img height="50" src="https://santrikoding.com/storage/categories/d629226b-24e4-41eb-bafe-1ee86f3dc102.webp">
"""

github_stats_link = "https://github-readme-stats.vercel.app/api?username=maulayyacyber&show_icons=true&hide_border=true"

# Memanggil fungsi untuk menghasilkan konten README
generated_readme = generate_readme(name, city, working_on, portfolio_link, youtube_channel, ebook_link, email, languages_tools, github_stats_link)

# Menyimpan konten README ke dalam file README.md
with open('README.md', 'w') as readme_file:
    readme_file.write(generated_readme)

print("README.md telah berhasil dibuat atau diperbarui.")

