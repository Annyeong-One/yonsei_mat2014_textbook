# User Authentication System Project

Authentication systems handle sensitive data — passwords, session tokens, and account state — that must never be exposed or modified directly by external code. Encapsulation enforces these boundaries at the class level, ensuring that password hashes remain hidden, failed-attempt counters cannot be reset arbitrarily, and sessions expire automatically. This project applies the encapsulation patterns introduced earlier in the chapter.

Build a secure user authentication system using encapsulation.

## Requirements

### User Class

Private attributes (must not be accessible directly from outside the class):

- `_username` — The user's unique identifier.
- `_password_hash` — Stored hash of the password; never the plaintext.
- `_email` — The user's email address.
- `_failed_attempts` — Counter for consecutive failed login attempts.
- `_is_locked` — Whether the account is currently locked.

Properties:

- `username` — Read-only after creation.
- `email` — Validated format on set (must contain `@` and a domain).
- Password — Expose only a setter that hashes the input (e.g., using `hashlib`). No getter; the plaintext is never stored or retrievable.

Methods:

- `authenticate(password)` — Hash the input and compare to `_password_hash`. Increment `_failed_attempts` on failure and reset to zero on success. Lock the account if failures exceed the threshold (default: 3 consecutive attempts; make this configurable).
- `lock_account()` — Set `_is_locked` to `True`.
- `unlock_account()` — Set `_is_locked` to `False` and reset `_failed_attempts` to zero.

### Session Class

Private attributes:

- `_user` — The authenticated `User` instance.
- `_token` — Generated securely using `secrets.token_hex()` or similar.
- `_expiry` — Set to a configurable duration from creation time (e.g., 30 minutes).
- `_is_active` — Automatically becomes `False` when the current time exceeds `_expiry`.

Methods:

- `is_valid()` — Return `True` only if `_is_active` is `True` and the current time has not exceeded `_expiry`.

### AuthSystem Class

- `register_user(username, password, email)` — Create a new `User`, validate inputs, and store in an internal user registry. Raise an error if the username already exists.
- `login(username, password)` — Look up the user, call `authenticate()`, and create a `Session` if successful. Raise appropriate errors for locked accounts or invalid credentials.
- `logout(token)` — Invalidate the session associated with the given token.

Use Python's name-mangling (`_` prefix) and `@property` decorators to enforce encapsulation. No external code should be able to read password hashes or directly modify account lock status.
