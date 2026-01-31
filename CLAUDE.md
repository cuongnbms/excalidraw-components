This is a great aesthetic to aim for. The "hand-drawn" architectural style is perfect for system design diagrams because it feels approachable and clean.

---

## Agentic Coding Rules: Excalidraw Component Generation

### 1. Structural Composition

Every component must follow a strict three-layer hierarchy:

* **The Container:** A `rectangle` element with rounded corners acting as the boundary.
* **The Visual Center:** An `icon`, `inner drawing`, or `shape` (like the orange squares in the reference) placed precisely in the horizontal and vertical center of the container.
* **The Label:** A `text` element placed directly below the container, centered horizontally.

### 2. Visual Style & "Roughness"

To match the hand-drawn aesthetic of the reference image, apply these properties to all generated elements:

* **Roughness:** Set to `1` or `2` (avoid `0` to keep the "hand-drawn" feel).
* **Stroke Width:** Use `2` for containers and `1.5` for internal icons.
* **Stroke Sharpness:** Always set to `round`.
* **Fill Style:** Use `solid` or `hachure` for internal elements (like the orange boxes) to create contrast against the background.
* **Font Family:** Use `1` (Excalidraw’s default hand-drawn font).

### 3. Layout Constants (Spacing & Alignment)

Maintain consistency across all components:

* **Padding:** Ensure a minimum internal padding of `20px` between the container border and the inner icon.
* **Label Gap:** The text label should be positioned `10px` to `15px` below the bottom edge of the container.
* **Grouping:** Always wrap the container, inner icon, and text label into a single `group` in the Excalidraw JSON to allow for easy moving/scaling.

### 4. Color Palette

Unless specified otherwise, use a professional, muted palette:

* **Container Stroke:** `#000000` (Black).
* **Inner Icon Fill:** Use a distinct accent color (e.g., `#ff922b` for orange or `#4dabf7` for blue) to highlight functionality.
* **Text:** `#000000` (Black).

Each component creates several different variations, all in a single file named `<component>.excalidraw`

### Suggested Component Templates

You can ask the agent to create specific components based on these rules, such as:

* **Database:** Cylinder icon centered in a rectangle + "PostgreSQL" text.
* **Cache:** Lightning bolt icon centered in a rectangle + "Redis" text.
* **API Gateway:** Door/Proxy icon centered in a rectangle + "Gateway" text.

Would you like me to generate a sample **JSON structure** for one of these components that you can import directly into Excalidraw?