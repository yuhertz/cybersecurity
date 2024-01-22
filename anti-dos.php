<?php
// Function to check if an IP is in the blacklist
function isIPBanned($ip) {
    $blacklistFile = 'blacklist.txt';
    $blacklistedIPs = file($blacklistFile, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
    
    return in_array($ip, $blacklistedIPs);
}

// Function to add an IP to the blacklist
function addToBlacklist($ip) {
    $blacklistFile = 'blacklist.txt';
    
    // Check if the IP is not already in the blacklist
    if (!isIPBanned($ip)) {
        // Open the file in append mode and add the IP
        file_put_contents($blacklistFile, $ip . "\n", FILE_APPEND);
    }
}

// Example usage
$ipToBan = $_SERVER['REMOTE_ADDR'];

// Check if the IP is banned
if (isIPBanned($ipToBan)) {
    // Display an error message or perform a redirect
    die("Access Denied. Your IP is banned.");
}

// Your regular PHP code goes here

// Example: Ban an IP (uncomment the line below to add the current IP to the blacklist)
// addToBlacklist($ipToBan);
?>

<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <link rel="stylesheet" href="style.css" />
  <title>Anti DoS Website</title>
</head>

<body>
  <h1>
    Anti DoS(Denial Of Service) Website
  </h1>
  <p>
    This Website is protected by an Anti DoS System.
  </p>
</body>

</html>
