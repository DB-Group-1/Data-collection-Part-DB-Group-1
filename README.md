# Data-collection-Part-DB-Group-1

## Data Crawling

We used web crawling to collect data for use in the project on **Tving**. The data includes information about movies, dramas, broadcast programs, and more, with the following fields:

- `content_id`  
- `content_name`  
- `limit_age`  
- `production_date`  
- `url`  
- `img_url`  
- `category`  
- `introduction`  
- `cast`  
- `cast_role`  
- `genre`  
- `uploaded_date`  
- `running_time`  

### Tools Used

We utilized **Python** and the following libraries for automation and data extraction:
- **Selenium**: For browser automation.
- **WebDriver_Manager**: To manage and configure the browser driver.

### Results

- Collected data for approximately **200 streaming programs** and **240 movies**.
- Organized data into **CSV files** following a predefined schema.

### Limitations

Due to restrictions, we couldn’t access user-specific information directly from the browser. Instead, we created an **arbitrary dataset** to supplement our analysis.  

---

## Source Code and Results

### Code Overview
The Python scripts we developed perform the following tasks:
1. Navigate Tving pages automatically.
2. Extract relevant information, including:
   - Images
   - Titles
   - Categories
   - Additional metadata
3. Save the scraped data into structured **CSV files** and **text files**.

### Results
The final datasets are saved as CSV files with clean and structured data, ready for analysis and further processing.

---

For detailed implementation, refer to the source code in this repository.
