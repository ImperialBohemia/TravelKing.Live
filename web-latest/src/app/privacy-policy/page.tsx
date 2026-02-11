export const metadata = {
  title: "Privacy Protocol | TravelKing",
  description: "Operational security and data handling protocols.",
};

export default function PrivacyPage() {
  return (
    <div className="container mx-auto px-4 py-24 max-w-3xl">
      <h1 className="text-4xl md:text-6xl mb-12 font-black uppercase text-white">Privacy Protocol</h1>
      <div className="prose prose-invert prose-p:font-serif prose-headings:font-sans prose-headings:uppercase prose-headings:font-black prose-a:text-primary">
        <p><strong>Effective Date:</strong> January 1, 2026</p>
        <p>TravelKing.Live ("The System") operates with a strict data minimization policy. We do not store personal data unless explicitly provided for operational purposes.</p>

        <h3>1. Data Collection</h3>
        <p>We collect operational data (IP address, browser user agent) for security and analytics purposes via Google Analytics 4.</p>

        <h3>2. Third-Party Intelligence</h3>
        <p>This site integrates with third-party networks (Travelpayouts, Google) to provide flight data and functionality. These partners may collect data according to their own protocols.</p>

        <h3>3. Contact</h3>
        <p>For data inquiries, contact: <a href="mailto:ops@travelking.live">ops@travelking.live</a></p>
      </div>
    </div>
  );
}
