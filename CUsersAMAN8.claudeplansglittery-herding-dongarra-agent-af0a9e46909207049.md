# Implementation Plan: User Profile Page

## Overview
Implement the User Profile page (`/profile`) to provide a personalized experience for logged-in users. This includes backend route protection, database retrieval of user data, and a high-fidelity editorial-style frontend.

## Requirements
- **Route**: `GET /profile` (protected, redirects to `/login`).
- **Template**: `templates/profile.html` (extends `base.html`).
- **UI Components**:
    - User info card (Name, Email, Member since).
    - Summary stats (Total spent, transaction count, top category) - hardcoded for now.
    - Transaction history table (3+ hardcoded rows).
    - Category breakdown (3+ categories).
- **Styling**: Editorial style, using CSS variables from `static/css/style.css`.
- **Constraints**: No ORMs, parameterized queries, no hex colors.

## Step-by-Step Implementation

### 1. Database Layer Update (`database/db.py`)
- Add `get_user_by_id(user_id: int)` function.
    - Use `get_db()` to open a connection.
    - Execute `SELECT * FROM users WHERE id = ?` with `(user_id,)`.
    - Return the first result (`fetchone()`).
    - Ensure connection is closed in a `finally` block.

### 2. Route Implementation (`app.py`)
- Modify the `@app.route("/profile")` handler:
    - Check `if "user_id" not in session: return redirect(url_for("login"))`.
    - Call `get_user_by_id(session["user_id"])`.
    - Handle the case where the user might not exist (though unlikely given session logic).
    - Pass the `user` object to `render_template("profile.html", user=user)`.

### 3. Template Creation (`templates/profile.html`)
- Create the file extending `base.html`.
- Use the following structure:
    - **Page Header**: A clear "Your Profile" heading in `var(--font-display)`.
    - **User Info Card**: A card using `var(--paper-card)` displaying:
        - Name
        - Email
        - Joined Date (formatted from `user['created_at']`).
    - **Stats Grid**: A row of 3 stat tiles (similar to `.dash-stat` in `style.css`):
        - Total Spent: e.g., "₹ 45,200"
        - Transactions: e.g., "128"
        - Top Category: e.g., "Food & Dining"
    - **Transaction Table**: A styled table (`.profile-table`) with hardcoded entries:
        - Date | Category | Description | Amount
    - **Category Breakdown**: A section showing categories (e.g., Food, Transport, Shopping) with dummy percentage or amount values.

### 4. Styling (`static/css/style.css`)
- Add specific styles for the profile page.
- Reuse and extend existing design tokens:
    - Use `var(--paper-warm)` for background sections.
    - Use `var(--border)` for table borders.
    - Use `var(--accent)` for highlighting key values.
- Avoid any hardcoded hex colors.
- Ensure responsive layout (stacking cards on mobile).

### 5. Verification (Definition of Done)
- [ ] **Auth Guard**: Visit `/profile` while logged out $\rightarrow$ redirect to `/login`.
- [ ] **Access**: Visit `/profile` while logged in $\rightarrow$ HTTP 200.
- [ ] **User Data**: Verify name and email from DB are displayed correctly.
- [ ] **UI Completeness**: 
    - [ ] Info card present.
    - [ ] 3+ summary stats present.
    - [ ] 3+ hardcoded transactions in table.
    - [ ] 3+ categories listed.
- [ ] **Design Fidelity**: No hex colors in CSS/HTML; uses `var(--*)` and editorial fonts.
- [ ] **Navbar**: Verify "Profile" and "Logout" are visible when logged in.

## Critical Files for Implementation
- `database/db.py`
- `app.py`
- `templates/profile.html`
- `static/css/style.css`
