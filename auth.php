<?php
/**
 * User Authentication API
 * Handles login and session management
 */

session_start();
header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');

$USERS_FILE = __DIR__ . '/users.json';

// Get request method
$method = $_SERVER['REQUEST_METHOD'];

if ($method === 'POST') {
    // Login request
    $input = json_decode(file_get_contents('php://input'), true);
    
    if (!isset($input['username']) || !isset($input['password'])) {
        http_response_code(400);
        echo json_encode(['success' => false, 'message' => 'Username and password required']);
        exit;
    }
    
    $username = trim($input['username']);
    $password = $input['password'];
    
    // Load users
    if (!file_exists($USERS_FILE)) {
        http_response_code(500);
        echo json_encode(['success' => false, 'message' => 'Users file not found']);
        exit;
    }
    
    $usersData = json_decode(file_get_contents($USERS_FILE), true);
    
    // Find user
    $user = null;
    foreach ($usersData['users'] as $u) {
        if ($u['username'] === $username && $u['password'] === $password) {
            $user = $u;
            break;
        }
    }
    
    if ($user) {
        // Update last login
        foreach ($usersData['users'] as &$u) {
            if ($u['id'] === $user['id']) {
                $u['lastLogin'] = date('c');
                break;
            }
        }
        file_put_contents($USERS_FILE, json_encode($usersData, JSON_PRETTY_PRINT));
        
        // Set session
        $_SESSION['user_id'] = $user['id'];
        $_SESSION['username'] = $user['username'];
        $_SESSION['role'] = $user['role'];
        
        echo json_encode([
            'success' => true,
            'user' => [
                'id' => $user['id'],
                'username' => $user['username'],
                'email' => $user['email'],
                'role' => $user['role']
            ]
        ]);
    } else {
        http_response_code(401);
        echo json_encode(['success' => false, 'message' => 'Invalid username or password']);
    }
    
} elseif ($method === 'GET') {
    // Check session
    if (isset($_SESSION['user_id'])) {
        echo json_encode([
            'success' => true,
            'authenticated' => true,
            'user' => [
                'id' => $_SESSION['user_id'],
                'username' => $_SESSION['username'],
                'role' => $_SESSION['role']
            ]
        ]);
    } else {
        echo json_encode([
            'success' => true,
            'authenticated' => false
        ]);
    }
    
} elseif ($method === 'DELETE') {
    // Logout
    session_destroy();
    echo json_encode(['success' => true, 'message' => 'Logged out successfully']);
}
?>
