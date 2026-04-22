<h1>Spotify Data Analyis Application - Group 27</h1>
<h2>Overview</h2>
    <p>This application allows users to explore and analyse a dataset of songs using both graphical visualisations and numerical summaries. It provides an interactive menu system where users can investigate relationships between song attributes and identify trends or averages.</p>
    <p></p>
    <h3>Libraries</h3>
        <p>The system is built in Python using the following libraries:</p>
        <ul>
            <li><a href="https://pandas.pydata.org/">pandas</a> for data handling</li>
            <li><a href="https://matplotlib.org/">matplotlib</a> for visualisation</li>
            <li><a href="https://numpy.org/">numpy</a> for calculations</li>
        </ul>

<h2>Functionality</h2>
    <p>The application allows users to:</p>
    <ul>
        <li>Visualise relationships between variables using graphs</li>
        <li>View numerical summaries such as averages and correlations</li>
        <li>Filter and select specific dataset columns for analysis</li>
        <li>Identify trends and patterns in song characteristics</li>
        <li>Generate insights into how different musical features relate to one another</li>
    </ul>

<h2>Requirements</h2>
    <ol>
        <li>A user-friendly menu that allows for easy operation of the application</li>
        <li>User selects whether to make a 'trend-based' or 'average-based' enquiry in to the data set</li>
 </ol>
 <p>The system's next processes vary depending on the users selection: </p>
    <h3>Trend-Based Enquiry</h3> 
        <p>If a 'trend-based' enquiry is selected, the system completes the following tasks:</p>
        <ol>
        <li>Displays a list of available columns (excluding non-relevant metadata)</li>
        <li>Prompts the user to input two column names</li>
        <li>Validates the input to ensure both columns exist in the dataset</li>
        <li>Displays the selected data</li>
        <li>Generates a scatter plot showing the relationship between the two variables</li>
        <li>Calculates and overlays a line of best fit (trend line) using linear regression</li>
        <li>Labels and formats the graph for clarity</li>
        </ol>
        <p>This allows users to visually assess correlations between variables.</p>
    <h3>Average-Based Enquiry</h3>
        <p>If an 'average-based' enquiry is selected, the system completes the following tasks:</p>
        <ol>
        <li>Displays available columns</li>
        <li>Prompts the user to input two column names</li>
        <li>Validates the input</li>
        <li>Calculates the mean (average) of both columns</li>
        <li>Displays the results numerically</li>
        <li>Generates a bar chart comparing the average values</li>
        </ol>
        <p>This enables users to quickly compare different attributes.</p>

<h2>How to Run</h2>
<p>Follow these steps to set up and run the application:</p>
<h3>1. Prepare the Files</h3>
<ul>
    <li>Ensure the following files are in the same folder:
        <ul>
            <li><code>src.py</code> (the program file)</li>
            <li><code>dataset.csv</code> (the dataset)</li>
        </ul>
    </li>
    <li>Check that the dataset contains the required columns (e.g. popularity, genre, tempo, energy, etc.)</li>
</ul>
<h3>2. Install Required Libraries</h3>
<p>Make sure Python is installed on your system. Then install the required libraries if you do not already have them:</p>
<pre><code>pip install pandas matplotlib numpy</code></pre>
<h3>3. Run the Program</h3>
<p>Open a terminal or command prompt, navigate to the folder containing the files, and run:</p>
<pre><code>python main.py</code></pre>
<h3>4. Use the Menu</h3>
<p>Once the program starts, a menu will appear:</p>
<ol>
    <li>Trend-Based Enquiry</li>
    <li>Average-Based Enquiry</li>
    <li>Create a Custom Query</li>
    <li>Exit</li>
</ol>
<ul>
    <li>Enter the number corresponding to your choice</li>
    <li>Follow the prompts to input column names</li>
    <li>Ensure column names are typed exactly as shown (case-sensitive)</li>
</ul>
<h3>5. View Results</h3>
<ul>
    <li>Graphs will open in a new window</li>
    <li>Numerical results will be displayed in the terminal</li>
    <li>After completing an action, you will return to the main menu</li>
</ul>
<h3>6. Exit the Program</h3>
<p>Select option <strong>4</strong> from the menu to safely exit the application.</p>

<h2>Queries</h2>
    <ol>
        <li>Is there a most popular genre?</li>
        <li>Does the acousticness affect the danceability?</li>
        <li>Does the tempo of a song affect the popularity?</li>
        <li>Is there a genre with the longest/shortest songs?</li>
        <li>Does the loudness affect the energy of the song?</li>
        <li>How does the liveness affect the popularity?</li>
        <li>Does energy affect danceability?</li>
        <li>Does the key of the song affect the energy?</li>
        <li>Does the length of the song affect the popularity?</li>
        <li>Are faster songs more danceable?</li>
        <li>Do explicit songs have more energy?</li>
        <li>Are longer songs more or less danceable?</li>
        <li>Does the key of a song affect the popularity?</li>
        <li>Are explicit songs louder than others?</li>
    </ol>

<h2>Individual Data Visualisation</h2>
<h4>Daisy Farrow</h4>
<h5>Reference: <code>/DaisyFarrow-visualisation/DaisyFarrow-visualisation.py</code></h5>
<p>The system automatically outputs the visualisations as a scatter plot for query 3 (displaying the relationship between tempo and popularity) and a bar chart for query 4 (showing the average length of each song in seconds for each genre) and a list for each genre and their average for query 4.</p>
<h4>Millie McVey</h4>
<h5>Reference: <code>/MillieMcVey-visualisation/MillieMcVey-visualisation.py</code></h5>
<p>The system automatically produces two visualisations: a bar chart for query 1, and a scatter plot for query 8. The bar chart displays the average popularity for each genre, and the scatter plot displays the relationship between the key and the energy of the songs in the dataset </p>

<h2>Limitations</h2>
<ul>
    <li>Column names are case-sensitive and must be entered exactly</li>
    <li>Missing values are removed automatically during analysis</li>
    <li>Large datasets are sampled (e.g. 500 rows) for performance in visualisations</li>
    <li>The system relies on correct dataset formatting (CSV file with appropriate columns)</li>
</ul>
