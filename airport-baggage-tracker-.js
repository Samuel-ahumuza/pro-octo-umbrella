<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Baggage Tracker</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

    <div class="tracker-container">
        <h1>Airport Baggage Tracker</h1>
        <form id="tracker-form">
            <label for="baggage-id">Enter Baggage ID:</label>
            <input type="text" id="baggage-id" placeholder="e.g., XYZ12345" required>
            <button type="submit">Track My Bag</button>
        </form>
        <div id="status-display" class="status-box">
            <p id="initial-message">Please enter a Baggage ID to track your bag.</p>
        </div>
    </div>

    <script src="script.js"></script>
</body>
</html>
