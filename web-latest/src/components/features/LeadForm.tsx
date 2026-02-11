"use client";

import { Button } from '../ui/Button';

export function LeadForm() {
  return (
    <div className="w-full h-full min-h-[500px] bg-card/50 rounded-xl border border-border overflow-hidden">
        <iframe
            src="https://docs.google.com/forms/d/e/1FAIpQLSe-generic-placeholder/viewform?embedded=true"
            width="100%"
            height="100%"
            frameBorder="0"
            className="w-full h-full"
        >
            Loading...
        </iframe>
    </div>
  );
}
