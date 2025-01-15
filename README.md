# Automated Product Registration with Python

This project is a Python-based solution designed to automate the repetitive task of registering products in a system. The main goal is to reduce manual work, minimize errors, and save time when dealing with large datasets, such as a CSV file containing hundreds of product details.

## Features

- **Automated browser interaction:** Opens a specified browser and navigates to a pre-defined URL for login and product registration.
- **Dynamic data handling:** Reads product details from a CSV file and inputs them into the system.
- **Error reduction:** Ensures consistent and accurate data entry.
- **Repeatable process:** Loops through the dataset to register all products automatically.

## Technologies Used

- **Python**: The core programming language used for the automation.
- **Pandas**: For reading and handling the CSV file containing product data.
- **PyAutoGUI**: For controlling the mouse and keyboard to simulate manual interaction with the system.

## How It Works

1. **Setup**: Install required Python libraries:
   ```bash
   pip install pyautogui pandas
   ```

2. **Data Preparation**: Ensure your data is stored in a CSV file (e.g., `produtos.csv`) in the following format:

   | codigo | marca    | tipo    | categoria | preco_unitario | custo | obs           |
   |--------|----------|---------|-----------|----------------|-------|---------------|
   | 001    | Brand A  | Type X  | Category Y| 10.00          | 8.00  | Optional Note |

3. **Automation Process**:
   - Open the specified browser.
   - Navigate to the login page and authenticate.
   - Read data from the CSV file.
   - Fill in the product information fields in the system.
   - Submit the form for each product.

4. **Customization**: Adjust the positions (`x`, `y` coordinates) for mouse clicks to match your screen setup using the provided `taking_mouse_position.py` script.


## Notes

- Ensure your CSV file and Python script are in the same directory, or provide the full path to the CSV file.
- Use the `taking_mouse_position.py` script to identify and adjust the `x`, `y` coordinates for your screen.
- Test with a small subset of data before running the full automation.

## Challenges and Solutions

- **Screen Resolution Variations**: Use the position script to adapt to different screen setups.
- **Website Loading Times**: Adjust `time.sleep` as needed for slower connections or systems.
- **Data Validation**: Ensure the CSV file contains valid and complete data before running the script.

## Conclusion

This project demonstrates the power of Python for automating repetitive tasks. It significantly reduces manual effort, minimizes errors, and improves efficiency. Whether for personal projects or professional workflows, this automation serves as a foundation for further customization and scalability.

Feel free to modify and expand this project to suit your needs!

---

### Resources
- [PyAutoGUI Documentation](https://pyautogui.readthedocs.io/en/latest/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)


