"use client";

import { useState, useEffect } from "react";

export default function CookieBanner() {
    const [show, setShow] = useState(false);

    useEffect(() => {
        const consent = localStorage.getItem("tk_cookie_consent");
        if (!consent) {
            setShow(true);
        }
    }, []);

    const accept = () => {
        localStorage.setItem("tk_cookie_consent", "accepted");
        setShow(false);
    };

    if (!show) return null;

    return (
        <div className="fixed bottom-0 left-0 right-0 z-[100] p-4 md:p-6 bg-slate-900/95 backdrop-blur-xl border-t border-white/10 animate-fade-in-up">
            <div className="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between gap-4">
                <div className="text-slate-300 text-sm max-w-3xl">
                    <p>
                        <strong className="text-white">TravelKing.Live uses cookies</strong> to optimize your premium experience, analyze traffic, and ensure EU261 compliance tracking. By continuing, you agree to our <a href="/privacy-policy" className="text-amber-400 hover:underline">Privacy Policy</a>.
                    </p>
                </div>
                <div className="flex gap-4">
                    <button
                        onClick={accept}
                        className="px-6 py-2 bg-white/5 hover:bg-white/10 text-white text-sm font-medium rounded-lg border border-white/10 transition-colors"
                    >
                        Preferences
                    </button>
                    <button
                        onClick={accept}
                        className="px-6 py-2 bg-gradient-to-r from-amber-500 to-yellow-600 text-black text-sm font-bold rounded-lg hover:shadow-[0_0_15px_rgba(251,191,36,0.3)] transition-all"
                    >
                        Accept All
                    </button>
                </div>
            </div>
        </div>
    );
}
