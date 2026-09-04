---
# Spec: User Profile

## Overview
The User Profile feature introduces a protected area where logged-in users can view their account information. This reinforces the concept of session-based access control and data retrieval for the currently authenticated user.

## Depends on
- Step 3: Login and Logout

## Routes
- `GET /profile` — Display the logged-in user's profile details (name, email) — access level: logged-in

## Database changes
No database changes.

## Templates
- **Create:** `templates/profile.html` — A simple, editorial-style profile page.
- **Modify:** `templates/base.html` — Update navbar to show a "Profile" link when the user is authenticated.

## Files to change
- `app.py` — Replace the placeholder `/profile` route with a functional handler that fetches user data from the database.

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
- Profile route must redirect to `/login` if `user_id` is not in session

## Definition of done
[] Visiting /profile without being logged in redirects to /login
 []Visiting /profile while logged in returns HTTP 200
 []The page displays a user info card with a name and email
 []The page displays at least three summary stat values (e.g. total spent, transaction count, top category)
 []The page displays a transaction history table with at least three hardcoded rows
 []The page displays a category breakdown section with at least three categories
 []The navbar shows the logged-in state (username + logout link)
 []No hex colour values appear in profile.html — only CSS variables
---
