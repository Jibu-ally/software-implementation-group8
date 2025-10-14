# software-implementation-group8 members
GROUP MEMBERS
1)Suleiman Siyat -674039 (Program- writing)
2) Hussein Ali-674334(Input-validation-and-exceptions)
3)Ibrahim Mohammed-673931(Unit-testing)
4)Amina Mohammed-673204(Final-README- and-merging)
5)Abdirahman Hashim -674353(peer-review)
6)Kassim Mohamed-674210(Documentation)


# software-implementation-group8
# 🌡️ Digital Thermometer

A simple yet interactive **Python program** that converts temperatures from **Celsius** to **Fahrenheit**, while providing weather feedback based on the temperature entered.  

---

## 🧠 Overview

The **Digital Thermometer** helps users understand how warm or cold a day feels based on the temperature in Celsius.  
It:
- Prompts the user to input a temperature (°C).  
- Describes the weather as *hot*, *cold*, or *moderate*.  
- Converts the temperature to Fahrenheit (°F) and displays the result.

---

## ⚙️ How It Works

1. The program requests the user to enter a temperature in **Celsius**.  
2. It checks:
   - **Above 25°C** → ☀️ *Hot day*  
   - **Below 7°C** → ❄️ *Cold day*  
   - **Otherwise** → 🌤 *Moderate weather*  
3. It then converts Celsius to Fahrenheit using the formula:  
   \[
   °F = (°C × \frac{9}{5}) + 32
   \]
4. Finally, it displays the equivalent Fahrenheit value.

---

## 🧩 Code Structure

| Function | Description |
|-----------|--------------|
| `celsius_to_fahrenheit(celsius)` | Converts Celsius temperature to Fahrenheit. |
| `main()` | Handles user input, evaluates weather, and displays results. |

---

## 🚀 How to Run the Program

### **1. Requirements**
- Python 3.x installed on your computer.

### **2. Steps**
1. Save the file as `digital_thermometer.py`.  
2. Open your terminal or command prompt.  
3. Navigate to the file location:
   ```bash
   cd path/to/your/file
