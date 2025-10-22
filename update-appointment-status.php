<?php
header('Content-Type: application/json');

// Enable error reporting for debugging
error_reporting(E_ALL);
ini_set('display_errors', 0);

// Get JSON input
$input = json_decode(file_get_contents('php://input'), true);

$appointmentId = $input['id'] ?? '';
$newStatus = $input['status'] ?? '';

if (empty($appointmentId) || empty($newStatus)) {
    echo json_encode(['success' => false, 'message' => 'Missing required parameters.']);
    exit;
}

// Validate status
$validStatuses = ['pending', 'confirmed', 'completed', 'cancelled'];
if (!in_array($newStatus, $validStatuses)) {
    echo json_encode(['success' => false, 'message' => 'Invalid status value.']);
    exit;
}

$appointmentFile = __DIR__ . '/appointments/' . $appointmentId . '.json';

if (!file_exists($appointmentFile)) {
    echo json_encode(['success' => false, 'message' => 'Appointment not found.']);
    exit;
}

// Read current appointment data
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

// Update status
$appointment['status'] = $newStatus;
$appointment['status_updated_at'] = date('Y-m-d H:i:s');

// Save updated appointment
$saved = file_put_contents($appointmentFile, json_encode($appointment, JSON_PRETTY_PRINT));

if ($saved === false) {
    echo json_encode(['success' => false, 'message' => 'Error saving appointment.']);
    exit;
}

echo json_encode(['success' => true, 'message' => 'Status updated successfully.']);
?>
