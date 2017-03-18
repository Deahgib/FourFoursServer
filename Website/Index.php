
<!DOCTYPE html>
<html>
<head>
    <title><?php echo "TESTING"; ?></title>
	<meta charset="utf-8" />
</head>
<body>

<?php
/**
 * Simple example of extending the SQLite3 class and changing the __construct
 * parameters, then using the open method to initialize the DB.
 */

echo "£";

echo "$";
$db = new SQLite3('game-results.db');
echo "!";
$result = $db->query('SELECT * FROM results');
echo "~";

echo "<table>";
echo "<tr><th>Target</th><th>Solution</th></tr>";
while ($row = $result->fetchArray()) {
    
	echo "<tr>";
	echo "<td>{$row["target"]}</td>";
	echo "<td>{$row["solution"]}</td>";
	echo "</tr>";
}
echo "</table>";
echo "#";
?>

</body>
</html>
