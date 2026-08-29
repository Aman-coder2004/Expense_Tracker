# Spec: Registration

## Overview
Implement the user registration flow, allowing new users to create an account with a name, email, and password.
On success the user is shown the success message and redirected to the main page. This is the first step in establishing user identity for the Spendly expense tracker, enabling personalized expense tracking.

## Depends on
- 01 Database Setup

## Routes
- `POST /register` — Handle registration form submission, validate inputs, hash passwords, and create user record — public

## Database changes
No database changes. Uses the existing `users` table defined in Step 01.

## Templates
- **Modify:** `templates/register.html` — Ensure it correctly displays inline error messages passed from the backend.

## Files to change
- `app.py` — Implement the POST handler for `/register`.

## Files to create
No new files.

## New dependencies
No new dependencies.

## Rules for implementation
- No SQLAlchemy or ORMs
- Parameterised queries only
- Passwords hashed with werkzeug
- Use CSS variables — never hardcode hex values
- All templates extend `base.html`

## Definition of done
- [ ] Submitting the registration form with valid data creates a user in the `users` table.
- [ ] Submitting a duplicate email returns a clear error message on the registration page.
- [ ] Missing required fields (name, email, password) returns a validation error.
- [ ] Passwords are stored as hashes, not plain text.
- [ ] Successful registration redirects the user to the login page with a success message.
