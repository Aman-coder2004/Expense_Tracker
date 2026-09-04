---
# Spec: User Profile Design

## Overview
The User Profile page provides a dedicated space for logged-in users to view their account details. This feature transitions the app from a simple authentication flow to a personalized experience, establishing the layout for future account management features.

## Depends on
- Step 2: Registration
- Step 3: Login and Logout

## Routes
- `GET /profile` — Displays the current user's profile information (name, email, member since). Access level: logged-in.

## Database changes
No database changes. Uses the existing `users` table.

## Templates
- **Create:** `templates/profile.html` — A clean, editorial-style profile page.
- **Modify:** `templates/base.html` — Update navigation to conditionally show "Profile" vs "Sign in/Get started" based on authentication state.

## Files to change
- `app.py` — Implement the `/profile` route handler and add session-based navigation logic.
- `templates/base.html` — Update navbar.

## Files to create
- `templates/profile.html`

## New dependencies
No new dependencies.

## Rules for implementation
- No SQLAlchemy or ORMs
- Parameterised queries only
- Passwords hashed with werkzeug
- Use CSS variables — never hardcode hex values
- All templates extend `base.html`
- Ensure a redirect to `/login` occurs if an unauthenticated user attempts to access `/profile`.

## Definition of done
 []Visiting /profile without being logged in redirects to /login
 []Visiting /profile while logged in returns HTTP 200
 []The page displays a user info card with a name and email
 []The page displays at least three summary stat values (e.g. total spent, transaction count, top category)
 []The page displays a transaction history table with at least three hardcoded rows
 []The page displays a category breakdown section with at least three categories
 []The navbar shows the logged-in state (username + logout link)
 []No hex colour values appear in profile.html — only CSS variables
---
