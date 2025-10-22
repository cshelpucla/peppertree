<?php
/**
 * Get Single Appointment API
 * Returns the full details of a specific appointment
 */

header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');

$APPOINTMENTS_DIR = __DIR__ . '/appointments';

try {
    if (!isset($_GET['id'])) {
        throw new Exception('No appointment ID specified');
    }

    $id = $_GET['id'];
    // Sanitize the ID
    $id = preg_replace('/[^a-zA-Z0-9_-]/', '', $id);
    
    $filename = 'apt_' . $id . '.json';
    $filepath = $APPOINTMENTS_DIR . '/' . $filename;

    if (!file_exists($filepath)) {
        throw new Exception('Appointment not found');
    }

    if (!is_file($filepath) || pathinfo($filepath, PATHINFO_EXTENSION) !== 'json') {
        throw new Exception('Invalid file');
    }

    $content = file_get_contents($filepath);
    if ($content === false) {
        throw new Exception('Failed to read appointment file');
    }

    $data = json_decode($content, true);
    if ($data === null) {
        throw new Exception('Invalid JSON data');
    }

    echo json_encode([
        'success' => true,
        'appointment' => $data
    ]);

} catch (Exception $e) {
    error_log("Get appointment error: " . $e->getMessage());
    http_response_code(400);
    echo json_encode([
        'success' => false,
        'message' => $e->getMessage()
    ]);
}
?>
