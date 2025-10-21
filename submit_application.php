<?php
/**
 * Rental Application Submission Handler
 * Works on any standard web server with PHP support
 * Saves applications as JSON files - No email, no dependencies
 */

// Prevent output buffering issues
ob_start();

// Set headers first
header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: POST, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type');

// Handle preflight OPTIONS request
if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(200);
    ob_end_clean();
    exit;
}

// Only accept POST requests
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    ob_end_clean();
    echo json_encode(['success' => false, 'message' => 'Method not allowed. POST requests only.']);
    exit;
}

// Configuration - No dependencies, just file storage
$SUBMISSIONS_DIR = __DIR__ . '/applications';

// Disable error display, log instead
error_reporting(E_ALL);
ini_set('display_errors', 0);
ini_set('log_errors', 1);

try {
    // Get POST data
    $input = file_get_contents('php://input');
    
    if (empty($input)) {
        throw new Exception('No data received');
    }
    
    $data = json_decode($input, true);
    
    if (json_last_error() !== JSON_ERROR_NONE) {
        throw new Exception('Invalid JSON: ' . json_last_error_msg());
    }
    
    // Add server metadata
    $data['submittedAt'] = date('c'); // ISO 8601 format
    $data['submittedFrom'] = $_SERVER['REMOTE_ADDR'] ?? 'Unknown';
    $data['userAgent'] = $_SERVER['HTTP_USER_AGENT'] ?? 'Unknown';
    $data['serverTime'] = time();
    
    // Create submissions directory if it doesn't exist
    if (!is_dir($SUBMISSIONS_DIR)) {
        if (!mkdir($SUBMISSIONS_DIR, 0755, true)) {
            throw new Exception('Failed to create applications directory');
        }
    }
    
    // Generate unique filename
    $timestamp = date('Ymd_His');
    $firstName = isset($data['firstName']) ? preg_replace('/[^a-zA-Z0-9]/', '_', $data['firstName']) : 'Unknown';
    $lastName = isset($data['lastName']) ? preg_replace('/[^a-zA-Z0-9]/', '_', $data['lastName']) : 'Unknown';
    $filename = $timestamp . '_' . $firstName . '_' . $lastName . '.json';
    $filepath = $SUBMISSIONS_DIR . '/' . $filename;
    
    // Ensure unique filename (in case of simultaneous submissions)
    $counter = 1;
    while (file_exists($filepath)) {
        $filename = $timestamp . '_' . $firstName . '_' . $lastName . '_' . $counter . '.json';
        $filepath = $SUBMISSIONS_DIR . '/' . $filename;
        $counter++;
    }
    
    // Save to JSON file with pretty print
    $json_data = json_encode($data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
    
    if ($json_data === false) {
        throw new Exception('Failed to encode JSON: ' . json_last_error_msg());
    }
    
    $bytes_written = file_put_contents($filepath, $json_data, LOCK_EX);
    
    if ($bytes_written === false) {
        throw new Exception('Failed to write application file');
    }
    
    // Optional: Log to server error log (if configured)
    error_log("Rental application saved: $filename");
    
    // Clean output buffer and send success response
    ob_end_clean();
    http_response_code(200);
    echo json_encode([
        'success' => true,
        'message' => 'Application submitted successfully',
        'filename' => $filename,
        'timestamp' => $data['submittedAt']
    ]);
    
} catch (Exception $e) {
    // Log error to server log
    error_log("Rental application error: " . $e->getMessage());
    
    // Clean output buffer and send error response
    ob_end_clean();
    http_response_code(500);
    echo json_encode([
        'success' => false,
        'message' => 'Error processing application. Please try again or contact us directly.'
    ]);
}
?>
