import glob, re

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # We find all occurrences of grid-cols-1 md:grid-cols-3 gap-(6|8|12)
    grid_pattern = re.compile(r'(<div[^>]*class="[^"]*grid[^"]*grid-cols-1 md:grid-cols-3 gap-(\d+)[^"]*">)(.*?)(?=\n\s*</section>|\n\s*</div>\n\s*</div>)', re.DOTALL)
    
    # Wait, regex parsing HTML is fragile.
    # It's better to just do it manually for the known grids.
