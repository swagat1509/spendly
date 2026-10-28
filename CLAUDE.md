# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Spendly** is a Flask-based expense tracker web application. It's designed as a student learning project with incremental feature development steps. The application allows users to register, log in, and manage their expenses.

## Architecture

### Directory Structure

- **app.py** — Main Flask application entry point. Contains all routes organized into sections:
  - Core routes (landing, register, login, terms/privacy)
  - Placeholder routes for student implementation (steps 3-9)
- **database/** — Database setup and operations
  - `db.py` is currently a stub; students implement `get_db()`, `init_db()`, and `seed_db()`
  - SQLite is used as the database engine
- **templates/** — Jinja2 templates for HTML pages
  - `base.html` — Main layout template with navbar, footer, and content block
  - Individual page templates extend base.html
- **static/** — Frontend assets
  - `css/style.css` — Consistent design system with CSS variables (color palette, fonts, spacing)
  - `js/main.js` — Client-side JavaScript (currently minimal)
- **requirements.txt** — Project dependencies (Flask, pytest, pytest-flask)

### Design System

The app uses a cohesive design system defined in `static/css/style.css` with CSS variables:
- **Colors**: Ink (dark), paper (light), accent (green), accent-2 (orange), danger (red)
- **Typography**: DM Serif Display for headings, DM Sans for body
- **Spacing**: Predefined radius values (--radius-sm/md/lg)
- When modifying styles, use existing CSS variables rather than hardcoding values

### Template Hierarchy

All pages extend `base.html`, which provides:
- Navbar with branding and auth links
- Main content area (use `{% block content %}`)
- Footer with links to terms/privacy
- Load static assets and allow script blocks

## Common Development Tasks

### Running the Application

```bash
python app.py
```
The app runs on `http://localhost:5001` with debug mode enabled.

### Working with the Database

The database file is `expense_tracker.db`. When implementing database features:
1. Complete `database/db.py` with `get_db()`, `init_db()`, and `seed_db()` functions
2. Ensure SQLite connection has `row_factory` and foreign keys enabled
3. Use `CREATE TABLE IF NOT EXISTS` for schema idempotency

### Testing

```bash
pytest                    # Run all tests
pytest -v                # Verbose output
pytest tests/test_file.py  # Run specific test file
pytest tests/test_file.py::test_function  # Run specific test
```

The project uses pytest and pytest-flask. Tests should verify both happy paths and error cases.

### Adding New Routes

1. Add the route function in `app.py` with appropriate section comments
2. Create a corresponding template in `templates/` that extends `base.html`
3. Use `{{ url_for('function_name') }}` for internal links
4. Maintain the existing code comment structure (section dividers)

### Adding Templates

1. Extend `base.html` with `{% extends "base.html" %}`
2. Override `{% block content %}` for page content
3. Use semantic HTML and existing CSS classes for styling
4. Stick to the established design system (use CSS variables from style.css)

## Key Notes

- **Step-based development**: The project has placeholder routes (logout, profile, add/edit/delete expense) marked for specific implementation steps
- **Student-friendly**: Code is intentionally scaffolded with clear section comments and stubs
- **No complex frameworks**: Uses vanilla Flask, Jinja2, and plain CSS/JS (no build tools or front-end frameworks)
- **Database not yet initialized**: Students implement database setup in Step 1
