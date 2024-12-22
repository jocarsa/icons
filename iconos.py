def generate_svg(filename):
    width = 960
    height = 960
    step = 32

    # Start SVG content
    svg_content = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        f'  <!-- Background -->',
        f'  <rect width="{width}" height="{height}" fill="#ffffff" />',
        f'',
        f'  <!-- Vertical Guides -->',
        f'  <g stroke="#cccccc" stroke-width="0.5">'
    ]

    # Vertical guides
    for x in range(step, width, step):
        svg_content.append(f'    <line x1="{x}" y1="0" x2="{x}" y2="{height}" />')

    svg_content.append(f'  </g>')
    svg_content.append(f'')
    svg_content.append(f'  <!-- Horizontal Guides -->')
    svg_content.append(f'  <g stroke="#cccccc" stroke-width="0.5">')

    # Horizontal guides
    for y in range(step, height, step):
        svg_content.append(f'    <line x1="0" y1="{y}" x2="{width}" y2="{y}" />')

    svg_content.append(f'  </g>')
    svg_content.append(f'</svg>')

    # Write to file
    with open(filename, 'w') as file:
        file.write("\n".join(svg_content))

# Generate the SVG file
generate_svg("grid_3200x3200.svg")
