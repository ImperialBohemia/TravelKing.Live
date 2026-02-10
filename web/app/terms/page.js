"use client";

import Navbar from "../components/Navbar";
import Footer from "../components/Footer";

export default function Terms() {
    return (
        <main className="min-h-screen bg-black text-slate-300">
            <Navbar />
            <section className="py-32 px-6 max-w-4xl mx-auto">
                <h1 className="text-4xl font-bold text-white mb-8">Terms of Service</h1>
                <div className="prose prose-invert prose-lg max-w-none">
                    <p className="mb-4">Last Updated: February 10, 2026</p>
                    <p className="mb-4">
                        Welcome to TravelKing.Live. By accessing our website and using our services, you agree to comply with and be bound by the following terms and conditions.
                    </p>
                    <h2 className="text-2xl font-bold text-white mt-8 mb-4">1. Services</h2>
                    <p className="mb-4">
                        TravelKing.Live provides flight search aggregation, EU261 compensation guidance, and luxury travel concierge services. We act as an intermediary and are not responsible for the acts or omissions of airlines or third-party providers.
                    </p>
                    <h2 className="text-2xl font-bold text-white mt-8 mb-4">2. User Obligations</h2>
                    <p className="mb-4">
                        You agree to provide accurate information when using our services. You must not use our platform for any illegal or unauthorized purpose.
                    </p>
                    <h2 className="text-2xl font-bold text-white mt-8 mb-4">3. Limitation of Liability</h2>
                    <p className="mb-4">
                        To the fullest extent permitted by law, TravelKing.Live shall not be liable for any indirect, incidental, special, consequential, or punitive damages, including without limitation, loss of profits.
                    </p>
                    <h2 className="text-2xl font-bold text-white mt-8 mb-4">4. Governing Law</h2>
                    <p className="mb-4">
                        These Terms shall be governed by and construed in accordance with the laws of the European Union and the Czech Republic.
                    </p>
                </div>
            </section>
            <Footer />
        </main>
    );
}
