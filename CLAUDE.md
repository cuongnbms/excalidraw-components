# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Static library of reusable Excalidraw components for system design diagrams. No build system or dependencies—just JSON files.

## File Format

Each `.excalidraw` file is JSON with this structure:
```json
{
  "type": "excalidraw",
  "version": 2,
  "source": "https://excalidraw.com",
  "elements": [...],
  "appState": { "gridSize": 20, "viewBackgroundColor": "#ffffff" },
  "files": {}
}
```

## Component Style Standards

When creating new components:
- **strokeColor**: `#1e1e1e`
- **strokeWidth**: 2 for main shapes, 1 for details
- **fillStyle**: `solid`
- **roughness**: 1
- **backgroundColor**: Pastel colors (e.g., `#a5d8ff`, `#b2f2bb`, `#ffc9c9`)
- **Labels**: fontSize 14-16, textAlign center
- **IDs**: Use descriptive kebab-case (e.g., `user-head`, `laptop-screen`)

## Adding Components

1. Group related components in one file by category
2. Include a title text element at top (fontSize 24)
3. Arrange components in rows with ~200px horizontal spacing
4. Add label text below each component
5. Increment seed values sequentially within a file
