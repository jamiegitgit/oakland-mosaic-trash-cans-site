# First, get the template files
top_template = open('templates/top.html').read()
top_header = open ('templates/topheader.html').read()
bottom_template = open('templates/bottom.html').read()
bottom_footer = open('templates/bottomfooter.html').read()

# Read in index HTML code
content = open('content/index.html').read()

# Combine template HTML code with content HTML code
#index_html = top_template + content + bottom_template
#open('index.html', 'w+').write(index_html)

# Rinse and repeat, but with blog HTML code
#content = open('middle_blog.html').read()
#blog_html = top_template + content + bottom_template
#open('blog.html', 'w+').write(blog_html)

# And again, this time with art HTML code
#content = open('middle_art.html').read()
#art_html = top_template + content + bottom_template
#open('art.html', 'w+').write(art_html)

