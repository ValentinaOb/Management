<?php
$servername = "your_server";
$username = "your_username";
$dbname = "andr_user";

// Create connection
$conn = new mysqli($servername, $username, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Get POST data
$username = $_POST['username'];
$email = $_POST['email'];
//$password = password_hash($_POST['password'], PASSWORD_BCRYPT); // Encrypt password

// Check if user already exists
$sql = "SELECT * FROM andr_users WHERE email='$email'";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    echo json_encode(["status" => "error", "message" => "User already exists"]);
} else {
    $sql = "INSERT INTO andr_users (username, email, password) VALUES ('$username', '$email')";
    if ($conn->query($sql) === TRUE) {
        echo json_encode(["status" => "success", "message" => "User registered"]);
    } else {
        echo json_encode(["status" => "error", "message" => "Registration failed"]);
    }
}

$conn->close();
?>
