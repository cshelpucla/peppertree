<?php
header('Content-Type: application/json');

// Enable error reporting for debugging
error_reporting(E_ALL);
ini_set('display_errors', 0);

$appointmentsDir = __DIR__ . '/appointments';

// Check if appointments directory exists
if (!file_exists($appointmentsDir)) {
    echo json_encode(['success' => true, 'appointments' => []]);
    exit;
}

// Get all appointment JSON files
$files = glob($appointmentsDir . '/*.json');

if (empty($files)) {
    echo json_encode(['success' => true, 'appointments' => []]);
    exit;
}

$appointments = [];

foreach ($files as $file) {
    $content = file_get_contents($file);
    if ($content) {
        $appointment = json_decode($content, true);
        if ($appointment) {
            $appointments[] = $appointment;
        }
    }
}

// Sort by submission date (newest first)
usort($appointments, function($a, $b) {
    return strtotime($b['submitted_at']) - strtotime($a['submitted_at']);
});

echo json_encode(['success' => true, 'appointments' => $appointments]);
?>
