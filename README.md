# Snag_CodeReview
<h2>Usage</h2>
  <p>Ensure Assignment.py is in your working directory then run:<code>python Assignment.py <i>path/to/file.csv</i> <i>column=value</i></code>from the command line.</p>
  <p>You can add as many <i>column=value</i> pairs as you'd like, provided the column referenced is in the csv, or else it will throw an error
<h2>Notes</h2>
  <ol>
    <li>Error checking is minimal. I was able to get away with this in for this code because I know it well and could pinpoint issues quickly. In production this would have to be expanded at least to account for likely breaking points</li>
    <li>Assumes a header row. It is quite possible to have an indicator parameter to tell the script if there is a header row. I chose to exclude that for ease of use and given that parameters had column names its likely that this would be used on csvs with headers</li>
    <li>In real life I would just use Pandas for this</li>
  </ol>
