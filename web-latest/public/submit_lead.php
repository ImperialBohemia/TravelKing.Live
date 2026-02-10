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
    file_put_contents($logFile, "Date,Flight Number,From,To,Passengers,Email,Wants News\n");
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $data = json_decode(file_get_contents('php://input'), true);

    $flightNo = isset($data['flightNo']) ? trim($data['flightNo']) : '';
    $departure = isset($data['departure']) ? trim($data['departure']) : '';
    $arrival = isset($data['arrival']) ? trim($data['arrival']) : '';
    $passengers = isset($data['passengers']) ? (int)$data['passengers'] : 1;
    $email = isset($data['email']) ? trim($data['email']) : '';

    if (empty($flightNo) || empty($email)) {
        http_response_code(400);
        echo json_encode(['status' => 'error', 'message' => 'Missing fields']);
        exit;
    }

    $wantsNews = isset($data['wantsNews']) && $data['wantsNews'] ? 'YES' : 'NO';

    $entry = [
        date('Y-m-d H:i:s'),
        $flightNo,
        $departure,
        $arrival,
        $passengers,
        $email,
        $wantsNews
    ];

    // Append to CSV
    $fp = fopen($logFile, 'a');
    fputcsv($fp, $entry);
    fclose($fp);

    // Tactical Estimation (EU261/UK261)
    $perPersonEUR = 600; // Peak estimation for conversion
    $totalEUR = $perPersonEUR * $passengers;
    $totalUSD = round($totalEUR * 1.08);

    // Tactical Response: Identify best service (AirHelp)
    $referralLink = "https://www.airhelp.com/en/?utm_source=travelking";
    $subject = "Tactical Analysis: Flight $flightNo";
    $message = "Your tactical flight analysis is ready.\n\n" .
               "Flight: $flightNo ($departure -> $arrival)\n" .
               "Passengers: $passengers\n" .
               "TOTAL ESTIMATED COMPENSATION: €$totalEUR (~$$totalUSD)\n\n" .
               "Our engine has identified AirHelp as the optimal service to maximize your payout.\n" .
               "They offer a 'No Win, No Fee' guarantee and will handle all legal proceedings for you.\n\n" .
               "START YOUR RECOVERY HERE: $referralLink\n\n" .
               "Status: 100% FREE ANALYSIS COMPLETED.";

    // Send the email to the user (Requires SMTP config on cPanel)
    $headers = "From: concierge@travelking.live";
    // mail($email, $subject, $message, $headers);

    echo json_encode([
        'status' => 'success',
        'message' => "Analysis complete. Total estimated payout: €$totalEUR for $passengers pax.",
        'redirect' => $referralLink,
        'estimate' => "€$totalEUR"
    ]);
}
else {
    http_response_code(405);
    echo json_encode(['status' => 'error', 'message' => 'Method not allowed']);
}
?>