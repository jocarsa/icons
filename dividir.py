import os
import xml.etree.ElementTree as ET

def create_icons_folder():
    if not os.path.exists("icons"):
        os.makedirs("icons")
    else:
        print("Icons folder already exists.")

def parse_svg(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    return tree, root

def get_paths_within_cell(root, x_min, y_min, cell_size):
    # This function is currently a placeholder to simulate paths being within bounds.
    # Replace with actual logic to determine if paths intersect the cell.
    return []

def create_cell_svg(x, y, cell_size, paths):
    cell_svg = ET.Element('svg', xmlns="http://www.w3.org/2000/svg", width=str(cell_size), height=str(cell_size),
                          viewBox=f"{x} {y} {cell_size} {cell_size}")
    for path in paths:
        cell_svg.append(path)
    return cell_svg

def write_cell_svg(cell_svg, x_index, y_index):
    filename = f"icons/icon_{x_index}_{y_index}.svg"
    ET.ElementTree(cell_svg).write(filename, encoding="utf-8", xml_declaration=True)
    print(f"Saved: {filename}")

def split_svg_to_cells(input_svg, cell_size=32):
    create_icons_folder()
    tree, root = parse_svg(input_svg)

    width = int(root.attrib.get('width', '0'))
    height = int(root.attrib.get('height', '0'))
    
    if width == 0 or height == 0:
        print("Invalid SVG dimensions. Ensure the SVG file has 'width' and 'height' attributes.")
        return

    print(f"Splitting SVG into {cell_size}x{cell_size} cells...")
    
    for x in range(0, width, cell_size):
        for y in range(0, height, cell_size):
            paths = get_paths_within_cell(root, x, y, cell_size)
            cell_svg = create_cell_svg(x, y, cell_size, paths)
            write_cell_svg(cell_svg, x // cell_size, y // cell_size)

# Run the script
split_svg_to_cells("grid_3200x3200.svg")
