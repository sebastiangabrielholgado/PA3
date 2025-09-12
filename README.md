# PA-3
### Version
- Python 7.3.2 (Jupyter Notebook)

Import the pandas library into the Python code

# Problem #1: Getting a Specific row in the pandas data
> Tasks: Save your file as `Surname_Pandas-P1.py` then load the corresponding `.csv` file into a data frame named cars using pandas. Display the first five and last five rows of the resulting cars.

- For the first problem, I first imported the pandas library then extracted the content of the provided csv file which is named "cars.csv".
- I tried to experiment with some syntaxes using .iloc and .loc so that I can get the desired data in the table with the little knowledge i have about pandas
- I then remembered about the the function that prints the first and last 5 rpws. So I settled with just using the `.head()` and `.tail()` feature of pandas

# Problem#2: Use subsetting, slicing and indexing operations to extract data from the provided data
> Tasks: Display the first five rows with odd-numbered columns. Display the row that contains the ‘Model’ of ‘Mazda RX4’. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have? Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 
Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have

- For this task, I mainly used `.iloc` to get a whole row and column based on their positions
- In the other tasks, I used `.loc` to easily specify what cell that is to be printed
