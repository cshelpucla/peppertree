<?php
header('Content-Type: application/json');

// Enable error reporting for debugging (remove in production)
error_reporting(E_ALL);
ini_set('display_errors', 0);

// Function to sanitize input
function sanitizeInput($data) {
    $data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data);
    return $data;
}

// Check if form was submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get and sanitize form data
    $name = sanitizeInput($_POST['name'] ?? '');
    $email = sanitizeInput($_POST['email'] ?? '');
    $phone = sanitizeInput($_POST['phone'] ?? '');
    $unit = sanitizeInput($_POST['unit'] ?? 'No Preference');
    $notes = sanitizeInput($_POST['notes'] ?? 'None');
    
    // Get time slot data
    $date1 = sanitizeInput($_POST['date1'] ?? '');
    $time1_hour = sanitizeInput($_POST['time1_hour'] ?? '');
    $time1_period = sanitizeInput($_POST['time1_period'] ?? '');
    
    $date2 = sanitizeInput($_POST['date2'] ?? '');
    $time2_hour = sanitizeInput($_POST['time2_hour'] ?? '');
    $time2_period = sanitizeInput($_POST['time2_period'] ?? '');
    
    $date3 = sanitizeInput($_POST['date3'] ?? '');
    $time3_hour = sanitizeInput($_POST['time3_hour'] ?? '');
    $time3_period = sanitizeInput($_POST['time3_period'] ?? '');
    
    // Validate required fields
    if (empty($name) || empty($email) || empty($phone) || empty($date1) || empty($time1_hour) || empty($time1_period)) {
        echo json_encode(['success' => false, 'message' => 'Please fill in all required fields.']);
        exit;
    }
    
    // Validate email format
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        echo json_encode(['success' => false, 'message' => 'Invalid email format.']);
        exit;
    }
    
    // Format time slots
    $timeSlots = [];
    
    // First choice (required)
    if ($date1 && $time1_hour && $time1_period) {
        $formattedDate1 = date('l, F j, Y', strtotime($date1));
        $timeSlots[] = "1st Choice: {$formattedDate1} at {$time1_hour}:00 {$time1_period}";
    }
    
    // Second choice (optional)
    if ($date2 && $time2_hour && $time2_period) {
        $formattedDate2 = date('l, F j, Y', strtotime($date2));
        $timeSlots[] = "2nd Choice: {$formattedDate2} at {$time2_hour}:00 {$time2_period}";
    }
    
    // Third choice (optional)
    if ($date3 && $time3_hour && $time3_period) {
        $formattedDate3 = date('l, F j, Y', strtotime($date3));
        $timeSlots[] = "3rd Choice: {$formattedDate3} at {$time3_hour}:00 {$time3_period}";
    }
    
    $timeSlotsText = implode("\n", $timeSlots);
    
    // Format unit preference
    $unitText = $unit ?: 'No Preference';
    if ($unit == '720c') {
        $unitText = 'Unit 720C - 3BR Premium';
    } elseif ($unit == '161d') {
        $unitText = 'Unit 161D - 3BR Great Value';
    } elseif ($unit == '151a') {
        $unitText = 'Unit 151A - 3BR Prime Location';
    }
    
    // Email details
    $to = "rent@peppertreetownhomes.com";
    $subject = "New Tour Schedule Request - {$name}";
    
    // Email body
    $message = "New Tour Schedule Request\n\n";
    $message .= "Contact Information:\n";
    $message .= "------------------------\n";
    $message .= "Name: {$name}\n";
    $message .= "Email: {$email}\n";
    $message .= "Phone: {$phone}\n\n";
    
    $message .= "Tour Details:\n";
    $message .= "------------------------\n";
    $message .= "Unit Interest: {$unitText}\n\n";
    
    $message .= "Preferred Time Slots:\n";
    $message .= "------------------------\n";
    $message .= $timeSlotsText . "\n\n";
    
    if (!empty($notes) && $notes != 'None') {
        $message .= "Additional Notes:\n";
        $message .= "------------------------\n";
        $message .= $notes . "\n\n";
    }
    
    $message .= "------------------------\n";
    $message .= "Submitted: " . date('F j, Y g:i A') . "\n";
    
    // Email headers
    $headers = "From: PepperTree Townhomes <noreply@peppertreetownhomes.com>\r\n";
    $headers .= "Reply-To: {$email}\r\n";
    $headers .= "X-Mailer: PHP/" . phpversion() . "\r\n";
    $headers .= "MIME-Version: 1.0\r\n";
    $headers .= "Content-Type: text/plain; charset=UTF-8\r\n";
    
    // Create appointments directory if it doesn't exist
    $appointmentsDir = __DIR__ . '/appointments';
    if (!file_exists($appointmentsDir)) {
        mkdir($appointmentsDir, 0755, true);
    }
    
    // Generate unique appointment ID
    $appointmentId = uniqid('apt_', true);
    $timestamp = date('Y-m-d H:i:s');
    
    // Prepare appointment data for JSON storage
    $appointmentData = [
        'id' => $appointmentId,
        'submitted_at' => $timestamp,
        'contact' => [
            'name' => $name,
            'email' => $email,
            'phone' => $phone
        ],
        'tour_details' => [
            'unit' => $unit,
            'unit_text' => $unitText
        ],
        'time_slots' => [],
        'notes' => $notes,
        'status' => 'pending'
    ];
    
    // Add time slots to appointment data
    if ($date1 && $time1_hour && $time1_period) {
        $appointmentData['time_slots'][] = [
            'priority' => 1,
            'date' => $date1,
            'time_hour' => $time1_hour,
            'time_period' => $time1_period,
            'formatted' => date('l, F j, Y', strtotime($date1)) . " at {$time1_hour}:00 {$time1_period}"
        ];
    }
    
    if ($date2 && $time2_hour && $time2_period) {
        $appointmentData['time_slots'][] = [
            'priority' => 2,
            'date' => $date2,
            'time_hour' => $time2_hour,
            'time_period' => $time2_period,
            'formatted' => date('l, F j, Y', strtotime($date2)) . " at {$time2_hour}:00 {$time2_period}"
        ];
    }
    
    if ($date3 && $time3_hour && $time3_period) {
        $appointmentData['time_slots'][] = [
            'priority' => 3,
            'date' => $date3,
            'time_hour' => $time3_hour,
            'time_period' => $time3_period,
            'formatted' => date('l, F j, Y', strtotime($date3)) . " at {$time3_hour}:00 {$time3_period}"
        ];
    }
    
    // Save appointment to JSON file
    $appointmentFile = $appointmentsDir . '/' . $appointmentId . '.json';
    $jsonSaved = file_put_contents($appointmentFile, json_encode($appointmentData, JSON_PRETTY_PRINT));
    
    // Send email
    $mailSent = mail($to, $subject, $message, $headers);
    
    if ($mailSent || $jsonSaved) {
        // Also send confirmation email to the applicant
        $confirmSubject = "Tour Request Received - PepperTree Townhomes";
        $confirmMessage = "Dear {$name},\n\n";
        $confirmMessage .= "Thank you for your interest in PepperTree Townhomes!\n\n";
        $confirmMessage .= "We have received your tour schedule request with the following details:\n\n";
        $confirmMessage .= "Preferred Time Slots:\n";
        $confirmMessage .= $timeSlotsText . "\n\n";
        $confirmMessage .= "Unit Interest: {$unitText}\n\n";
        $confirmMessage .= "We will review your preferred times and contact you shortly to confirm your appointment.\n\n";
        $confirmMessage .= "If you have any questions, please call us at (559) 935-2200 or reply to this email.\n\n";
        $confirmMessage .= "Best regards,\n";
        $confirmMessage .= "PepperTree Townhomes Team\n";
        $confirmMessage .= "770 E Elm Ave, Coalinga, CA 93210\n";
        
        $confirmHeaders = "From: PepperTree Townhomes <noreply@peppertreetownhomes.com>\r\n";
        $confirmHeaders .= "Reply-To: rent@peppertreetownhomes.com\r\n";
        $confirmHeaders .= "X-Mailer: PHP/" . phpversion() . "\r\n";
        $confirmHeaders .= "MIME-Version: 1.0\r\n";
        $confirmHeaders .= "Content-Type: text/plain; charset=UTF-8\r\n";
        
        mail($email, $confirmSubject, $confirmMessage, $confirmHeaders);
        
        echo json_encode([
            'success' => true, 
            'message' => 'Your tour request has been submitted successfully! We will contact you shortly to confirm your appointment.',
            'appointment_id' => $appointmentId
        ]);
    } else {
        echo json_encode([
            'success' => false, 
            'message' => 'There was an error sending your request. Please try again or call us at (559) 935-2200.'
        ]);
    }
} else {
    echo json_encode(['success' => false, 'message' => 'Invalid request method.']);
}
?>
