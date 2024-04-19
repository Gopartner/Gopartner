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
working_on = "SantriKoding"
portfolio_link = "https://github.com/maulayyacyber/portfolio/blob/master/README.md"
youtube_channel = "https://youtube.com/@Yudibilly?si=1NOrsSsfdV52loLv"
ebook_link = "https://santrikoding.com/ebook"
email = "yudibilly@gmail.com"

# Daftar bahasa dan tools (gunakan format Markdown untuk gambar)
languages_tools = """
<img height="50" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHUTeQ1lG65P_SULpnMYXNDDCWjklYJofm5mpM0h99AmZ87a0J_F00m8YOmJhnMJq0pmLDqLqi4c6lOLTOBCSxVj6BwkpRJMokGTi-d1h1Vw1ZhR8rGLi3NljyMVlhrqD212e8ikHCe2y8C4sebn8s6o7R_0zC8yBvixIxKRHRbBZ-XbAhVnz-rPQB63Y/s200/express.webp">
<img height="50" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjlxvSXJVxokMCldUF9tFDlDF_sCOcBBM7ErT0hokBYQhbQcb-lIJrCpdYSBhEEBY3cE2faXOpPZDVIZ57dq_GwnvnPwNbUjCT3AJcWv9ckas4AqeVmbNFOxxhhF4HjSyU_bzqhENAfbVXOiAMPXvrXKu81Sk3-6eoGk5b0hIfHbkEPH7IBMdXC2MorGko/s200/laravel.webp">
<img height="50" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhHVloB1KINN1wDthSBFJP_vyvPWa3aU56Yg-nSk6lbC_OGVypomAmpkeedVwW4wbr5gaOCI5uz093LacXFhRhPOxzpLW3zqWW6NOOus1m9E6wj90WD80DZW5LQHp_eQ-hgDaR7kCBVC5D-5RlJY3SFpf1drJ4oJ4ZqdKqiFAaFXxW6tN8WJ0pJ6qm86JY/s200/javascript.webp">
"""

github_stats_link = "https://github-readme-stats.vercel.app/api?username=maulayyacyber&show_icons=true&hide_border=true"

# Memanggil fungsi untuk menghasilkan konten README
generated_readme = generate_readme(name, city, working_on, portfolio_link, youtube_channel, ebook_link, email, languages_tools, github_stats_link)

# Menyimpan konten README ke dalam file README.md
with open('README.md', 'w') as readme_file:
    readme_file.write(generated_readme)

print("README.md telah berhasil dibuat atau diperbarui.")

