# Secondary Axes

Secondary axes display an alternative scale or transformation of the same data, useful for showing different units or transformations.

## secondary_xaxis / secondary_yaxis

Unlike `twinx()`/`twiny()` which create independent axes for different data, secondary axes transform the same data to a different scale.

### Basic Usage

```python
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

x = np.linspace(0, 100, 100)
y = np.sin(x * np.pi / 50)

ax.plot(x, y)
ax.set_xlabel('Distance (km)')

# Secondary axis showing same data in miles
def km_to_miles(x):
    return x * 0.621371

def miles_to_km(x):
    return x / 0.621371

secax = ax.secondary_xaxis('top', functions=(km_to_miles, miles_to_km))
secax.set_xlabel('Distance (miles)')

plt.show()
```

### Temperature Conversion

```python
fig, ax = plt.subplots()

temp_c = np.linspace(-40, 100, 100)
y = np.exp(-temp_c / 50)

ax.plot(temp_c, y)
ax.set_xlabel('Temperature (°C)')
ax.set_ylabel('Value')

# Secondary axis in Fahrenheit
def c_to_f(x):
    return x * 9/5 + 32

def f_to_c(x):
    return (x - 32) * 5/9

secax = ax.secondary_xaxis('top', functions=(c_to_f, f_to_c))
secax.set_xlabel('Temperature (°F)')

plt.show()
```

## Secondary Y-Axis

```python
fig, ax = plt.subplots()

x = np.linspace(0, 10, 100)
y = x ** 2

ax.plot(x, y)
ax.set_ylabel('Energy (Joules)')

# Secondary axis showing same energy in calories
def j_to_cal(x):
    return x / 4.184

def cal_to_j(x):
    return x * 4.184

secax = ax.secondary_yaxis('right', functions=(j_to_cal, cal_to_j))
secax.set_ylabel('Energy (calories)')

plt.show()
```

## Logarithmic Secondary Axis

```python
fig, ax = plt.subplots()

x = np.linspace(1, 100, 100)
ax.plot(x, x ** 2)
ax.set_xlabel('Frequency (Hz)')
ax.set_yscale('log')

# Secondary axis in decades
def hz_to_decades(x):
    return np.log10(x)

def decades_to_hz(x):
    return 10 ** x

secax = ax.secondary_xaxis('top', functions=(hz_to_decades, decades_to_hz))
secax.set_xlabel('Frequency (decades)')

plt.show()
```

## Comparison: Secondary vs Twin Axes

| Feature | Secondary Axes | Twin Axes |
|---------|----------------|-----------|
| Data | Same data, different units | Different data |
| Scaling | Mathematical transformation | Independent |
| Method | `secondary_xaxis()` | `twinx()` |
| Alignment | Automatically aligned | Manual alignment |
| Use case | Unit conversion | Overlay different variables |

### When to Use Each

**Secondary Axes:**
- Same measurement in different units (km ↔ miles)
- Same scale with transformation (linear ↔ log)
- Wavelength and frequency

**Twin Axes:**
- Price and volume on same chart
- Temperature and humidity
- Different physical quantities

## Practical Examples

### 1. Wavelength and Frequency

```python
fig, ax = plt.subplots()

wavelength = np.linspace(400, 700, 100)  # nm
intensity = np.exp(-((wavelength - 550) ** 2) / 5000)

ax.plot(wavelength, intensity)
ax.set_xlabel('Wavelength (nm)')
ax.set_ylabel('Intensity')

# Frequency = c / wavelength
c = 3e8  # m/s

def wavelength_to_freq(wl):
    return c / (wl * 1e-9) / 1e12  # THz

def freq_to_wavelength(f):
    return c / (f * 1e12) / 1e-9  # nm

secax = ax.secondary_xaxis('top', functions=(wavelength_to_freq, freq_to_wavelength))
secax.set_xlabel('Frequency (THz)')

plt.show()
```

### 2. Pressure Units

```python
fig, ax = plt.subplots()

altitude = np.linspace(0, 50000, 100)  # meters
pressure = 101325 * np.exp(-altitude / 8500)  # Pa

ax.plot(altitude / 1000, pressure / 1000)
ax.set_xlabel('Altitude (km)')
ax.set_ylabel('Pressure (kPa)')

# Secondary in atmospheres
def kpa_to_atm(x):
    return x / 101.325

def atm_to_kpa(x):
    return x * 101.325

secax = ax.secondary_yaxis('right', functions=(kpa_to_atm, atm_to_kpa))
secax.set_ylabel('Pressure (atm)')

plt.show()
```

### 3. Date and Day Number

```python
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from datetime import datetime, timedelta

fig, ax = plt.subplots()

# Data for one year
start = datetime(2024, 1, 1)
days = np.arange(0, 365)
dates = [start + timedelta(days=int(d)) for d in days]
values = np.sin(days * 2 * np.pi / 365)

ax.plot(days, values)
ax.set_xlabel('Day of Year')
ax.set_ylabel('Value')

plt.show()
```

## Key Parameters

| Parameter | Description |
|-----------|-------------|
| `location` | 'top', 'bottom', 'left', or 'right' |
| `functions` | Tuple of (forward, inverse) functions |
| `transform` | Alternative to functions |

## Common Pitfalls

### 1. Inverse Function Required

```python
# Both forward AND inverse functions needed
def forward(x):
    return x * 2

def inverse(x):
    return x / 2

# CORRECT
secax = ax.secondary_xaxis('top', functions=(forward, inverse))

# WRONG: Missing inverse
# secax = ax.secondary_xaxis('top', functions=(forward,))
```

### 2. Non-Monotonic Transforms

Secondary axes work best with monotonic transformations. Non-monotonic transforms may produce unexpected results.

### 3. Log Scale Interactions

When using log scales, ensure transformations handle the log space correctly.
