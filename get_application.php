<?php
/**
 * Get Single Application API
 * Returns the full details of a specific application
 */

header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');

$APPLICATIONS_DIR = __DIR__ . '/applications';

try {
    if (!isset($_GET['file'])) {
        throw new Exception('No file specified');
    }

    $filename = basename($_GET['file']); // Prevent directory traversal
    $filepath = $APPLICATIONS_DIR . '/' . $filename;

    if (!file_exists($filepath)) {
        throw new Exception('Application not found');
    }

    if (!is_file($filepath) || pathinfo($filepath, PATHINFO_EXTENSION) !== 'json') {
        throw new Exception('Invalid file');
    }

    $content = file_get_contents($filepath);
    if ($content === false) {
        throw new Exception('Failed to read application file');
    }

    $data = json_decode($content, true);
    if ($data === null) {
        throw new Exception('Invalid JSON data');
    }

    // Add filename to the data
    $data['_filename'] = $filename;

    echo json_encode([
        'success' => true,
        'application' => $data
    ]);

} catch (Exception $e) {
    error_log("Get application error: " . $e->getMessage());
    http_response_code(400);
    echo json_encode([
        'success' => false,
        'message' => $e->getMessage()
    ]);
}
?>
