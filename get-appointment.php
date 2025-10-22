<?php
header('Content-Type: application/json');

// Enable error reporting for debugging
error_reporting(E_ALL);
ini_set('display_errors', 0);

$appointmentId = $_GET['id'] ?? '';

if (empty($appointmentId)) {
    echo json_encode(['success' => false, 'message' => 'No appointment ID provided.']);
    exit;
}

$appointmentFile = __DIR__ . '/appointments/' . $appointmentId . '.json';

if (!file_exists($appointmentFile)) {
    echo json_encode(['success' => false, 'message' => 'Appointment not found.']);
    exit;
}

$content = file_get_contents($appointmentFile);
if (!$content) {
    echo json_encode(['success' => false, 'message' => 'Error reading appointment file.']);
    exit;
}

$appointment = json_decode($content, true);
if (!$appointment) {
    echo json_encode(['success' => false, 'message' => 'Error parsing appointment data.']);
    exit;
}

echo json_encode(['success' => true, 'appointment' => $appointment]);
?>
