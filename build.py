# First, get the template files
top_template = open('templates/top.html').read()
top_header = open ('templates/topheader.html').read()
bottom_template = open('templates/bottom.html').read()
bottom_footer = open('templates/bottomfooter.html').read()

# Read in index HTML code
content = open('content/index.html').read()

# Combine template HTML code with content HTML code
index_html = top_template + content + bottom_template
open('docs/index.html', 'w+').write(index_html)

# Rinse and repeat, but with about me HTML code
content = open('content/about-me.html').read()
aboutme_html = top_template + top_header + content + bottom_footer + bottom_template
open('docs/about-me.html', 'w+').write(aboutme_html)

# And again, this time with gallery HTML code
content = open('content/gallery.html').read()
gallery_html = top_template + top_header + content + bottom_footer + bottom_template
open('docs/gallery.html', 'w+').write(gallery_html)

# And again, this time with contribute HTML code
content = open('content/contribute.html').read()
contribute_html = top_template + top_header + content + bottom_footer + bottom_template
open('docs/contribute.html', 'w+').write(contribute_html)
