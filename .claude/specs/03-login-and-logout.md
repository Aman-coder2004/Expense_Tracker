# Step 3: Login and Logout

## Goal
Implement a secure authentication system allowing users to access their personalized expense data.

## Requirements
- **Login Page**: A dedicated page with a form for email and password.
- **Authentication**: Verify user credentials against the database using secure password hashing.
- **Session Management**: Maintain user state across requests using Flask sessions.
- **Error Handling**: Provide clear feedback for missing fields or invalid credentials.
- **Logout**: A secure way to terminate the session and return to the landing page.

## Technical Specification

### 1. Database Layer (`database/db.py`)
- `get_user_by_email(email)`: Query the `users` table for a record matching the provided email.

### 2. Routing (`app.py`)
- **`/login` (GET)**: Render `login.html`.
- **`/login` (POST)**:
    - Extract `email` and `password` from `request.form`.
    - Validate that neither field is empty.
    - Retrieve user via `get_user_by_email`.
    - Verify password using `check_password_hash`.
    - On success: Set `session["user_id"]` and redirect to `/profile`.
    - On failure: Render `login.html` with an error message.
- **`/logout` (GET)**:
    - Clear `user_id` from `session`.
    - Flash a success message and redirect to `/`.

### 3. Templates
- **`login.html`**: Form posting to `/login` with fields for email and password. Supports an `error` variable for inline alerts.

## Security Considerations
- **Password Hashing**: Never store passwords in plain text. Use `werkzeug.security.generate_password_hash` during registration and `check_password_hash` during login.
- **Session Security**: Use a strong `app.secret_key` to sign session cookies.
