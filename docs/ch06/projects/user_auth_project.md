# User Authentication System Project

Build a secure user authentication system using encapsulation.

## Requirements

### User Class
- Private: _username, _password_hash, _email, _failed_attempts, _is_locked
- Properties with validation for username and email
- Password is write-only
- Methods: authenticate(password), lock_account(), unlock_account()

### Session Class
- Private: _user, _token, _expiry, _is_active
- Automatic session expiration
- Secure token generation

### AuthSystem Class
- Manage users and sessions
- register_user(), login(), logout()
- Account lockout after failed attempts

Implement this system with proper encapsulation!
