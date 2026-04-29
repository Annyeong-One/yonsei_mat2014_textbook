# Notification System Project

Real-world applications often need to deliver messages through multiple channels---email, SMS, push notifications, and chat platforms like Slack. When each channel has its own sending and validation logic, abstraction lets you add new channels without modifying the code that dispatches messages. This project exercises the Abstract Base Class patterns introduced earlier in the chapter.

Build a multi-channel notification system using abstraction.

## Requirements

### Abstract NotificationChannel

Define `NotificationChannel` as an abstract base class using Python's `abc` module. It must declare two abstract methods:

- `send(recipient, message)`---Deliver the message to the given recipient via this channel. Raise an exception if delivery fails.
- `validate_recipient(recipient)`---Check that the recipient string is valid for this channel (e.g., email format, phone number format). Return `True` or `False`.

### Implementations

Each concrete class inherits from `NotificationChannel` and implements both abstract methods with channel-specific logic:

- **EmailNotification**---Validate email format, simulate sending via SMTP.
- **SMSNotification**---Validate phone number format, simulate sending via SMS gateway.
- **PushNotification**---Validate device token, simulate push delivery.
- **SlackNotification**---Validate Slack channel or user ID, simulate webhook post.

### NotificationService

- `register_channel(channel)`---Register a `NotificationChannel` instance for use.
- `send_notification(recipients, message, channels)`---Send the message to all recipients via the specified channels. Handle per-channel failures gracefully by logging the error and continuing with remaining channels.
- Sends via all registered channels if no specific channels are specified.

Use Python's `abc` module to define `NotificationChannel` as an abstract base class. Each concrete channel must implement all abstract methods. The `NotificationService` should depend only on the `NotificationChannel` interface, not on any concrete implementation.

## Exercises

**Exercise 1.** Identify the key classes and their responsibilities in this project. Draw a simple class diagram showing the inheritance and composition relationships.

??? success "Solution to Exercise 1"
    Answers will vary based on the specific project. A good answer should identify 3-5 core classes, their primary methods, and how they interact (e.g., "BankAccount has a list of Transaction objects" or "SavingsAccount inherits from BankAccount").

---

**Exercise 2.** Extend the project by adding one new feature that requires creating at least one new class. Describe the class, its methods, and how it integrates with the existing code.

??? success "Solution to Exercise 2"
    Answers will vary. A good extension should demonstrate understanding of the existing architecture, use appropriate OOP patterns (inheritance, composition, or interfaces), and include proper error handling.

