<?php
/**
 * User Management API
 * Handles CRUD operations for users
 */

session_start();
header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');

$USERS_FILE = __DIR__ . '/users.json';

// Check authentication
if (!isset($_SESSION['user_id']) || $_SESSION['role'] !== 'administrator') {
    http_response_code(403);
    echo json_encode(['success' => false, 'message' => 'Unauthorized access']);
    exit;
}

$method = $_SERVER['REQUEST_METHOD'];

// Load users
if (!file_exists($USERS_FILE)) {
    http_response_code(500);
    echo json_encode(['success' => false, 'message' => 'Users file not found']);
    exit;
}

$usersData = json_decode(file_get_contents($USERS_FILE), true);

if ($method === 'GET') {
    // List all users (exclude passwords)
    $users = array_map(function($user) {
        unset($user['password']);
        return $user;
    }, $usersData['users']);
    
    echo json_encode([
        'success' => true,
        'users' => $users,
        'count' => count($users)
    ]);
    
} elseif ($method === 'POST') {
    // Add new user
    $input = json_decode(file_get_contents('php://input'), true);
    
    if (!isset($input['username']) || !isset($input['password']) || !isset($input['email'])) {
        http_response_code(400);
        echo json_encode(['success' => false, 'message' => 'Username, password, and email required']);
        exit;
    }
    
    // Check if username already exists
    foreach ($usersData['users'] as $user) {
        if ($user['username'] === $input['username']) {
            http_response_code(400);
            echo json_encode(['success' => false, 'message' => 'Username already exists']);
            exit;
        }
    }
    
    // Generate new ID
    $maxId = 0;
    foreach ($usersData['users'] as $user) {
        if ((int)$user['id'] > $maxId) {
            $maxId = (int)$user['id'];
        }
    }
    $newId = (string)($maxId + 1);
    
    // Create new user
    $newUser = [
        'id' => $newId,
        'username' => trim($input['username']),
        'password' => $input['password'],
        'email' => trim($input['email']),
        'role' => $input['role'] ?? 'user',
        'createdAt' => date('c'),
        'lastLogin' => null
    ];
    
    $usersData['users'][] = $newUser;
    
    if (file_put_contents($USERS_FILE, json_encode($usersData, JSON_PRETTY_PRINT))) {
        unset($newUser['password']);
        echo json_encode([
            'success' => true,
            'message' => 'User created successfully',
            'user' => $newUser
        ]);
    } else {
        http_response_code(500);
        echo json_encode(['success' => false, 'message' => 'Failed to save user']);
    }
    
} elseif ($method === 'DELETE') {
    // Delete user
    $userId = $_GET['id'] ?? null;
    
    if (!$userId) {
        http_response_code(400);
        echo json_encode(['success' => false, 'message' => 'User ID required']);
        exit;
    }
    
    // Don't allow deleting yourself
    if ($userId === $_SESSION['user_id']) {
        http_response_code(400);
        echo json_encode(['success' => false, 'message' => 'Cannot delete your own account']);
        exit;
    }
    
    $newUsers = array_filter($usersData['users'], function($user) use ($userId) {
        return $user['id'] !== $userId;
    });
    
    if (count($newUsers) === count($usersData['users'])) {
        http_response_code(404);
        echo json_encode(['success' => false, 'message' => 'User not found']);
        exit;
    }
    
    $usersData['users'] = array_values($newUsers);
    
    if (file_put_contents($USERS_FILE, json_encode($usersData, JSON_PRETTY_PRINT))) {
        echo json_encode([
            'success' => true,
            'message' => 'User deleted successfully'
        ]);
    } else {
        http_response_code(500);
        echo json_encode(['success' => false, 'message' => 'Failed to delete user']);
    }
}
?>
