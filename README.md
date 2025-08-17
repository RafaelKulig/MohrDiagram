# Mohr Circle Plotter

This Python script calculates and plots **Mohr's Circle**, a graphical method used in solid mechanics to determine the state of stress at a point, including principal stresses and maximum shear stress.

The script supports:
- Calculation of principal stresses
- Determination of the principal plane angle
- Visualization of Mohr's Circle in a plot

---

## 📦 Requirements

- Python 3.7+
- Libraries: numpy, matplotlib

```bash
pip install numpy matplotlib
```
---
## 🚀 How to Use
You can use the script in two ways: via command line arguments (CLI) or in interactive mode.

### 🔧 Command Line (CLI)
```bash
python mohr.py -sx 50 -sy 30 -txy 10
```
Where:

- sx → Normal stress in x direction (σx)
- sy → Normal stress in y direction (σy)
- txy → Shear stress (τxy)

The program will display the calculated values and show the Mohr Circle plot.

### 👤 Interactive Mode
If you run the script without arguments, it will ask you to manually input the stress values:
```bash
python mohr.py
```
And prompt:
```plaintext
Insert σx, σy and τxy separated by space:
```

## 📈 Example Output
```plaintext
Average normal stress: 40.00
Maximum shear stress: 20.00
Principal stresses:
    σ1 = 60.00
    σ2 = 20.00
Principal plane angle: 26.57°
```
A plot of Mohr's Circle will also be shown, including:

- Original stress state
- Principal stresses
- Circle center
- Visual indicators

## 📁 Project Structure
```bash
mohr_circle/
│
├── mohr.py         # Main script
├── README.md       # This file
```

## 📚 References
- Hibbeler – Mechanics of Materials
- Mohr's Circle: https://en.wikipedia.org/wiki/Mohr%27s_circle
- Norton - Machine Design

## 📄 License
This project is free to use for educational purposes.