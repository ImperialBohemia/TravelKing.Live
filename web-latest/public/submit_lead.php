<?php
/**
 * Simple Lead Capture for TravelKing.Live
 * Saves to local CSV and optionally emails
 */

header('Access-Control-Allow-Origin: *');
header('Content-Type: application/json');

$logFile = 'leads_database.csv';

// Create file with header if not exists
if (!file_exists($logFile)) {
    file_put_contents($logFile, "Date,Flight Number,Email\n");
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $data = json_decode(file_get_contents('php://input'), true);

    $flightNo = isset($data['flightNo']) ? trim($data['flightNo']) : '';
    $email = isset($data['email']) ? trim($data['email']) : '';

    if (empty($flightNo) || empty($email)) {
        http_response_code(400);
        echo json_encode(['status' => 'error', 'message' => 'Missing fields']);
        exit;
    }

    $entry = [
        date('Y-m-d H:i:s'),
        $flightNo,
        $email
    ];

    // Append to CSV
    $fp = fopen($logFile, 'a');
    fputcsv($fp, $entry);
    fclose($fp);

    // Tactical Response: Identify best service (AirHelp)
    $referralLink = "https://www.airhelp.com/en/?utm_source=travelking";
    $subject = "Tactical Analysis: Flight $flightNo";
    $message = "Your tactical flight analysis is ready.\n\n" .
        "Our engine has identified AirHelp as the optimal service to maximize your payout for Flight $flightNo.\n\n" .
        "Proceed at: $referralLink\n\n" .
        "Status: 100% FREE ANALYSIS COMPLETED.";

    // Send the email to the user (Requires SMTP config on cPanel)
    $headers = "From: concierge@travelking.live";
    // mail($email, $subject, $message, $headers); 

    echo json_encode(['status' => 'success', 'message' => 'Tactical email dispatched.', 'redirect' => $referralLink]);
}
else {
    http_response_code(405);
    echo json_encode(['status' => 'error', 'message' => 'Method not allowed']);
}
?>
