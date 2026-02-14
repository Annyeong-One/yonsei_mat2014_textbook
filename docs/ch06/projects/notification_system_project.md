# Notification System Project

Build a multi-channel notification system using abstraction.

## Requirements

### Abstract NotificationChannel
- send(recipient, message)
- validate_recipient(recipient)

### Implementations
- EmailNotification
- SMSNotification  
- PushNotification
- SlackNotification

### NotificationService
- register_channel(channel)
- send_notification(recipients, message, channels)
- Sends via all registered channels

Implement this using proper abstraction!
