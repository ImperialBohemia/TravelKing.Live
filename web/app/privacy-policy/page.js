"use client";

import Navbar from "../components/Navbar";
import Footer from "../components/Footer";

export default function Privacy() {
    return (
        <main className="min-h-screen bg-black text-slate-300">
            <Navbar />
            <section className="py-32 px-6 max-w-4xl mx-auto">
                <h1 className="text-4xl font-bold text-white mb-8">Privacy Policy</h1>
                <div className="prose prose-invert prose-lg max-w-none">
                    <p className="mb-4">Effective Date: February 10, 2026</p>
                    <p className="mb-4">
                        TravelKing.Live ("we", "us", or "our") is committed to protecting your privacy. This Privacy Policy explains how we collect, use, and share your personal information when you visit our website or use our services.
                    </p>
                    <h2 className="text-2xl font-bold text-white mt-8 mb-4">1. Information We Collect</h2>
                    <p className="mb-4">
                        We collect information you provide directly to us, such as when you submit a flight compensation claim or contact us for concierge services. This may include your name, email address, flight details, and payment information.
                    </p>
                    <h2 className="text-2xl font-bold text-white mt-8 mb-4">2. Cookies and Tracking</h2>
                    <p className="mb-4">
                        We use cookies to improve your experience. By using our site, you consent to our use of cookies in accordance with our Cookie Policy. We use local storage to remember your cookie preferences.
                    </p>
                    <h2 className="text-2xl font-bold text-white mt-8 mb-4">3. Data Usage</h2>
                    <p className="mb-4">
                        We use your data solely for the purpose of processing your requests (e.g., flight search, compensation claims) and improving our platform. We do not sell your personal data to third parties.
                    </p>
                    <h2 className="text-2xl font-bold text-white mt-8 mb-4">4. Contact Us</h2>
                    <p className="mb-4">
                        If you have any questions about this Privacy Policy, please contact our Data Protection Officer at legal@travelking.live.
                    </p>
                </div>
            </section>
            <Footer />
        </main>
    );
}
