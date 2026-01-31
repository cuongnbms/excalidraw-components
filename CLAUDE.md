# Excalidraw Component Generation Guidelines

Hand-drawn architectural style for system design diagrams - approachable, clean, and professional.

---

## 1. Structural Composition

Every component follows a **three-layer hierarchy**:

* **Container:** A single `rectangle` with dark stroke (`#1e1e1e`), rounded corners, and **full background fill** - no inner padding rectangle.
* **Visual Elements:** Icons, shapes, or message boxes centered inside with visual indicators:
  * **Flow arrow** (`→`) for standard queues
  * **X mark** for dead letter / failed message queues
  * **Color coding** for priority queues (red=high, orange=medium, green=low)
* **Label:** Multi-line `text` below the container:
  * Line 1: Component name (e.g., "Message Queue")
  * Line 2: Type/variant description (e.g., "FIFO / Priority")

## 2. Visual Style & "Roughness"

Apply these properties for hand-drawn aesthetic:

| Property | Container | Icons/Shapes | Text |
|----------|-----------|--------------|------|
| Roughness | `1` | `1` | `0` |
| Stroke Width | `2` | `1.5` | - |
| Fill Style | `solid` | `solid` | - |
| Font Family | - | - | `1` (hand-drawn) |

## 3. Layout Constants

* **Container Size:** `140x60` for queue-type components
* **Icon Padding:** `12px` from container edge to icons
* **Icon Size:** `24x24` squares with `4px` gap between them
* **Label Gap:** `12px` below container bottom
* **Line Spacing:** `24px` between label lines

## 4. Color Palette

### Queue Variants
| Variant | Background | Icon Colors | Indicator |
|---------|------------|-------------|-----------|
| Message Queue | `#ffd8a8` (peach) | `#e8590c` (orange) | Arrow `→` |
| Dead Letter Queue | `#868e96` (gray) | `#343a40` (dark gray) | X mark |
| Priority Queue | `#ffc078` (orange) | `#e03131` red, `#f76707` orange, `#2f9e44` green | Color bands |

### Visual Indicators
| Indicator | Usage | Color |
|-----------|-------|-------|
| Flow Arrow | Standard queue output | `#495057` |
| X Mark | Failed/rejected messages | `#f8f9fa` (white) |
| Priority Colors | High/Medium/Low priority | Red → Orange → Green |

## 5. File Organization

* Save all variations in single file: `<component>.excalidraw`
* Group all elements per component variant
* Use descriptive group IDs: `queue-fifo-group`, `queue-dlq-group`, `queue-priority-group`

## 6. Component Templates

### Message Queue (FIFO / Priority)
```
[Rectangle: 140x60, stroke #1e1e1e, fill #ffd8a8]
  └─[Box 1: 24x24, fill #e8590c]
  └─[Box 2: 24x24, fill #e8590c]
  └─[Box 3: 24x24, fill #e8590c]
  └─[Box 4: 24x24, fill #e8590c]
  └─[Arrow: →, stroke #495057]
[Text: "Message Queue"]
[Text: "FIFO / Priority"]
```

### Dead Letter Queue
```
[Rectangle: 140x60, stroke #1e1e1e, fill #868e96]
  └─[Box 1: 24x24, fill #343a40]
  └─[Box 2: 24x24, fill #343a40]
  └─[Box 3: 24x24, fill #343a40 + X mark]
[Text: "Dead Letter Queue"]
[Text: "Failed Messages"]
```

### Priority Queue
```
[Rectangle: 140x60, stroke #1e1e1e, fill #ffc078]
  └─[Box 1: 24x24, fill #e03131 (high)]
  └─[Box 2: 24x24, fill #f76707 (medium)]
  └─[Box 3: 24x24, fill #2f9e44 (low)]
[Text: "Priority Queue"]
[Text: "High → Low"]
```
