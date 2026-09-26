import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's see the pricing grid.
start = content.find('it every pet\'s comfort and personality.</p>')
end = content.find('<section id="testimonials"', start)
print(content[start:start+1500])
