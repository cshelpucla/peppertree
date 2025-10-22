<?php
/**
 * List Appointments API
 * Returns a list of all submitted tour appointments
 */

// Prevent output buffering issues
ob_start();

header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');

$APPOINTMENTS_DIR = __DIR__ . '/appointments';

try {
    if (!is_dir($APPOINTMENTS_DIR)) {
        ob_end_clean();
        echo json_encode([
            'success' => true,
            'appointments' => [],
            'count' => 0
        ]);
        exit;
    }

    $files = glob($APPOINTMENTS_DIR . '/apt_*.json');
    
    if ($files === false || empty($files)) {
        ob_end_clean();
        echo json_encode([
            'success' => true,
            'appointments' => [],
            'count' => 0
        ]);
        exit;
    }

    $appointments = [];

    foreach ($files as $file) {
        $content = file_get_contents($file);
        if ($content === false) {
            continue;
        }

        $data = json_decode($content, true);
        if ($data === null) {
            continue;
        }

        // Only include essential fields for the list view
        // Extract ID: remove 'apt_' prefix and '.json' extension
        $filename = basename($file, '.json');
        $id = preg_replace('/^apt_/', '', $filename);
        
        $appointments[] = [
            'id' => $data['id'] ?? $id,
            'submitted_at' => $data['submitted_at'] ?? null,
            'name' => $data['contact']['name'] ?? '',
            'email' => $data['contact']['email'] ?? '',
            'phone' => $data['contact']['phone'] ?? '',
            'unit' => $data['tour_details']['unit'] ?? '',
            'unit_text' => $data['tour_details']['unit_text'] ?? '',
            'time_slots' => $data['time_slots'] ?? []
        ];
    }

    // Sort by submission date, newest first
    usort($appointments, function($a, $b) {
        $dateA = strtotime($a['submitted_at'] ?? 0);
        $dateB = strtotime($b['submitted_at'] ?? 0);
        return $dateB - $dateA;
    });

    ob_end_clean();
    echo json_encode([
        'success' => true,
        'appointments' => $appointments,
        'count' => count($appointments)
    ]);

} catch (Exception $e) {
    error_log("List appointments error: " . $e->getMessage());
    ob_end_clean();
    http_response_code(500);
    echo json_encode([
        'success' => false,
        'message' => 'Error loading appointments'
    ]);
}
?>
