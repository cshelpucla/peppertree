<?php
/**
 * List Applications API
 * Returns a list of all submitted applications
 */

// Prevent output buffering issues
ob_start();

header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');

$APPLICATIONS_DIR = __DIR__ . '/applications';

try {
    if (!is_dir($APPLICATIONS_DIR)) {
        ob_end_clean();
        echo json_encode([
            'success' => true,
            'applications' => [],
            'count' => 0
        ]);
        exit;
    }

    $files = glob($APPLICATIONS_DIR . '/*.json');
    
    if ($files === false || empty($files)) {
        ob_end_clean();
        echo json_encode([
            'success' => true,
            'applications' => [],
            'count' => 0
        ]);
        exit;
    }

    $applications = [];

    foreach ($files as $file) {
        $content = file_get_contents($file);
        if ($content === false) {
            continue;
        }

        $data = json_decode($content, true);
        if ($data === null) {
            continue;
        }

        // Add filename to the data
        $data['filename'] = basename($file);
        
        // Only include essential fields for the list view
        $applications[] = [
            'filename' => basename($file),
            'submittedAt' => $data['submittedAt'] ?? ($data['submissionDate'] ?? null),
            'firstName' => $data['firstName'] ?? '',
            'lastName' => $data['lastName'] ?? '',
            'email' => $data['email'] ?? '',
            'cellPhone' => $data['cellPhone'] ?? '',
            'homePhone' => $data['homePhone'] ?? '',
            'desiredMoveIn' => $data['desiredMoveIn'] ?? ''
        ];
    }

    // Sort by submission date, newest first
    usort($applications, function($a, $b) {
        $dateA = strtotime($a['submittedAt'] ?? 0);
        $dateB = strtotime($b['submittedAt'] ?? 0);
        return $dateB - $dateA;
    });

    ob_end_clean();
    echo json_encode([
        'success' => true,
        'applications' => $applications,
        'count' => count($applications)
    ]);

} catch (Exception $e) {
    error_log("List applications error: " . $e->getMessage());
    ob_end_clean();
    http_response_code(500);
    echo json_encode([
        'success' => false,
        'message' => 'Error loading applications'
    ]);
}
?>
