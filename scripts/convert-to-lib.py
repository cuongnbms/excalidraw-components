#!/usr/bin/env python3
"""
Convert .excalidraw files to .excalidrawlib format.

Groups elements by ID prefix and creates separate library items for each component.
"""

import json
import os
import sys
import time
from pathlib import Path
from collections import defaultdict


def get_component_prefix(element_id: str) -> str | None:
    """Extract component prefix from element ID (e.g., 'user-head' -> 'user')."""
    if element_id == "title":
        return None  # Skip title elements

    # Handle IDs like "user-head", "phone-body", "laptop-screen-frame"
    parts = element_id.split("-")
    if len(parts) >= 2:
        # For compound prefixes like "user-alt", check if second part is descriptive
        if len(parts) >= 3 and parts[1] in ("alt", "stand"):
            return f"{parts[0]}-{parts[1]}"
        return parts[0]

    return element_id


def normalize_elements(elements: list[dict]) -> list[dict]:
    """Normalize element positions so the group starts at (0, 0)."""
    if not elements:
        return elements

    # Find bounding box
    min_x = min(e.get("x", 0) for e in elements)
    min_y = min(e.get("y", 0) for e in elements)

    # Offset all elements
    normalized = []
    for element in elements:
        new_element = element.copy()
        new_element["x"] = element.get("x", 0) - min_x
        new_element["y"] = element.get("y", 0) - min_y
        normalized.append(new_element)

    return normalized


def group_elements_by_component(elements: list[dict]) -> dict[str, list[dict]]:
    """Group elements by their component prefix."""
    groups = defaultdict(list)

    for element in elements:
        prefix = get_component_prefix(element.get("id", ""))
        if prefix:
            groups[prefix].append(element)

    return dict(groups)


def create_library_item(component_name: str, elements: list[dict]) -> dict:
    """Create a library item from a group of elements."""
    normalized = normalize_elements(elements)

    return {
        "id": component_name,
        "status": "published",
        "elements": normalized,
        "created": int(time.time() * 1000)
    }


def convert_file(input_path: Path) -> dict:
    """Convert a single .excalidraw file to library format."""
    with open(input_path) as f:
        data = json.load(f)

    elements = data.get("elements", [])
    groups = group_elements_by_component(elements)

    library_items = []
    for component_name, component_elements in sorted(groups.items()):
        item = create_library_item(component_name, component_elements)
        library_items.append(item)
        print(f"  → {component_name}: {len(component_elements)} elements")

    return {
        "type": "excalidrawlib",
        "version": 2,
        "source": "https://excalidraw.com",
        "libraryItems": library_items
    }


def convert_directory(input_dir: Path, output_file: Path):
    """Convert all .excalidraw files in a directory to a single library."""
    all_items = []

    for excalidraw_file in sorted(input_dir.glob("*.excalidraw")):
        print(f"\nProcessing: {excalidraw_file.name}")

        with open(excalidraw_file) as f:
            data = json.load(f)

        elements = data.get("elements", [])
        groups = group_elements_by_component(elements)

        # Use filename as category prefix
        category = excalidraw_file.stem

        for component_name, component_elements in sorted(groups.items()):
            item = create_library_item(
                f"{category}-{component_name}",
                component_elements
            )
            all_items.append(item)
            print(f"  → {component_name}: {len(component_elements)} elements")

    library = {
        "type": "excalidrawlib",
        "version": 2,
        "source": "https://excalidraw.com",
        "libraryItems": all_items
    }

    with open(output_file, "w") as f:
        json.dump(library, f, indent=2)

    print(f"\n✅ Created library with {len(all_items)} items: {output_file}")


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  Convert single file:    python convert-to-lib.py input.excalidraw [output.excalidrawlib]")
        print("  Convert directory:      python convert-to-lib.py input_dir/ output.excalidrawlib")
        sys.exit(1)

    input_path = Path(sys.argv[1])

    if input_path.is_dir():
        # Convert all files in directory
        if len(sys.argv) < 3:
            output_path = input_path / "library.excalidrawlib"
        else:
            output_path = Path(sys.argv[2])

        convert_directory(input_path, output_path)

    elif input_path.is_file():
        # Convert single file
        if len(sys.argv) >= 3:
            output_path = Path(sys.argv[2])
        else:
            output_path = input_path.with_suffix(".excalidrawlib")

        print(f"Converting: {input_path.name}")
        library = convert_file(input_path)

        with open(output_path, "w") as f:
            json.dump(library, f, indent=2)

        print(f"\n✅ Created: {output_path}")

    else:
        print(f"Error: {input_path} not found")
        sys.exit(1)


if __name__ == "__main__":
    main()
