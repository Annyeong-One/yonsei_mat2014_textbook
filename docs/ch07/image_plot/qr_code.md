# QR Code

Generate and visualize QR codes using the `qrcode` library.

[QR Code Video Explanation](https://www.youtube.com/watch?v=03qMfonukno)

## Installation

```bash
pip install qrcode
```

## Basic Usage

### Generate and Display QR Code

```python
import matplotlib.pyplot as plt
import qrcode

def main():
    # Make QR code image
    img = qrcode.make('https://www.youtube.com/watch?v=03qMfonukno')

    # Save QR code image as jpg
    img.save('YouTubeQRCode.jpg')

    # Show QR code image
    fig, ax = plt.subplots()
    ax.imshow(img, cmap='binary')
    ax.axis('off')
    plt.show()

if __name__ == "__main__":
    main()
```

## QR Code Content Types

### URL

```python
import matplotlib.pyplot as plt
import qrcode

url_qr = qrcode.make('https://www.example.com')

fig, ax = plt.subplots()
ax.imshow(url_qr, cmap='binary')
ax.set_title('URL QR Code')
ax.axis('off')
plt.show()
```

### Text

```python
import matplotlib.pyplot as plt
import qrcode

text_qr = qrcode.make('Hello, World! This is a QR code.')

fig, ax = plt.subplots()
ax.imshow(text_qr, cmap='binary')
ax.set_title('Text QR Code')
ax.axis('off')
plt.show()
```

### Contact Information (vCard)

```python
import matplotlib.pyplot as plt
import qrcode

vcard = """BEGIN:VCARD
VERSION:3.0
N:Doe;John
FN:John Doe
ORG:Example Inc.
TEL:+1234567890
EMAIL:john.doe@example.com
END:VCARD"""

vcard_qr = qrcode.make(vcard)

fig, ax = plt.subplots()
ax.imshow(vcard_qr, cmap='binary')
ax.set_title('vCard QR Code')
ax.axis('off')
plt.show()
```

### WiFi Connection

```python
import matplotlib.pyplot as plt
import qrcode

# WiFi QR code format: WIFI:T:WPA;S:NetworkName;P:Password;;
wifi_config = "WIFI:T:WPA;S:MyWiFiNetwork;P:MyPassword;;"
wifi_qr = qrcode.make(wifi_config)

fig, ax = plt.subplots()
ax.imshow(wifi_qr, cmap='binary')
ax.set_title('WiFi QR Code')
ax.axis('off')
plt.show()
```

## Advanced QR Code Generation

### Using QRCode Class

```python
import matplotlib.pyplot as plt
import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data('https://www.example.com')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

fig, ax = plt.subplots()
ax.imshow(img, cmap='binary')
ax.axis('off')
plt.show()
```

### Error Correction Levels

| Level | Constant | Recovery |
|-------|----------|----------|
| L | ERROR_CORRECT_L | ~7% |
| M | ERROR_CORRECT_M | ~15% |
| Q | ERROR_CORRECT_Q | ~25% |
| H | ERROR_CORRECT_H | ~30% |

```python
import matplotlib.pyplot as plt
import qrcode

data = 'https://www.example.com'

fig, axes = plt.subplots(1, 4, figsize=(16, 4))
corrections = [
    (qrcode.constants.ERROR_CORRECT_L, 'L (~7%)'),
    (qrcode.constants.ERROR_CORRECT_M, 'M (~15%)'),
    (qrcode.constants.ERROR_CORRECT_Q, 'Q (~25%)'),
    (qrcode.constants.ERROR_CORRECT_H, 'H (~30%)')
]

for ax, (level, name) in zip(axes, corrections):
    qr = qrcode.QRCode(error_correction=level, box_size=10, border=2)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image()
    ax.imshow(img, cmap='binary')
    ax.set_title(f'Error Correction: {name}')
    ax.axis('off')

plt.tight_layout()
plt.show()
```

## Custom Colors

### Colored QR Codes

```python
import matplotlib.pyplot as plt
import qrcode

qr = qrcode.QRCode(box_size=10, border=2)
qr.add_data('https://www.example.com')
qr.make(fit=True)

# Different color combinations
colors = [
    ("black", "white"),
    ("darkblue", "lightyellow"),
    ("darkgreen", "lightgray"),
    ("darkred", "white")
]

fig, axes = plt.subplots(1, 4, figsize=(16, 4))

for ax, (fill, back) in zip(axes, colors):
    img = qr.make_image(fill_color=fill, back_color=back)
    ax.imshow(img)
    ax.set_title(f'{fill} on {back}')
    ax.axis('off')

plt.tight_layout()
plt.show()
```

## Multiple QR Codes

### Grid Display

```python
import matplotlib.pyplot as plt
import qrcode

urls = [
    'https://www.google.com',
    'https://www.github.com',
    'https://www.python.org',
    'https://www.wikipedia.org'
]

fig, axes = plt.subplots(2, 2, figsize=(10, 10))

for ax, url in zip(axes.flat, urls):
    qr = qrcode.make(url)
    ax.imshow(qr, cmap='binary')
    ax.set_title(url.replace('https://www.', ''))
    ax.axis('off')

plt.tight_layout()
plt.show()
```

## Saving QR Codes

### Various Formats

```python
import qrcode

qr = qrcode.make('https://www.example.com')

# Save as different formats
qr.save('qr_code.png')
qr.save('qr_code.jpg')
qr.save('qr_code.bmp')
```

### With Custom Size

```python
import qrcode

qr = qrcode.QRCode(
    version=1,
    box_size=20,  # Larger boxes = larger image
    border=4,
)
qr.add_data('https://www.example.com')
qr.make(fit=True)

img = qr.make_image()
img.save('qr_code_large.png')
```

## QR Code Version

### Version Comparison

```python
import matplotlib.pyplot as plt
import qrcode

# More data = higher version
data_short = 'Hi'
data_long = 'This is a much longer text that requires a higher QR code version to encode properly.'

fig, axes = plt.subplots(1, 2, figsize=(10, 5))

qr_short = qrcode.make(data_short)
axes[0].imshow(qr_short, cmap='binary')
axes[0].set_title('Short Data (Low Version)')
axes[0].axis('off')

qr_long = qrcode.make(data_long)
axes[1].imshow(qr_long, cmap='binary')
axes[1].set_title('Long Data (Higher Version)')
axes[1].axis('off')

plt.tight_layout()
plt.show()
```

## Practical Example

### Business Card QR

```python
import matplotlib.pyplot as plt
import qrcode

# Create comprehensive contact QR
contact_info = """BEGIN:VCARD
VERSION:3.0
N:Smith;Jane
FN:Jane Smith
TITLE:Software Engineer
ORG:Tech Company
TEL;TYPE=WORK:+1-555-123-4567
EMAIL:jane.smith@techcompany.com
URL:https://janesmith.dev
END:VCARD"""

qr = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)
qr.add_data(contact_info)
qr.make(fit=True)
img = qr.make_image(fill_color="#2c3e50", back_color="white")

fig, ax = plt.subplots(figsize=(6, 6))
ax.imshow(img)
ax.set_title('Scan for Contact Info', fontsize=14, fontweight='bold')
ax.axis('off')
plt.tight_layout()
plt.show()
```
