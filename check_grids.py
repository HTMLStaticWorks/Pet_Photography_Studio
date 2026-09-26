import re
import glob

def process_file(f):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Let's find any grid that has grid-cols-1 md:grid-cols-2 lg:grid-cols-3
    grids = re.split(r'(<div[^>]*class="[^"]*grid-cols-1 md:grid-cols-2 lg:grid-cols-3[^"]*">)', content)
    
    if len(grids) == 1:
        return
        
    modified = False
    new_content = grids[0]
    
    for i in range(1, len(grids), 2):
        grid_tag = grids[i]
        grid_body = grids[i+1]
        
        # Determine gap to calculate width
        gap_match = re.search(r'gap-(\d+)', grid_tag)
        gap = int(gap_match.group(1)) if gap_match else 8
        rem_value = gap * 0.25
        width_calc = f'calc(50%-{rem_value/2}rem)'
        
        # We need to find the direct children divs. This is tricky with regex.
        # But we know the 3rd card needs classes.
        # For simplicity, if we know it's testimonials or gallery in index.html, we can just replace.
        
        new_content += grid_tag + grid_body

process_file('index.html')
