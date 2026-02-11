export const metadata = {
  title: "Terms of Engagement | TravelKing",
  description: "Rules of engagement for accessing the TravelKing intelligence network.",
};

export default function TermsPage() {
  return (
    <div className="container mx-auto px-4 py-24 max-w-3xl">
      <h1 className="text-4xl md:text-6xl mb-12 font-black uppercase text-white">Terms of Engagement</h1>
      <div className="prose prose-invert prose-p:font-serif prose-headings:font-sans prose-headings:uppercase prose-headings:font-black prose-a:text-primary">
        <p>By accessing TravelKing.Live, you agree to the following operational terms.</p>

        <h3>1. Intelligence Only</h3>
        <p>All content provided is for informational purposes ("Intelligence"). It does not constitute legal advice. Verify all intel independently before execution.</p>

        <h3>2. Affiliate Protocol</h3>
        <p>We may earn a commission when you utilize our strategic partners (e.g., for flight booking or compensation claims). This funds our operations.</p>

        <h3>3. Liability</h3>
        <p>TravelKing is not liable for missed flights, denied claims, or operational failures by third-party providers.</p>
      </div>
    </div>
  );
}
